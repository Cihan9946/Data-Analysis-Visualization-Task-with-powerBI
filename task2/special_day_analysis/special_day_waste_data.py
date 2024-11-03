import pandas as pd

# Veriyi yükle
waste_data = pd.read_csv('waste_data_update.csv')

# VisitDate sütununu datetime formatına çevir
waste_data['VisitDate'] = pd.to_datetime(waste_data['VisitDate'])

# Türkiye'nin 2019, 2020 ve 2021 yıllarındaki özel günleri
special_days = [
    # 2019 yılı
    '2019-01-01',  # Yılbaşı
    '2019-04-23',  # Ulusal Egemenlik ve Çocuk Bayramı
    '2019-05-01',  # Emek ve Dayanışma Günü
    '2019-05-19',  # Atatürk'ü Anma, Gençlik ve Spor Bayramı
    '2019-06-04',  # Ramazan Bayramı Arife Günü
    '2019-06-05',  # Ramazan Bayramı 1. Gün
    '2019-06-06',  # Ramazan Bayramı 2. Gün
    '2019-06-07',  # Ramazan Bayramı 3. Gün
    '2019-07-15',  # Demokrasi ve Millî Birlik Günü
    '2019-08-10',  # Kurban Bayramı Arife Günü
    '2019-08-11',  # Kurban Bayramı 1. Gün
    '2019-08-12',  # Kurban Bayramı 2. Gün
    '2019-08-13',  # Kurban Bayramı 3. Gün
    '2019-08-14',  # Kurban Bayramı 4. Gün
    '2019-08-30',  # Zafer Bayramı
    '2019-10-29',  # Cumhuriyet Bayramı

    # 2020 yılı
    '2020-01-01',  # Yılbaşı
    '2020-04-23',  # Ulusal Egemenlik ve Çocuk Bayramı
    '2020-05-01',  # Emek ve Dayanışma Günü
    '2020-05-19',  # Atatürk'ü Anma, Gençlik ve Spor Bayramı
    '2020-05-23',  # Ramazan Bayramı Arife Günü
    '2020-05-24',  # Ramazan Bayramı 1. Gün
    '2020-05-25',  # Ramazan Bayramı 2. Gün
    '2020-05-26',  # Ramazan Bayramı 3. Gün
    '2020-07-15',  # Demokrasi ve Millî Birlik Günü
    '2020-07-30',  # Kurban Bayramı Arife Günü
    '2020-07-31',  # Kurban Bayramı 1. Gün
    '2020-08-01',  # Kurban Bayramı 2. Gün
    '2020-08-02',  # Kurban Bayramı 3. Gün
    '2020-08-03',  # Kurban Bayramı 4. Gün
    '2020-08-30',  # Zafer Bayramı
    '2020-10-29',  # Cumhuriyet Bayramı

    # 2021 yılı (Mart sonuna kadar veri mevcut)
    '2021-01-01',  # Yılbaşı
    '2021-04-23',  # Ulusal Egemenlik ve Çocuk Bayramı
    '2021-05-01',  # Emek ve Dayanışma Günü
    '2021-05-19',  # Atatürk'ü Anma, Gençlik ve Spor Bayramı
    '2021-05-12',  # Ramazan Bayramı Arife Günü
    '2021-05-13',  # Ramazan Bayramı 1. Gün
    '2021-05-14',  # Ramazan Bayramı 2. Gün
    '2021-05-15',  # Ramazan Bayramı 3. Gün
    '2021-07-15',  # Demokrasi ve Millî Birlik Günü
    '2021-07-19',  # Kurban Bayramı Arife Günü
    '2021-07-20',  # Kurban Bayramı 1. Gün
    '2021-07-21',  # Kurban Bayramı 2. Gün
    '2021-07-22',  # Kurban Bayramı 3. Gün
    '2021-07-23',  # Kurban Bayramı 4. Gün
    '2021-08-30',  # Zafer Bayramı
    '2021-10-29'   # Cumhuriyet Bayramı
]

# Tarihleri datetime formatına çevir
special_days = pd.to_datetime(special_days)

# Sadece özel günlere ait verileri filtrele ve toplam/ortalama değerlerini hesapla
special_day_summary = waste_data[waste_data['VisitDate'].dt.date.isin(special_days.date)]
special_day_summary = (
    special_day_summary
    .groupby(special_day_summary['VisitDate'].dt.date)
    .agg({
        '# Paper': 'sum',         # Kağıt kutu sayısı toplamı
        '% Paper': 'mean',        # Kağıt yüzdesi ortalaması
        '# Plastic': 'sum',       # Plastik kutu sayısı toplamı
        '% Plastic': 'mean',      # Plastik yüzdesi ortalaması
        'total_waste': 'sum'      # Toplam atık miktarı
    })
    .reset_index()
    .rename(columns={'VisitDate': 'Special Day'})
)

# Sonuçları göster
print(special_day_summary)

# Sonuçları bir CSV dosyasına kaydet
special_day_summary.to_csv("special_day_summary_2019_2021.csv", index=False)
