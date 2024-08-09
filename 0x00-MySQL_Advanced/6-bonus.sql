-- create prodedure to add new row
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), 
	score FLOAT)
BEGIN
	DECLARE p_count INT default 0;
	DECLARE p_id INT default 0;
	SELECT count(id) INTO p_count FROM projects
	WHERE name = project_name;

	IF p_count = 0 THEN
		INSERT into projects(name)
		VALUES (project_name);
	END IF;
	SELECT id INTO p_id FROM projects WHERE
	name = project_name;
	INSERT into corrections(user_id,project_id,score)
	VALUES (user_id, p_id, score);
END //
DELIMITER ;
