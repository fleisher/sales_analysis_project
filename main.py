import os
from sales_analysis.data_loader import load_sales_data
from sales_analysis.analyzer import (
    total_revenue,
    revenue_by_country,
    top_products,
    revenue_by_month,
    avg_order_value
)
from sales_analysis.visualizer import (
    plot_revenue_by_country,
    plot_monthly_revenue,
    plot_top_products
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, "data", "online_retail_II.csv")

df = load_sales_data(filepath)

print("📊 Общая статистика")
print(f"Всего строк: {len(df)}")
print(f"Общая выручка: £{total_revenue(df):,.2f}")
print(f"Средний чек: £{avg_order_value(df):,.2f}")

print("\n🌍 Выручка по странам (топ-10):")
print(revenue_by_country(df))

print("\n🏆 Топ-10 товаров:")
print(top_products(df))

print("\n📅 Выручка по месяцам:")
print(revenue_by_month(df))

# === Визуализация ===
plot_revenue_by_country(df, top_n=10)
plot_monthly_revenue(df)
plot_top_products(df, top_n=10)
