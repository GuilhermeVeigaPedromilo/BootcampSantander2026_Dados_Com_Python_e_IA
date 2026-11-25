import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import urllib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

URL = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

try:
    # Extraction
    df = pd.read_csv(URL)

    print(df.head(10))

    # Transform
    df = df.dropna() # Handling NaN and Null data

    # X has values to estimate "median_house_value"
    x = df.drop("median_house_value", axis=1)
    x = pd.get_dummies(x) # Transforming categorical values into numerical values

    # Y has values will be estimate
    y = df["median_house_value"]

    # Settings of training and testing
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42 # 80% of the data is for training and 20% of the data is for testing
    )

    # Settings of the model
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    # Waste data of the model
    data_waste = y_test - y_pred

    # Generating the data waste chart:
    plt.figure(figsize=(6,5))
    plt.scatter(y_pred, data_waste)
    plt.axhline(0, color='red')
    plt.xlabel("Predict Values")
    plt.ylabel("Waste Data")
    plt.title("Data Waste vs Predict Values")

    # Calculating metrics

    # Mean Absolute Error (MAE)
    mae = mean_absolute_error(y_test, y_pred)

    # Mean Squared Error (MSE)
    mse = mean_squared_error(y_test, y_pred)

    # Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mse)

    # Mean Absolute Percentage Error (MAPE)
    mape = np.mean(np.abs((y_test - y_pred)/ y_test)) * 100

    # Coefficient of Determination
    r2 = r2_score(y_test, y_pred)

    metrics = pd.DataFrame({
        "MAE": [mae],
        "MSE": [mse],
        "RMSE": [rmse],
        "MAPE": [mape],
        "R2": [r2]
    })

    print("\nMetrics:")
    print(metrics)

    plt.show()

except (urllib.error.HTTPError, FileNotFoundError) as e:
    print("Error: dataset not found.")
    print(e)

finally:
    print("Function has been finished.")