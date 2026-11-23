import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import urllib

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

try:
    # Extraction
    df = pd.read_csv(URL)

    print(df.head(10))

    # Pie chart
    bill_per_day = df.groupby("day")["total_bill"].sum()

    plt.figure(figsize=(8, 6))
    plt.pie(
        bill_per_day,
        labels=bill_per_day.index,
        autopct="%1.1f%%"
    )
    plt.title("Total Bill per Day")

    # Scatter Plot Plotly
    chart = px.scatter(
        data_frame=df,
        x="total_bill",
        y="tip",
        color="day",
        title="Total Bill vs Tip"
    )

    chart.show()
    plt.show()

except (urllib.error.HTTPError, FileNotFoundError) as e:
    print("Error: dataset not found.")
    print(e)

finally:
    print("Program to generate charts has been executed.")