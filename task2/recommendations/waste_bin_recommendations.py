import pandas as pd

# Veriyi yükle
waste_data = pd.read_csv('waste_data_update.csv')

# VisitDate sütununu datetime formatına çevir
waste_data['VisitDate'] = pd.to_datetime(waste_data['VisitDate'])

# SPID bazında total_waste% ortalamasını hesapla
spid_summary = waste_data.groupby('SPID').agg({
    'total_waste%': 'mean'  # Her SPID için total_waste% ortalamasını al
}).reset_index()

# Koşullara göre sınıflandırma yap
def classify_waste_level(average):
    if average >= 0.90:
        return "trash can should be added"
    elif average < 0.50:
        return "Trash bin should be reduced"
    else:
        return "Ideal"

# Sınıflandırmayı yeni bir sütun olarak ekle
spid_summary['Case'] = spid_summary['total_waste%'].apply(classify_waste_level)

# Sonuçları göster
print(spid_summary)

# Sonuçları bir CSV dosyasına kaydet
spid_summary.to_csv("waste_bin_recommendations.csv", index=False)
