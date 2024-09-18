-- ORDER

CREATE TABLE "Order" (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    customer_address_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(10) CHECK (status IN ('pending', 'payed', 'waiting', 'canceled')),
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES "Customer"(id),
    CONSTRAINT fk_address FOREIGN KEY (customer_address_id) REFERENCES "Address"(id)
);

-- indexes 
CREATE INDEX idx_order_customer_id ON "Order"(customer_id);
CREATE INDEX idx_order_customer_address_id ON "Order"(customer_address_id);


--  USER

CREATE TABLE "User" (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20),
    birth_date DATE,
    gender VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);


-- SELLER

CREATE TABLE "Seller" (
    id SERIAL PRIMARY KEY,
    document VARCHAR(20) NOT NULL,
    user_id INT REFERENCES "User"(id),
    description TEXT,
    rate FLOAT
    CONSTRAINT fk_seller_user FOREIGN KEY (user_id) REFERENCES "User"(id)
);

-- indexes
CREATE INDEX idx_seller_user_id ON "Seller"(user_id);


-- CUSTOMER

CREATE TABLE "Customer" (
    id SERIAL PRIMARY KEY,
    document VARCHAR(20) NOT NULL,
    user_id INT REFERENCES "User"(id)
    CONSTRAINT fk_customer_user FOREIGN KEY (user_id) REFERENCES "User"(id)
);
-- indexes
CREATE INDEX idx_customer_user_id ON "Customer"(user_id);

-- ADDRESS

CREATE TABLE "Address" (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(100),
    street VARCHAR(255),
    number VARCHAR(10),
    zip_code VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Address x User (n X 1)

CREATE TABLE "Address_User" (
    address_id INT UNIQUE REFERENCES "Address"(id),
    user_id INT REFERENCES "User"(id),
    CONSTRAINT fk_address FOREIGN KEY (address_id) REFERENCES "Address"(id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES "User"(id),
    PRIMARY KEY (address_id, user_id)
);
-- indexes
CREATE INDEX idx_address_user_address_id ON "Address_User"(address_id);
CREATE INDEX idx_address_user_user_id ON "Address_User"(user_id);

-- Order x User (n X 1)

CREATE TABLE "Order_User" (
    order_id INT REFERENCES "Order"(id),
    user_id INT REFERENCES "User"(id),
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES "Order"(id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES "User"(id),
    PRIMARY KEY (order_id, user_id)
);
-- indexes
CREATE INDEX idx_order_user_order_id ON "Order_User"(order_id);
CREATE INDEX idx_order_user_user_id ON "Order_User"(user_id);

-- PRODUCT 

CREATE TABLE "Product" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    seller_id INT REFERENCES "Seller"(id),
    image TEXT,
    thumbnail TEXT,
    description TEXT,
    value DECIMAL(10, 2),
    amount INT,
    status VARCHAR(20),
    brand VARCHAR(100),
    rate FLOAT
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_seller FOREIGN KEY (seller_id) REFERENCES "Seller"(id)
);
-- indexes
CREATE INDEX idx_product_seller_id ON "Product"(seller_id);

-- Order x Product (n X n)

CREATE TABLE "Order_Product" (
    product_id INT REFERENCES "Product"(id),
    order_id INT REFERENCES "Order"(id),
    discount DECIMAL(5, 2),
    quantity INT,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES "Product"(id),
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES "Order"(id),
    PRIMARY KEY (product_id, order_id)
);
-- indexes
CREATE INDEX idx_order_product_product_id ON "Order_Product"(product_id);
CREATE INDEX idx_order_product_order_id ON "Order_Product"(order_id);

-- CATEGORY

CREATE TABLE "Category" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    parent INT REFERENCES "Category"(id)
);

-- Product x Category (n X n)

CREATE TABLE "Product_Category" (
    category_id INT REFERENCES "Category"(id),
    product_id INT REFERENCES "Product"(id),
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES "Category"(id),
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES "Product"(id),
    PRIMARY KEY (category_id, product_id)
);
-- indexes
CREATE INDEX idx_product_category_category_id ON "Product_Category"(category_id);
CREATE INDEX idx_product_category_product_id ON "Product_Category"(product_id);