import pandas as pd

perf = pd.read_csv(
    "../data/raw/07_scheme_performance.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

result = (
    perf[
        perf["risk_grade"]
        .str.contains(
            risk,
            case=False
        )
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(
    result[
        [
            "scheme_name",
            "sharpe_ratio",
            "risk_grade"
        ]
    ]
)