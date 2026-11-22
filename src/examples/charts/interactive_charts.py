import pandas as pd
import plotly.express as ply
import urllib

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

try:
    # Extraction
    df = pd.read_csv(URL)
    print(df.head(10))

    chart = ply.scatter(data_frame=df, x="total_bill", y="tip", color="day", title="Total Bill per Tip")
    chart.show()

except (urllib.error.HTTPError or FileNotFoundError) as e:
    print("Error: the dataset not founded. Output: ", e)

finally:
    print("Program to generate charts has been executed.")