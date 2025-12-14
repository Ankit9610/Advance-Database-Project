DELIMITER //
CREATE PROCEDURE GetUserTransactionHistory(IN uid INT)
BEGIN
    SELECT t.transaction_id, u.name, c.category_name, c.type, t.transaction_date, t.amount
    FROM Transactions t
    JOIN Users u ON t.user_id = u.user_id
    JOIN Categories c ON t.category_id = c.category_id
    WHERE t.user_id = uid;
END;
//
DELIMITER ;

CALL GetUserTransactionHistory(1);