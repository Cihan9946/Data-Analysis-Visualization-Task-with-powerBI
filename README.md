# Dataset information

# navigation_records_analysis_anomly_result.csv information
- **route_id**: Belirli bir rotaya ait benzersiz kimlik numarası. Bu kimlik, kayıtların hangi rotaya ait olduğunu belirlemeye yarar ve aynı rotadaki farklı kayıtları birbirinden ayırt etmeyi sağlar.

- **recorded_at**: Kaydın oluşturulduğu tarih ve saat bilgisi. Bu sütun, her bir kaydın zaman damgasını içerir ve rotanın belirli bir zaman diliminde nasıl ilerlediğini veya sapmalar gösterdiğini analiz etmede önemlidir.

- **distance**: Kaydın ilgili rotada aldığı mesafe (genellikle kilometre veya metre cinsinden). Bu mesafe, rotanın önceki noktalarına göre kat edilen toplam mesafeyi gösterir.

- **next_distance**: İlgili rotanın bir sonraki kayıt noktasına kadar olan mesafesi. Bu değer, iki kayıt noktası arasındaki mesafeyi belirler ve ani mesafe değişiklikleri gibi olası anormallikleri tespit etmek için kullanılır.


# daily_max_hour_waste.csv information
- **Date**: The specific date of waste collection (formatted as YYYY-MM-DD). This column allows for chronological tracking of waste data to observe daily patterns or seasonal trends.

- **Hour**: The hour of the day during which the waste collection data was recorded (in 24-hour format). This column helps in identifying peak times of waste collection.

- **total_waste**: The total amount of waste collected during the specified hour on that day. This figure is typically measured in units like kilograms or the number of waste items, depending on the data collection method.

# monthly_paper_plastic_total_counts_percentage.csv information
- **YearMonth**: The year and month of the data in YYYY-MM format. This column allows for tracking and comparing waste data over time.

- **Monthly Paper Percentage**: The percentage of paper waste collected relative to the total waste for that month. This value helps in understanding how much of the monthly waste consists of paper.

- **Monthly Plastic Percentage**: The percentage of plastic waste collected relative to the total waste for that month. This provides insights into the plastic waste contribution each month.

- **Monthly Total Percentage**: The overall percentage of waste (both paper and plastic) relative to the total collected waste for that month. This metric is useful for assessing how paper and plastic collectively contribute to the monthly waste.

- **Monthly Paper Total**: The total amount of paper waste collected for the month, usually measured in units such as kilograms or item count. This absolute figure gives a direct measure of paper waste quantity each month.

- **Monthly Plastic Total**: The total amount of plastic waste collected for the month, also in units such as kilograms or item count. This column shows the actual volume of plastic waste collected monthly.

# seasonal_results.csv information
- **Year**: This column indicates the year in which the data was collected. It helps to track trends over time.

- **Season**: This column specifies the season during which the data was collected. The seasons are categorized as Spring, Summer, Fall, and Winter.

- **Paper_Avg**: This column represents the average score or performance metric for paper materials in the given season and year. It is a numerical value that reflects how well paper was managed or utilized.

- **Plastic_Avg**: Similar to the Paper_Avg, this column shows the average score or performance metric for plastic materials in the specified season and year. This indicates the effectiveness of plastic management or recycling.

- **Total_Avg**: This column provides the average score that combines both paper and plastic averages for the given season and year. It gives an overall assessment of material management performance.

- **Paper_Total**: This column indicates the total quantity of paper (in presumably units like tons or kilograms) accounted for during that season and year. It reflects the volume of paper material considered in the calculations.

- **Plastic_Total**: This column represents the total quantity of plastic (again in units like tons or kilograms) accounted for during the specified season and year. It indicates the volume of plastic material included in the dataset.

    

# waste_bin_recommendations.csv information 

- **SPID**: A unique identifier for each service point. This ID allows for tracking and referencing individual locations within the dataset.

- **total_waste%**: The percentage of total waste capacity utilized at each service point. This value indicates how much of each trash bin’s capacity is used and can help identify locations where bins are either underused or nearing full capacity.

- **Case**: A recommendation or status indicator for each service point based on the waste utilization percentage. The possible values are:

- **Ideal**: The waste collection usage is at an optimal level, indicating no immediate need for adjustment.
trash can should be added: Indicates that waste levels are consistently high, suggesting an additional bin may be needed at this location to handle the waste volume.
Trash bin should be reduced: Indicates that waste levels are low, suggesting that a trash bin may be removed or relocated to optimize resources.


# weekday_weekend_summary_2019_2021.csv information
- **Year**: The year in which the data was collected.
- **Weekday # Paper**: The number of bins emptied for paper waste on weekdays.
- **Weekday % Paper**: The average fullness percentage of paper bins emptied on weekdays.
- **Weekday # Plastic**: The number of bins emptied for plastic waste on weekdays.
- **Weekday % Plastic**: The average fullness percentage of plastic bins emptied on weekdays.
- **Weekday Total**: The total number of bins emptied for both paper and plastic waste on weekdays.
- **Weekend # Paper**: The number of bins emptied for paper waste on weekends.
- **Weekend % Paper**: The average fullness percentage of paper bins emptied on weekends.
- **Weekend # Plastic**: The number of bins emptied for plastic waste on weekends.
- **Weekend % Plastic**: The average fullness percentage of plastic bins emptied on weekends.
- **Weekend Total**: The total number of bins emptied for both paper and plastic waste on weekends.

# update_navigation.csv information
- **route_id**: A unique identifier for each route. This ID is used to distinguish between different routes and allows for tracking specific route information.

- **total_distance**: The total distance covered in the route, typically measured in meters. This value represents the full length of the route and is used to analyze the scope or extent of travel along this route.

- **total_duration**: The total time taken to complete the route, usually measured in seconds. This duration helps in assessing the time efficiency and duration of travel for each route.

# waste_data_update.csv information
 
- **SPID**: A unique identifier for each service point or location where waste data is recorded. This helps to distinguish data points across different service points.

- **VisitDate**: The date and time when the waste data was collected at the service point. This timestamp is crucial for tracking the collection time and analyzing patterns over different periods.

- **Paper_No**: The number of paper waste items recorded at the service point during the visit. This indicates the quantity of paper waste collected.

- **Paper_Percentage**: The percentage of paper waste relative to the total waste collected during the visit. This helps in understanding the proportion of paper waste among the total waste.

- **Plastic_No**: The number of plastic waste items recorded at the service point during the visit. It provides the quantity of plastic waste collected.

- **Plastic_Percentage**: The percentage of plastic waste relative to the total waste collected during the visit. This helps in analyzing the composition of plastic waste as a part of the total waste.

- **total_waste_No**: The total number of waste items (including paper, plastic, and other types) collected during the visit. This gives the overall waste count for that specific visit.

- **total_waste_Percentage**: The percentage of total waste items relative to a larger dataset or waste management goal, as calculated based on certain conditions. This can be useful for assessing waste management efficiency.


# location_data_with_adress
- **SPID**: A unique identifier for each service point, representing individual waste collection locations. This ID helps to distinguish and reference each location separately.

- **Latitude**: The latitude coordinate of the waste collection point. This value indicates the north-south positioning of the location on the Earth's surface.

- **Longitude**: The longitude coordinate of the waste collection point. This value represents the east-west positioning of the location.

- **adres**: The detailed address of each waste collection point, including street names, neighborhood, district, city, and country information. This provides a full description of the location, making it easy to identify the specific area where each service point is located.

# special_day_summary_2019_2021.csv information
Special Day: This column indicates specific dates (e.g., holidays, events) on which waste collection was measured. The data is aggregated based on these notable days, reflecting changes in waste management practices during special occasions.

- **# Paper**: This column represents the number of paper items collected on the specified special day. It indicates the volume of paper waste generated or recycled during that day.

- **% Paper**: This column shows the percentage of the total waste collected that is composed of paper. It reflects how much of the waste on that special day consisted of paper materials.

- **# Plastic**: This column indicates the number of plastic items collected on the specified special day. It provides insight into the volume of plastic waste generated or recycled on that day.

- **% Plastic**: This column represents the percentage of the total waste collected that is composed of plastic. It highlights how much of the waste on that special day consisted of plastic materials.

- **Total Waste**: This column provides the total quantity of waste (in presumably units like kilograms or tons) collected on the special day. It sums up both paper and plastic waste, giving an overall picture of waste generation.