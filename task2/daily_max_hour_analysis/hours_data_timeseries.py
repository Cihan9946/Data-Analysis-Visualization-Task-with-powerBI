import pandas as pd

# CSV dosyasını oku
waste_data = pd.read_csv('waste_data_update.csv')

# 'VisitDate' sütununu datetime formatına çevir ve tarih/saat bilgilerini ayır
waste_data['VisitDate'] = pd.to_datetime(waste_data['VisitDate'])
waste_data['Date'] = waste_data['VisitDate'].dt.date
waste_data['Hour'] = waste_data['VisitDate'].dt.hour

# Her gün için saat bazında toplam atık miktarını hesapla
daily_hourly_totals = waste_data.groupby(['Date', 'Hour'])['total_waste'].sum().reset_index()

# Her gün için en fazla atık toplanan saati bul
max_hour_per_day = daily_hourly_totals.loc[daily_hourly_totals.groupby('Date')['total_waste'].idxmax()]

# Sonuçları göster
print(max_hour_per_day)

# Sonuçları bir CSV dosyasına kaydet
max_hour_per_day.to_csv("daily_max_hour_waste.csv", index=False)
