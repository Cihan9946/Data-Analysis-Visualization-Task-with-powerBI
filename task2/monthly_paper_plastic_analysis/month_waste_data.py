import pandas as pd

# CSV dosyasını oku
waste_data = pd.read_csv('waste_data_update.csv')

# 'VisitDate' sütununu datetime formatına çevir
waste_data['VisitDate'] = pd.to_datetime(waste_data['VisitDate'])

# Yıl ve ay bilgisine göre gruplandırarak işlem yapacağız
waste_data['YearMonth'] = waste_data['VisitDate'].dt.to_period('M')

# Aylık hesaplama fonksiyonu
def monthly_percentage(df, column_count, column_percentage):
    # Her ay için (column_count * column_percentage) toplamı ve column_count toplamı
    weighted_sum = (df[column_count] * df[column_percentage]).sum()
    total_sum = df[column_count].sum()
    # Aylık yüzdelik ortalamayı hesapla
    return weighted_sum / total_sum if total_sum > 0 else 0

# Her ay için aylık yüzdelik ortalamaları hesapla
monthly_results = waste_data.groupby('YearMonth').apply(
    lambda x: pd.Series({
        'Monthly Paper Percentage': monthly_percentage(x, '# Paper', '% Paper'),
        'Monthly Plastic Percentage': monthly_percentage(x, '# Plastic', '% Plastic')
    })
).reset_index()

# Sonuçları görüntüle
print(monthly_results)

# Yeni sonuçları bir CSV dosyasına kaydet
monthly_results.to_csv("monthly_paper_plastic_percentage.csv", index=False)
