-- valid email trigger
DROP TRIGGER IF EXISTS valid_email;
DELIMITER //
CREATE TRIGGER valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = NEW.valid_email;
	END IF;
END //
DELIMITER ;
