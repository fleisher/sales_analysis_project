import pandas as pd

def load_sales_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=["InvoiceDate"])

    # Удалим возвраты или ошибочные продажи (Quantity <= 0 или Price <= 0)
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

    # Вычислим выручку
    df["Revenue"] = df["Quantity"] * df["Price"]

    return df
