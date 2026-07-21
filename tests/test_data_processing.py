import os
import pandas as pd


def test_processed_data_exists():
    """Validates that the pipeline output directory contains processed data assets."""
    processed_path = "data/processed/cleaned_unified_data.csv"
    assert os.path.exists(
        processed_path
    ), "Processed data asset directory path is missing!"


def test_data_schema_columns():
    """Validates that your data structure contains essential unified schema fields."""
    processed_path = "data/processed/cleaned_unified_data.csv"
    if os.path.exists(processed_path):
        df = pd.read_csv(processed_path)
        assert (
            "record_type" in df.columns
        ), "Schema error: record_type column not found!"
        assert (
            "indicator_code" in df.columns
        ), "Schema error: indicator_code column not found!"
