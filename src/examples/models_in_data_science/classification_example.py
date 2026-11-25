import pandas as pd
import urllib

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

URL = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

try:
    # Extraction
    df = pd.read_csv(URL)

    print("First rows of the dataset:")
    print(df.head())

    # Transform
    df = df.dropna()  # Handling NaN and Null data

    # Creating a binary target variable based on the median house value
    df_class = df.copy()

    df_class["HighPrice"] = (
        df_class["median_house_value"]
        > df_class["median_house_value"].median()
    ).astype(int)

    print("\nTransformed dataset:")
    print(df_class.head())

    # Features and target variable
    x = df_class.drop(
        ["median_house_value", "HighPrice"],
        axis=1
    )

    x = pd.get_dummies(
        x
    )  # Transforming categorical values into numerical values

    y = df_class["HighPrice"]

    # Settings of training and testing
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,  # 80% of the data is for training and 20% of the data is for testing
        random_state=42
    )

    # Solving by Logistic Regression
    clf = LogisticRegression(max_iter=1000)

    clf.fit(x_train, y_train)

    # Predictions
    y_pred = clf.predict(x_test)

    # Model evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\n===== MODEL METRICS =====")
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-Score : {f1:.4f}")

    print("\n===== CLASSIFICATION REPORT =====")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")
    plt.title("Confusion Matrix")

    plt.show()

except (urllib.error.HTTPError, FileNotFoundError) as e:
    print("Error: dataset not found.")
    print(e)

except Exception as e:
    print("Unexpected error:")
    print(e)

finally:
    print("\nFunction has been finished.")