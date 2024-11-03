import pandas as pd

# Veriyi yükle
waste_data = pd.read_csv('waste_data_update.csv')

# VisitDate sütununu datetime formatına çevir
waste_data['VisitDate'] = pd.to_datetime(waste_data['VisitDate'])

# Yıl bilgisi ve günün haftası
waste_data['Year'] = waste_data['VisitDate'].dt.year
waste_data['DayOfWeek'] = waste_data['VisitDate'].dt.weekday  # Pazartesi = 0, Pazar = 6

# 2021 yılı verisini 2021-03-24'e kadar sınırla
waste_data = waste_data[(waste_data['Year'] < 2021) | ((waste_data['Year'] == 2021) & (waste_data['VisitDate'] <= '2021-03-24'))]

# Hafta içi ve hafta sonu verilerini filtrele ve gruplandır
summary_data = []

for year in [2019, 2020, 2021]:
    # İlgili yılın verilerini al
    yearly_data = waste_data[waste_data['Year'] == year]
    
    # Hafta içi (Pazartesi - Cuma)
    weekday_data = yearly_data[yearly_data['DayOfWeek'] < 5]
    weekday_paper_count = weekday_data['# Paper'].sum()
    weekday_paper_percent = (weekday_data['# Paper'] * weekday_data['% Paper']).sum() / weekday_paper_count if weekday_paper_count > 0 else 0
    weekday_plastic_count = weekday_data['# Plastic'].sum()
    weekday_plastic_percent = (weekday_data['# Plastic'] * weekday_data['% Plastic']).sum() / weekday_plastic_count if weekday_plastic_count > 0 else 0
    weekday_total = weekday_data['total_waste'].sum()
    
    # Hafta sonu (Cumartesi - Pazar)
    weekend_data = yearly_data[yearly_data['DayOfWeek'] >= 5]
    weekend_paper_count = weekend_data['# Paper'].sum()
    weekend_paper_percent = (weekend_data['# Paper'] * weekend_data['% Paper']).sum() / weekend_paper_count if weekend_paper_count > 0 else 0
    weekend_plastic_count = weekend_data['# Plastic'].sum()
    weekend_plastic_percent = (weekend_data['# Plastic'] * weekend_data['% Plastic']).sum() / weekend_plastic_count if weekend_plastic_count > 0 else 0
    weekend_total = weekend_data['total_waste'].sum()
    
    # Yıl verilerini listeye ekle
    summary_data.append({
        'Year': year,
        'Weekday # Paper': weekday_paper_count,
        'Weekday % Paper': weekday_paper_percent,
        'Weekday # Plastic': weekday_plastic_count,
        'Weekday % Plastic': weekday_plastic_percent,
        'Weekday Total': weekday_total,
        'Weekend # Paper': weekend_paper_count,
        'Weekend % Paper': weekend_paper_percent,
        'Weekend # Plastic': weekend_plastic_count,
        'Weekend % Plastic': weekend_plastic_percent,
        'Weekend Total': weekend_total
    })

# Veriyi DataFrame'e çevir
summary_df = pd.DataFrame(summary_data)

# Sonucu göster
print(summary_df)

# Sonuçları bir CSV dosyasına kaydet
summary_df.to_csv("weekday_weekend_summary_2019_2021.csv", index=False)
