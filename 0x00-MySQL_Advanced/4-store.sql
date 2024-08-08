-- script to build update trigger
DROP TRIGGER IF EXISTS item_update;
DELIMITER //
CREATE TRIGGER item_update
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items set quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END //
DELIMITER ;
