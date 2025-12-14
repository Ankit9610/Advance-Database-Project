-- Inner Join for transaction details
SELECT t.transaction_id, u.name, c.category_name, t.amount, t.transaction_date
FROM Transactions t
JOIN Users u ON t.user_id = u.user_id
JOIN Categories c ON t.category_id = c.category_id;

-- Total spent by user
SELECT u.name, SUM(t.amount) AS total_spent
FROM Transactions t
JOIN Users u ON t.user_id = u.user_id
GROUP BY u.user_id;

-- Left Join for users with transaction counts
SELECT u.name, COUNT(t.transaction_id) AS transaction_count
FROM Users u
LEFT JOIN Transactions t ON u.user_id = t.user_id
GROUP BY u.user_id;