import pandas as pd


def read_csv_file(file_name):
    """Read csv file and return data"""
    data = pd.read_csv(file_name)
    return data


def generate_statistics_summary(data):
    """Generate statistics summary"""
    summary = data.describe()
    print(summary)
    return summary
