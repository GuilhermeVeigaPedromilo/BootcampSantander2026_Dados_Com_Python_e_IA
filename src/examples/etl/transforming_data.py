import pandas as pd
import urllib

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

try:
    df = pd.read_csv(URL)

    df["Age"] = df["Age"].fillna(df["Age"].mean()) # Filling out null values

    print("\nCreating a new column in dataset:")
    df["age_log"] = df["Age"].apply(lambda x: x) # That copy data from "Age" column to "age_log"
    print(df[["Age", "age_log"]])

except urllib.error.HTTPError or FileNotFoundError:
    print("Error: the dataset not founded")