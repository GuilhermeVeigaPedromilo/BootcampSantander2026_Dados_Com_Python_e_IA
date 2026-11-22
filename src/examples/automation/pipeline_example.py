import pandas as pd
import urllib

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
PATH = './public/data/examples/TipsPerDay_Ecommerce.csv'

try:
    # Extraction
    df = pd.read_csv(URL)
    print(df.head())

    # Transform
    tips_per_day = df.groupby("day")["tip"].sum()
    print("\nTips per day:\n", tips_per_day)
    report = tips_per_day.reset_index(name="tips_per_day")

    # Load
    report.to_csv(PATH, index=False)

except (urllib.error.HTTPError or FileNotFoundError) as e:
    print("Error: the dataset not founded. Output: ", e)

finally:
    print("Pipeline to Tips per Day Report has been executed.")