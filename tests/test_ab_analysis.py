"""
Automated tests for the A/B testing analysis project.
Run with: pytest tests/ -v
"""

import os
import sys
import pytest
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# Ensure project root is on path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
DATA_PATH = os.path.join(ROOT, "ab_data.csv")


@pytest.fixture(scope="module")
def df():
    assert os.path.exists(DATA_PATH), f"Missing data file: {DATA_PATH}"
    return pd.read_csv(DATA_PATH)


class TestDataValidation:
    """Data quality checks that mirror the notebook's strict validation."""

    def test_required_columns(self, df):
        assert set(df.columns) == {"user_id", "group", "converted"}

    def test_no_missing_values(self, df):
        assert df.isnull().sum().sum() == 0

    def test_no_duplicate_rows(self, df):
        assert df.duplicated().sum() == 0

    def test_no_duplicate_user_ids(self, df):
        assert df.duplicated(subset=["user_id"]).sum() == 0

    def test_group_labels(self, df):
        assert set(df["group"].unique()) == {"A", "B"}

    def test_converted_binary(self, df):
        assert set(df["converted"].unique()).issubset({0, 1})

    def test_balanced_groups(self, df):
        counts = df["group"].value_counts()
        assert counts["A"] == 250
        assert counts["B"] == 250


class TestSRM:
    """Sample Ratio Mismatch test against 50/50 allocation."""

    def test_no_srm_at_strict_threshold(self, df):
        observed = df["group"].value_counts().sort_index().values
        expected = [len(df) / 2, len(df) / 2]
        _, p = stats.chisquare(f_obs=observed, f_exp=expected)
        # Industry often uses p < 0.001 as SRM flag
        assert p >= 0.001, f"SRM detected (p={p:.4f})"


class TestConversionRates:
    def test_rates_in_plausible_range(self, df):
        rates = df.groupby("group")["converted"].mean()
        assert 0 < rates["A"] < 1
        assert 0 < rates["B"] < 1

    def test_known_rates(self, df):
        rates = df.groupby("group")["converted"].mean()
        assert abs(rates["A"] - 0.14) < 1e-9
        assert abs(rates["B"] - 0.176) < 1e-9

    def test_wilson_ci_contains_point_estimate(self, df):
        for g in ["A", "B"]:
            data = df.loc[df["group"] == g, "converted"]
            rate = data.mean()
            lo, hi = proportion_confint(data.sum(), len(data), method="wilson")
            assert lo <= rate <= hi


class TestHypothesisTest:
    def test_ztest_not_significant(self, df):
        a = df.loc[df["group"] == "A", "converted"]
        b = df.loc[df["group"] == "B", "converted"]
        count = [a.sum(), b.sum()]
        nobs = [len(a), len(b)]
        _, p = proportions_ztest(count, nobs)
        assert p > 0.05, "Expected non-significant result on this dataset"

    def test_ztest_and_ttest_agree_direction(self, df):
        a = df.loc[df["group"] == "A", "converted"]
        b = df.loc[df["group"] == "B", "converted"]
        _, p_z = proportions_ztest([a.sum(), b.sum()], [len(a), len(b)])
        _, p_t = stats.ttest_ind(a, b)
        # Both should be non-significant
        assert (p_z > 0.05) == (p_t > 0.05)
