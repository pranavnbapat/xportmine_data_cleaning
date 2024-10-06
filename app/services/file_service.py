import pandas as pd


def process_excel_file(file_path: str):
    try:
        # Process the Excel file
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        raise ValueError(f"Error processing file: {str(e)}")
