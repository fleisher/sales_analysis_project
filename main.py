import os
import json
from sales_analysis.data_loader import load_sales_data
from sales_analysis.analyzer import (
    total_revenue,
    revenue_by_country,
    top_products,
    revenue_by_month,
    avg_order_value,
    revenue_stats,
    revenue_confidence_interval  # добавили простой пример с scipy
)
from sales_analysis.visualizer import (
    plot_revenue_by_country,
    plot_monthly_revenue,
    plot_top_products
)


def main():
    # === 1. Загрузка данных ===
    # Определяем абсолютный путь к CSV, чтобы не зависеть от IDE
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(BASE_DIR, "data", "online_retail_II.csv")

    # Загружаем CSV → pandas DataFrame
    df = load_sales_data(filepath)

    # === 2. Анализ данных ===
    print("Общая статистика")
    print(f"Всего строк (транзакций): {len(df)}")
    print(f"Общая выручка: £{total_revenue(df):,.2f}")
    print(f"Средний чек: £{avg_order_value(df):,.2f}")

    # Статистика с использованием NumPy
    stats = revenue_stats(df)
    print("\nСтатистика по выручке (NumPy)")
    print(f"Среднее: £{stats['mean']:.2f}")
    print(f"Медиана: £{stats['median']:.2f}")
    print(f"Стандартное отклонение: £{stats['std_dev']:.2f}")
    print(f"Мин: £{stats['min']:.2f}, Макс: £{stats['max']:.2f}")

    # Пример с scipy: доверительный интервал
    mean, ci = revenue_confidence_interval(df, confidence=0.95)
    print(f"\nСредняя выручка (scipy): £{mean:.2f}")
    print(f"95% доверительный интервал: [{ci[0]:.2f}, {ci[1]:.2f}]")

    # Агрегаты
    print("\nВыручка по странам (топ-10):")
    print(revenue_by_country(df))

    print("\nТоп-10 товаров:")
    print(top_products(df))

    print("\nВыручка по месяцам:")
    print(revenue_by_month(df))

    # === 3. Экспорт отчёта в JSON ===
    report_data = {
        "total_rows": len(df),
        "total_revenue": float(total_revenue(df)),
        "avg_order_value": float(avg_order_value(df)),
        "revenue_stats": stats,
        "confidence_interval": {
            "mean": mean,
            "95_ci": ci
        },
        "top_countries": revenue_by_country(df).to_dict(orient="records"),
        "top_products": top_products(df).to_dict(orient="records"),
    }

    # Сохраняем JSON-отчёт в папку data
    report_path = os.path.join(BASE_DIR, "data", "report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=4)
    print(f"\nОтчёт сохранён: {report_path}")

    # === 4. Визуализация ===
    # Seaborn: топ стран по выручке
    plot_revenue_by_country(df, top_n=10)

    # Matplotlib: тренд выручки по месяцам
    plot_monthly_revenue(df)

    # Plotly: интерактивный график по товарам
    plot_top_products(df, top_n=10)

    # Проверка сохранения графика
    fig_path = os.path.join(BASE_DIR, "data", "top_products.png")
    fig = plot_top_products(df, top_n=10)
    fig.write_image(fig_path)
    print(f"✅ График сохранён: {fig_path}")

if __name__ == "__main__":
    main()
