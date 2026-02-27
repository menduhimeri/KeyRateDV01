import pandas as pd
from .constants import KEY_RATE_COLUMNS


class KeyRatePortfolio:
    """
    Stores portfolio key rate DV01 exposures.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self._validate_columns()

    def _validate_columns(self):
        missing = [c for c in KEY_RATE_COLUMNS if c not in self.df.columns]
        if missing:
            raise ValueError(f"Missing DV01 columns: {missing}")

    def total_exposure(self) -> pd.Series:
        return self.df[KEY_RATE_COLUMNS].sum()
