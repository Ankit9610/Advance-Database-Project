
USE FinanceTracker;

-- ---------------------------------------------------------
-- 1. Manual Insert for Users
-- ---------------------------------------------------------
-- Note: Logic assumes 100 users. Using explicit user_id to match JSON structure.
INSERT INTO Users (user_id, name, email, income) VALUES 
(1, 'User1', 'user1@finance.com', 50000.00),
(2, 'User2', 'user2@finance.com', 60000.00);
-- ... (Logic represents repetition for User3 to User100) ...


-- ---------------------------------------------------------
-- 2. Manual Insert for Categories
-- ---------------------------------------------------------
INSERT INTO Categories (category_name, type, budget) VALUES 
('Groceries', 'Expense', 300.00),
('Rent', 'Expense', 1000.00);
-- ... (Logic represents repetition for remaining categories) ...


-- ---------------------------------------------------------
-- 3. Manual Insert for Transactions
-- ---------------------------------------------------------
-- Note: transaction_id is AUTO_INCREMENT. 
-- Ensure Users and Categories exist before running this to satisfy Foreign Keys.
INSERT INTO Transactions (user_id, category_id, amount) VALUES 
(1, 1, 150.00),
(2, 2, 800.00);
-- ... (Logic represents repetition for remaining transactions) ...