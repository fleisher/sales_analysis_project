import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd


def plot_revenue_by_country(df: pd.DataFrame, top_n: int = 10):
    """Столбчатая диаграмма: выручка по странам"""
    revenue = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(x=revenue.values, y=revenue.index)
    plt.title(f"Топ-{top_n} стран по выручке")
    plt.xlabel("Выручка")
    plt.ylabel("Страна")
    plt.show()


def plot_monthly_revenue(df: pd.DataFrame):
    """Линейный график выручки по месяцам"""
    df["Month"] = df["InvoiceDate"].dt.to_period("M")
    monthly_revenue = df.groupby("Month")["Revenue"].sum()

    plt.figure(figsize=(12, 6))
    monthly_revenue.plot(kind="line", marker="o")
    plt.title("Выручка по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Выручка")
    plt.grid(True)
    plt.show()


def plot_top_products(df: pd.DataFrame, top_n: int = 10):
    """Интерактивный график топ продуктов"""
    top_products = (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Revenue",
        y="Description",
        orientation="h",
        title=f"Топ-{top_n} товаров по выручке",
    )
    fig.show()
