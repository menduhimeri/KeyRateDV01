import pandas as pd
from .constants import KEY_RATE_COLUMNS
from .scenario import Scenario
from .portfolio import KeyRatePortfolio


class KeyRateDV01Calculator:

    def __init__(self, portfolio: KeyRatePortfolio):
        self.portfolio = portfolio

    def run_scenario(self, scenario: Scenario) -> dict:
        exposures = self.portfolio.total_exposure()

        pnl_by_keyrate = {
            col: exposures[col] * scenario.get_shock(col)
            for col in KEY_RATE_COLUMNS
        }

        total_pnl = sum(pnl_by_keyrate.values())

        return {
            "Scenario": scenario.name,
            "Total PnL": total_pnl,
            "Breakdown": pnl_by_keyrate
        }

    def run_all_matrix(self, scenarios: list[Scenario]) -> pd.DataFrame:
        """
        Returns a DataFrame where:
        - rows = scenarios
        - columns = key rates + total parallel DV01
        """
        records = []

        for sc in scenarios:
            res = self.run_scenario(sc)
            row = res["Breakdown"]
            row["Total Parallel DV01"] = res["Total PnL"]
            row["Scenario"] = res["Scenario"]
            records.append(row)

        df = pd.DataFrame(records)
        # Put Scenario first, Total last
        cols = ["Scenario"] + KEY_RATE_COLUMNS + ["Total Parallel DV01"]
        return df[cols]

