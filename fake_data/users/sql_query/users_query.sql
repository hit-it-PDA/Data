#### hitit DB 사용
use hitit;
show databases;

#### 마이데이터_사용자
## 마이데이터_사용자 테이블 생성
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY
);

## 마이데이터_사용자 조회
select * from users;

## 마이데이터_사용자 300명 생성
DELIMITER $$
CREATE PROCEDURE create_users()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 300 DO
        INSERT INTO users () VALUES ();
        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;

CALL create_users();