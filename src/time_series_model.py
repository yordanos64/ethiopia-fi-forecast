import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def run_financial_forecasting():
    processed_data_path = "data/processed/cleaned_unified_data.csv"

    if not os.path.exists(processed_data_path):
        print(f"[Error] Processed dataset missing at {processed_data_path}!")
        return

    print("=" * 60)
    print("      COMPLETED FORECASTING ENGINE PIPELINE EXECUTION      ")
    print("=" * 60)

    # 1. Historical Ground-Truth Benchmarks (Global Findex Data Framework)
    historical_years = np.array([2011, 2014, 2017, 2021, 2024]).reshape(-1, 1)
    historical_access = np.array([14.0, 22.0, 35.0, 46.0, 49.0])

    # 2. Fit Time Series Trend Model using Linear Regression
    model_access = LinearRegression()
    model_access.fit(historical_years, historical_access)

    # 3. Predict metrics for future target horizons (2025 - 2027)
    future_years_list = [2025, 2026, 2027]
    future_years_arr = np.array(future_years_list).reshape(-1, 1)
    predictions_access = model_access.predict(future_years_arr)

    # 4. Digital Payments Baseline Formulation (Usage Pillar Acceleration)
    base_usage_2024 = 35.0
    growth_rate_usage = 4.5
    predictions_usage = [
        base_usage_2024 + (growth_rate_usage * (year - 2024))
        for year in future_years_list
    ]

    # 5. Structure and Display Results Cleanly
    forecast_results = pd.DataFrame(
        {
            "Forecast_Year": future_years_list,
            "Access_Account_Ownership_Percent": np.round(
                predictions_access, 2
            ),
            "Usage_Digital_Payments_Percent": np.round(predictions_usage, 2),
        }
    )

    print(forecast_results.to_string(index=False))
    print("-" * 60)

    output_forecast_path = "data/processed/ethiopia_fi_predictions.csv"
    forecast_results.to_csv(output_forecast_path, index=False)
    print(f"[Success] Predictions saved to: {output_forecast_path}")


if __name__ == "__main__":
    run_financial_forecasting()
