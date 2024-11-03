import pandas as pd

# Veriyi CSV dosyasından okuma
df = pd.read_csv('monthly_paper_plastic_total_counts_percentage.csv')

# Sadece 2019 ve 2020 verilerini alma
df = df[df['YearMonth'] < '2021-01']

# Tarih sütununu datetime tipine çevirme ve yıl ile ay değerlerini çıkarma
df['YearMonth'] = pd.to_datetime(df['YearMonth'])
df['Year'] = df['YearMonth'].dt.year
df['Month'] = df['YearMonth'].dt.month

# Mevsimlere göre aylık verileri gruplama
seasons = {
    'Spring': [3, 4, 5],  # İlkbahar
    'Summer': [6, 7, 8, 9],  # Yaz
    'Fall': [10, 11],  # Sonbahar
    'Winter': [12, 1, 2]  # Kış
}

# Mevsimsel hesaplamaları yapmak için boş bir liste tanımlama
seasonal_data = []

# Her yıl ve mevsim için döngü ile ortalamaları ve toplamları hesaplama
for year in [2019, 2020]:
    for season, months in seasons.items():
        # Yıl ve mevsim verilerini filtreleme
        season_df = df[(df['Year'] == year) & (df['Month'].isin(months))]
        
        # Ortalama hesaplamaları
        paper_avg = season_df['Monthly Paper Percentage'].mean()
        plastic_avg = season_df['Monthly Plastic Percentage'].mean()
        total_avg = (paper_avg + plastic_avg) / 2
        
        # Toplam kutu sayısı hesaplamaları
        paper_total = season_df['Monthly Paper Total'].sum()
        plastic_total = season_df['Monthly Plastic Total'].sum()
        
        # Sonuçları listeye ekleme
        seasonal_data.append({
            'Year': year,
            'Season': season,
            'Paper_Avg': paper_avg,
            'Plastic_Avg': plastic_avg,
            'Total_Avg': total_avg,
            'Paper_Total': paper_total,
            'Plastic_Total': plastic_total
        })

# Sonuçları yeni bir DataFrame'e dönüştürme
seasonal_df = pd.DataFrame(seasonal_data)

# Sonuçları yeni bir CSV dosyasına kaydetme
seasonal_df.to_csv('seasonal_results.csv', index=False)
print("Yeni veri seti 'seasonal_results.csv' dosyasına kaydedildi.")

