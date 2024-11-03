import pandas as pd
import pyodbc




# SQL Server bağlantısı kur
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};''SERVER=METEHAN\SQLEXPRESS;''DATABASE=task1db;' 'Trusted_Connection=yes;'
)


query = """
-- Veriyi route_id ve recorded_at alanlarına göre sıralı olarak numaralandırıyoruz.
WITH SortedData AS (
    SELECT
        route_id,
        recorded_at,
        distance,
        ROW_NUMBER() OVER(PARTITION BY route_id ORDER BY recorded_at) AS rn
    FROM navigation_records
),
-- Mesafe farkını önceki satıra göre hesaplıyoruz.
DistanceDiff AS (
    SELECT
        sd.route_id,
        sd.recorded_at,
        sd.distance,
        sd.distance - LAG(sd.distance) OVER (PARTITION BY sd.route_id ORDER BY sd.recorded_at) AS distance_diff
    FROM SortedData sd
),
-- Eğer mesafe farkı negatifse, bu farkı mesafe ile değiştiriyoruz.
AdjustedDistance AS (
    SELECT
        dd.route_id,
        dd.recorded_at,
        dd.distance,
        CASE 
            WHEN dd.distance_diff >= 0 THEN dd.distance_diff
            ELSE dd.distance
        END AS adjusted_distance
    FROM DistanceDiff dd
),
-- Kümülatif mesafeyi hesaplayarak mesafenin her kayıtta nasıl değiştiğini buluyoruz.
CumulativeDistance AS (
    SELECT
        ad.route_id,
        ad.recorded_at,
        ad.distance,
        SUM(ad.adjusted_distance) OVER (PARTITION BY ad.route_id ORDER BY ad.recorded_at ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_distance,
        LAG(ad.recorded_at) OVER (PARTITION BY ad.route_id ORDER BY ad.recorded_at) AS prev_recorded_at
    FROM AdjustedDistance ad
),
-- Nihai veriyi hazırlıyoruz; toplam mesafe ve toplam süreyi her bir route_id için hesaplıyoruz.
FinalData AS (
    SELECT
        cd.route_id,
        MAX(cd.cumulative_distance) AS total_distance,
        SUM(DATEDIFF(SECOND, cd.prev_recorded_at, cd.recorded_at)) AS total_duration
    FROM CumulativeDistance cd
    GROUP BY cd.route_id
)
-- Sonuçları `route_id`, toplam mesafe ve toplam süre olarak seçiyoruz.
SELECT
    route_id,
    total_distance,
    total_duration
FROM FinalData;
"""






# Sorguyu çalıştır ve sonucu pandas veri çerçevesine al
result = pd.read_sql_query(query, conn)
result.to_csv('update_navigation.csv',index=False)





# Sonuçları göster
print(result)

# Bağlantıyı kapat
conn.close()