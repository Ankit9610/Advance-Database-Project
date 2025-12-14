DELIMITER //
CREATE TRIGGER after_transaction_insert
AFTER INSERT ON Transactions
FOR EACH ROW
BEGIN
    UPDATE Users SET total_transactions = total_transactions + 1 WHERE user_id = NEW.user_id;
END;
//
DELIMITER ;