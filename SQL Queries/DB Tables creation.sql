CREATE TABLE manufacturers (
    manufacturer_id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    website VARCHAR(100)
);

CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    material_name VARCHAR(100) NOT NULL,
    manufacturer_id INTEGER REFERENCES manufacturers(manufacturer_id),
    purchase_price NUMERIC(10, 2),
    sell_price NUMERIC(10, 2)
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    phone_number VARCHAR(15)
);

CREATE TABLE mediators (
    mediator_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    phone_number VARCHAR(15),
    company_name VARCHAR(100)
);

CREATE TABLE orders (
	order_id SERIAL PRIMARY KEY,
	customer_id INTEGER REFERENCES customers(customer_id),
	mediator_id INTEGER REFERENCES mediators(mediator_id),
	city VARCHAR(100),
	address VARCHAR(255),
	order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE order_details (
    detail_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    material_id INTEGER NOT NULL REFERENCES materials(material_id) ON DELETE CASCADE,
    quantity NUMERIC(10, 2) NOT NULL CHECK (quantity > 0),
    coverage_area NUMERIC(10, 2) NOT NULL CHECK (coverage_area > 0),
    price_per_sqm NUMERIC(10, 2) NOT NULL CHECK (price_per_sqm > 0),
    description TEXT
);
