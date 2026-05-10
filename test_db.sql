DROP DATABASE IF EXISTS test_db;
CREATE DATABASE test_db;

USE test_db;

CREATE TABLE products (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(10),
    quantity INT,
    total_price DECIMAL(10,2),
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO products (id,name,price,stock) VALUES
('u21ht','boll',250.00,13);

INSERT INTO products (id,name,price,stock) VALUES
('u21yt','basket',150.00,5),
('u21io','iron scale',30.00,12),
('u21se','chess',300.00,6),
('u21po','bat',16.00,55),
('u21ve','box',45.00,55)
;





















