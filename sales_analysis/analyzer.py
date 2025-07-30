from scipy import stats
import pandas as pd
import numpy as np


def total_revenue(df: pd.DataFrame) -> float:
    """Общая выручка"""
    return df["Revenue"].sum()


def revenue_by_country(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Выручка по странам (топ N)"""
    return (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )


def top_products(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Топ товаров по выручке"""
    return (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )


def revenue_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """Выручка по месяцам"""
    df["Month"] = df["InvoiceDate"].dt.to_period("M")
    return (
        df.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
        .sort_values("Month")
    )


def avg_order_value(df: pd.DataFrame) -> float:
    """Средний чек"""
    order_totals = df.groupby("Invoice")["Revenue"].sum()
    return order_totals.mean()


def revenue_stats(df: pd.DataFrame) -> dict:
    """Базовая статистика по выручке с использованием NumPy"""
    revenues = df["Revenue"].values
    return {
        "mean": float(np.mean(revenues)),
        "median": float(np.median(revenues)),
        "std_dev": float(np.std(revenues)),
        "min": float(np.min(revenues)),
        "max": float(np.max(revenues)),
    }

def revenue_confidence_interval(df: pd.DataFrame, confidence: float = 0.95) -> tuple:
    """Доверительный интервал для среднего значения выручки"""
    revenues = df["Revenue"].values
    mean = np.mean(revenues)
    sem = stats.sem(revenues)  # стандартная ошибка среднего
    ci = stats.t.interval(confidence, len(revenues)-1, loc=mean, scale=sem)
    return mean, ci