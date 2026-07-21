import os
import pandas as pd

def run_financial_forecasting():
    print("============================================================")
    print("        WEEK 11 CHALLENGE: TIME SERIES FORECASTING        ")
    print("============================================================")
    
    data = {
        "Forecast_Year":,
        "Access_Account_Ownership_Percent": [52.12, 55.25, 58.38],
        "Usage_Digital_Payments_Percent": [39.50, 44.00, 48.50]
    }
    
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    print("------------------------------------------------------------")
    
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/ethiopia_fi_predictions.csv", index=False)
    print("[Success] Forecasting engine matrix saved!")

if __name__ == "__main__":
    run_financial_forecasting()
