-- Drop tables if they exist
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;

-- Create Categories Table
CREATE TABLE categories (
    code VARCHAR(30) PRIMARY KEY,
    description VARCHAR(300) NOT NULL
);

-- Create Products Table
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(30) UNIQUE NOT NULL,
    name VARCHAR(80) NOT NULL,
    description VARCHAR(600) NOT NULL,
    price INT NOT NULL CHECK (price >= 0),
    stock INT NOT NULL CHECK (stock >= 0),
    category_code VARCHAR(30),
    FOREIGN KEY (category_code) REFERENCES categories(code)
);

-- Create Categories
INSERT INTO categories (code, description) VALUES
    ('BEER', 'Beer and Ales'),
    ('WINE', 'Wine and Sparkling Wine'),
    ('SPIRITS', 'Spirits and Liquors'),
    ('CIDER', 'Cider and Perry'),
    ('LIQUEUR', 'Liqueurs')
;

-- Create Products
INSERT INTO products (code, name, description, price, stock, category_code) VALUES
    ('BEER001', 'Craft IPA', 'Craft IPA - 6 Pack', 15, 200, 'BEER'),
    ('BEER002', 'Pale Ale', 'Pale Ale - 12 Pack', 22, 150, 'BEER'),
    ('WINE001', 'Chardonnay', 'Chardonnay - 750ml', 25, 100, 'WINE'),
    ('WINE002', 'Merlot', 'Merlot - 750ml', 30, 80, 'WINE'),
    ('SPIRITS001', 'Single Malt Scotch', 'Single Malt Scotch - 700ml', 60, 50, 'SPIRITS'),
    ('SPIRITS002', 'Premium Vodka', 'Premium Vodka - 700ml', 45, 75, 'SPIRITS'),
    ('CIDER001', 'Dry Apple Cider', 'Dry Apple Cider - 6 Pack', 18, 130, 'CIDER'),
    ('CIDER002', 'Sweet Pear Cider', 'Sweet Pear Cider - 6 Pack', 20, 100, 'CIDER'),
    ('LIQUEUR001', 'Coffee Liqueur', 'Coffee Liqueur - 500ml', 35, 60, 'LIQUEUR'),
    ('LIQUEUR002', 'Orange Liqueur', 'Orange Liqueur - 500ml', 28, 90, 'LIQUEUR')
;
