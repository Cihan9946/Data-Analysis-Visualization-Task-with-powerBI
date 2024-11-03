import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Dosyayı oku
file_path = 'location_data.csv'  # Dosyanızın adını buraya ekleyin
location_data = pd.read_csv(file_path)

# Geopy kullanarak adres almak için Nominatim geocoding servisini tanımla
geolocator = Nominatim(user_agent="geoapiExercises")
geocode = RateLimiter(geolocator.reverse, min_delay_seconds=1)  # Hız sınırlandırması için

# Adres bilgisi eklemek için bir fonksiyon tanımla
def get_address(lat, lon):
    try:
        location = geocode((lat, lon), language='tr')  # Adresi Türkçe döndürmesi için
        return location.address if location else "Adres bulunamadı"
    except:
        return "Hata"

# Yeni bir 'adres' sütunu ekle
location_data['adres'] = location_data.apply(lambda row: get_address(row['Latitude'], row['Longitude']), axis=1)

# Sonuçları yeni bir CSV dosyasına kaydet
location_data.to_csv('location_data_with_address.csv', index=False)

print("Adres sütunu eklendi ve yeni dosya 'location_data_with_address.csv' olarak kaydedildi.")
