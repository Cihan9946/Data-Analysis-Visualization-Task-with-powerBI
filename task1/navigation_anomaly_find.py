import pandas as pd
import pyodbc

# SQL Server bağlantısı kur
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};''SERVER=METEHAN\SQLEXPRESS;''DATABASE=task1db;' 'Trusted_Connection=yes;'
)




queryanalysis = """

SELECT * FROM navigation_records WHERE distance = 0;

"""

queryanalysis1 = """

WITH AnomalyCheck AS (
    SELECT 
        route_id,
        recorded_at,
        distance,
        LEAD(distance) OVER (ORDER BY recorded_at) AS next_distance
    FROM navigation_records
)
SELECT *
FROM AnomalyCheck
WHERE distance > next_distance;

"""

zero_distance_rows = pd.read_sql_query(queryanalysis,conn)
zero_distance_rows.to_csv('navigation_records_zero_anomaly_results.csv',index=False)

print(zero_distance_rows)

anomaly_check_rows  = pd.read_sql_query(queryanalysis1,conn)
anomaly_check_rows.to_csv('navigation_records_analysis_anomaly_results.csv',index=False)
print(anomaly_check_rows)




conn.close()