-- Creates a database and grants user access.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER user_0d_2@localhost;
FLUSH PRIVILEGES;
CREATE USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
