DELIMITER //

CREATE PROCEDURE list_tables_in_database(IN database_name VARCHAR(255))
BEGIN
    SET @query = CONCAT('USE ', database_name, ';');
    PREPARE statement FROM @query;
    EXECUTE statement;
    DEALLOCATE PREPARE statement;

    SHOW TABLES;
END //

DELIMITER ;

