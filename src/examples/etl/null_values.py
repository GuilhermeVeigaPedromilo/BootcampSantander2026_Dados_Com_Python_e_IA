import pandas as pd
import urllib

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

try:
    df = pd.read_csv(URL)

    print("\nData frame summary:")
    data = df.head()
    print(data)

    print("\nData frame info:")
    df.info()

    print("\nData frame description:")
    data = df.describe()
    print(data)
    print("\nSum of null values of each column:\n", df.isnull().sum())

    print("\nRemoving NaN values:")
    nanRemoved = df.dropna()
    print(nanRemoved.head())

    print("\nFilling out null values with the average:")
    df["Cabin"] = df["Cabin"].fillna(df["Cabin"].mean)
    
    print("\nVerfying if there is any null register at Cabin column:")
    print(df["Cabin"].isnull())

except urllib.error.HTTPError or FileNotFoundError:
    print("Error: the dataset not founded")