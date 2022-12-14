--https://leetcode.com/problems/rising-temperature

SELECT A.id 
FROM Weather A, Weather B
WHERE B.recordDate = A.recordDate - INTERVAL 1 DAY AND A.temperature > B.temperature