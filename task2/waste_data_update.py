import pandas as pd

# CSV dosyasını oku
waste_data = pd.read_csv('waste_data_timeseries.csv')

# Temizleme işlemi: 1'den büyük olan değerleri 1 olarak ayarla
waste_data['% Paper'] = waste_data['% Paper'].apply(lambda x: min(x, 1))
waste_data['% Plastic'] = waste_data['% Plastic'].apply(lambda x: min(x, 1))




# Gerekli sütunlar: '# Paper', '% Paper', '# Plastic', '% Plastic'
# 1. 'total_waste' sütununu ekleyelim: # Paper ve # Plastic değerlerinin toplamı
waste_data['total_waste'] = waste_data['# Paper'] + waste_data['# Plastic']

# 2. 'total_waste%' sütununu ekleyelim: ((# Paper * % Paper) + (# Plastic * % Plastic)) / ( # Paper + # Plastic )
waste_data['total_waste%'] = ((waste_data['# Paper'] * waste_data['% Paper']) + (waste_data['# Plastic'] * waste_data['% Plastic'])) / waste_data['total_waste']

# Tarih sıralaması için 'VisitDate' sütununu datetime formatına çevirelim ve sıralama yapalım
waste_data['VisitDate'] = pd.to_datetime(waste_data['VisitDate'])
waste_data = waste_data.sort_values(by='VisitDate')

# İşlemin başarılı olup olmadığını kontrol edelim
waste_data[['# Paper', '% Paper', '# Plastic', '% Plastic', 'total_waste', 'total_waste%']].head()

waste_data.to_csv("waste_data_update.csv", index=False)



data_types = waste_data.dtypes
print(data_types)







