-- View all BMW data
SELECT * FROM bmw_data;

-- Average BMW closing price
SELECT AVG(Close) AS average_close_price
FROM bmw_data;

-- Highest BMW closing price
SELECT MAX(Close) AS highest_close_price
FROM bmw_data;

-- Lowest BMW closing price
SELECT MIN(Close) AS lowest_close_price
FROM bmw_data;

-- Find days where BMW closing price was above 100
SELECT *
FROM bmw_data
WHERE Close > 100;

-- Sort BMW prices from highest to lowest
SELECT *
FROM bmw_data
ORDER BY Close DESC;
SELECT * FROM bmw_data;

SELECT AVG(close) AS average_bmw_close
FROM bmw_data;

SELECT MAX(close) AS highest_bmw_close
FROM bmw_data;

SELECT MIN(close) AS lowest_bmw_close
FROM bmw_data;

SELECT AVG(close) AS average_porsche_close
FROM porsche_data;

SELECT MAX(close) AS highest_porsche_close
FROM porsche_data;

SELECT MIN(close) AS lowest_porsche_close
FROM porsche_data;