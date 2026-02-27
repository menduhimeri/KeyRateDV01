import pandas as pd
from keyrate import Scenario, KeyRatePortfolio, KeyRateDV01Calculator, KEY_RATE_COLUMNS


def build_sample_portfolio():
    data = {col: [0.0] for col in KEY_RATE_COLUMNS}

    data["ONE YR NET DV01"] = [1200]
    data["FIVE YR NET DV01"] = [800]
    data["TEN YR NET DV01"] = [1500]

    return pd.DataFrame(data)


def build_scenarios():
    parallel_up = Scenario(
        "Parallel +1bp",
        {col: 1 for col in KEY_RATE_COLUMNS}
    )

    steepener = Scenario(
        "Steepener",
        {
            "ONE YR NET DV01": -1,
            "FIVE YR NET DV01": 0,
            "TEN YR NET DV01": 1
        }
    )

    return [parallel_up, steepener]


def main():
    df = build_sample_portfolio()
    portfolio = KeyRatePortfolio(df)

    scenarios = build_scenarios()

    calc = KeyRateDV01Calculator(portfolio)
    matrix = calc.run_all_matrix(scenarios)

    # Print the matrix nicely
    pd.set_option("display.float_format", "{:,.2f}".format)
    print("\nKey Rate DV01 Matrix per Scenario:")
    print(matrix)


if __name__ == "__main__":
    main()
