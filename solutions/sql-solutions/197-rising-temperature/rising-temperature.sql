# Write your MySQL query statement below
SELECT id
FROM (
    SELECT id, temperature, LAG(temperature)
    OVER (ORDER BY recordDate) AS prev_temperature,
    recordDate, LAG(recordDate) OVER (ORDER BY recordDate) AS prevDate
    FROM Weather
) AS subquery
WHERE temperature > prev_temperature AND DATEDIFF(recordDate, prevDate) = 1;