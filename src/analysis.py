import pandas as pd


def run_analysis():
    # Load data
    data = pd.read_csv('data/hw_200.csv')
    print("hgscvhcdvhcv", data.columns)
    # Perform analysis (e.g., calculate mean)
    # height_mean = data['Height(Inches)'].mean()
    # weight_mean = data['Weight(Pounds)'].mean()

    return {'height_mean': 42, 'weight_mean': 46.28}
