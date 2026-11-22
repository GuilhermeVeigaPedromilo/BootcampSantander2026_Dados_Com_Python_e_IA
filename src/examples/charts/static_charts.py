import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sbn
import urllib

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

try:
    # Extraction
    df = pd.read_csv(URL)
    print(df.head(10))

    sbn.scatterplot(data=df, x="total_bill", y="tip")
    pyplot.show()

except (urllib.error.HTTPError or FileNotFoundError) as e:
    print("Error: the dataset not founded. Output: ", e)

finally:
    print("Program to generate charts has been executed.")