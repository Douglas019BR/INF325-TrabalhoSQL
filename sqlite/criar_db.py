import sqlite3

# Conectar ao banco de dados (ou criar um novo se não existir)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Função para criar as tabelas
def create_tables():
    # Criando tabela Order
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Order" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        customer_address_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT CHECK (status IN ('pending', 'payed', 'waiting', 'canceled')),
        FOREIGN KEY (customer_id) REFERENCES "Customer"(id),
        FOREIGN KEY (customer_address_id) REFERENCES "Address"(id)
    );
    ''')

    # Criando índices para Order
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_customer_id ON "Order"(customer_id);')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_customer_address_id ON "Order"(customer_address_id);')

    # Criando tabela User
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "User" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        birth_date DATE,
        gender TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # Criando tabela Seller
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Seller" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document TEXT NOT NULL,
        user_id INTEGER,
        description TEXT,
        rate REAL,
        FOREIGN KEY (user_id) REFERENCES "User"(id)
    );
    ''')

    # Criando índices para Seller
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_seller_user_id ON "Seller"(user_id);')

    # Criando tabela Customer
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Customer" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES "User"(id)
    );
    ''')

    # Criando índices para Customer
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_customer_user_id ON "Customer"(user_id);')

    # Criando tabela Address
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Address" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        country TEXT,
        street TEXT,
        number TEXT,
        zip_code TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP
    );
    ''')

    # Criando tabela Address_User
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Address_User" (
        address_id INTEGER,
        user_id INTEGER,
        PRIMARY KEY (address_id, user_id),
        FOREIGN KEY (address_id) REFERENCES "Address"(id),
        FOREIGN KEY (user_id) REFERENCES "User"(id)
    );
    ''')

    # Criando índices para Address_User
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_address_user_address_id ON "Address_User"(address_id);')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_address_user_user_id ON "Address_User"(user_id);')

    # Criando tabela Order_User
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Order_User" (
        order_id INTEGER,
        user_id INTEGER,
        PRIMARY KEY (order_id, user_id),
        FOREIGN KEY (order_id) REFERENCES "Order"(id),
        FOREIGN KEY (user_id) REFERENCES "User"(id)
    );
    ''')

    # Criando índices para Order_User
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_user_order_id ON "Order_User"(order_id);')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_user_user_id ON "Order_User"(user_id);')

    # Criando tabela Product
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Product" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        seller_id INTEGER,
        image TEXT,
        thumbnail TEXT,
        description TEXT,
        value REAL,
        amount INTEGER,
        status TEXT,
        brand TEXT,
        rate REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (seller_id) REFERENCES "Seller"(id)
    );
    ''')

    # Criando índices para Product
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_seller_id ON "Product"(seller_id);')

    # Criando tabela Order_Product
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Order_Product" (
        product_id INTEGER,
        order_id INTEGER,
        discount REAL,
        quantity INTEGER,
        PRIMARY KEY (product_id, order_id),
        FOREIGN KEY (product_id) REFERENCES "Product"(id),
        FOREIGN KEY (order_id) REFERENCES "Order"(id)
    );
    ''')

    # Criando índices para Order_Product
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_product_product_id ON "Order_Product"(product_id);')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_order_product_order_id ON "Order_Product"(order_id);')

    # Criando tabela Category
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Category" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        parent INTEGER,
        FOREIGN KEY (parent) REFERENCES "Category"(id)
    );
    ''')

    # Criando tabela Product_Category
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Product_Category" (
        category_id INTEGER,
        product_id INTEGER,
        PRIMARY KEY (category_id, product_id),
        FOREIGN KEY (category_id) REFERENCES "Category"(id),
        FOREIGN KEY (product_id) REFERENCES "Product"(id)
    );
    ''')

    # Criando índices para Product_Category
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_category_category_id ON "Product_Category"(category_id);')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_category_product_id ON "Product_Category"(product_id);')

    # Commitando as mudanças
    conn.commit()

# Função para popular o banco de dados com o arquivo SQL
def populate_database(sql_file):
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)
    conn.commit()

# Executa a função para criar as tabelas
create_tables()

# Chamada para popular o banco de dados com o arquivo dados.sql
populate_database('dados1.sql')
print("Arquivo dados1.sql inserido com sucesso!")
populate_database('dados2.sql')
print("Arquivo dados2.sql inserido com sucesso!")

# Fechar a conexão com o banco de dados
conn.close()

print("Banco de dados criado e populado com sucesso!")
