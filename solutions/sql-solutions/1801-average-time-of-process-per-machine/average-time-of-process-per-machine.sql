# Write your MySQL query statement below
SELECT machine_id, ROUND(AVG(end_time - timestamp), 3)
AS processing_time
FROM (
    SELECT machine_id, timestamp, LEAD(timestamp)
    OVER (PARTITION BY machine_id, process_id ORDER BY activity_type) AS end_time,
    activity_type
    FROM Activity
) AS subquery
WHERE end_time - timestamp IS NOT NULL
GROUP BY machine_id;