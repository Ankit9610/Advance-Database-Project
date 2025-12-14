CREATE DATABASE FinanceTracker;
USE FinanceTracker;

-- Users table (structured user accounts)
CREATE TABLE Users (
    user_id INT  PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    income DECIMAL(10,2),
    total_transactions INT DEFAULT 0
);

-- Categories table (structured categories)
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    type ENUM('Expense', 'Income', 'Savings') NOT NULL,
    budget DECIMAL(10,2)
);

-- Transactions table (structured transactions for ACID)
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10,2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL
);

-- Indexes for optimization
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_category_type ON Categories(type);
CREATE INDEX idx_transaction_user ON Transactions(user_id);
CREATE INDEX idx_transaction_date ON Transactions(transaction_date);