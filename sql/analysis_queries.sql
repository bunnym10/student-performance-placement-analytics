-- 1. Total number of students
SELECT COUNT(*) AS total_students
FROM students;


-- 2. Department-wise student count
SELECT department, COUNT(*) AS total_students
FROM students
GROUP BY department
ORDER BY total_students DESC;


-- 3. Placed and not-placed student count
SELECT placement_status, COUNT(*) AS total_students
FROM students
GROUP BY placement_status;


-- 4. Overall placement percentage
SELECT
    ROUND(
        SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS placement_percentage
FROM students;


-- 5. Department-wise placement percentage
SELECT
    department,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END) AS placed_students,
    ROUND(
        SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS placement_percentage
FROM students
GROUP BY department
ORDER BY placement_percentage DESC;


-- 6. Average performance by placement status
SELECT
    placement_status,
    COUNT(*) AS total_students,
    ROUND(AVG(cgpa), 2) AS average_cgpa,
    ROUND(AVG(attendance), 2) AS average_attendance,
    ROUND(AVG(aptitude_score), 2) AS average_aptitude,
    ROUND(AVG(technical_skills), 2) AS average_technical_skills
FROM students
GROUP BY placement_status;