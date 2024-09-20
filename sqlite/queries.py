import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# 1. Produto mais vendido por categoria (10 mais vendidos)
def product_sales_by_category():
    query = '''
    SELECT 
        c.name AS category_name,
        p.name AS product_name,
        SUM(op.quantity) AS total_quantity_sold
    FROM 
        "Order_Product" op
    JOIN 
        "Product" p ON op.product_id = p.id
    JOIN 
        "Product_Category" pc ON p.id = pc.product_id
    JOIN 
        "Category" c ON pc.category_id = c.id
    GROUP BY 
        c.name, p.name
    ORDER BY 
        total_quantity_sold DESC
    LIMIT 10;  -- Limitar aos 10 mais vendidos
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
    plot_product_sales_by_category(df)

def plot_product_sales_by_category(df):
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='category_name', y='total_quantity_sold', hue='product_name')
    plt.title('Top 10 Produtos Mais Vendidos por Categoria')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# 2. Produto mais vendido por região e por gênero (10 mais vendidos)
def product_sales_by_region_and_gender():
    query = '''
    SELECT 
        a.city AS region,
        u.gender AS gender,
        p.name AS product_name,
        SUM(op.quantity) AS total_quantity_sold
    FROM 
        "Order_Product" op
    JOIN 
        "Order" o ON op.order_id = o.id
    JOIN 
        "Customer" c ON o.customer_id = c.id
    JOIN 
        "User" u ON c.user_id = u.id
    JOIN 
        "Address" a ON o.customer_address_id = a.id
    JOIN 
        "Product" p ON op.product_id = p.id
    GROUP BY 
        a.city, u.gender, p.name
    ORDER BY 
        total_quantity_sold DESC
    LIMIT 10;  -- Limitar aos 10 mais vendidos
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
    plot_product_sales_by_region_and_gender(df)

def plot_product_sales_by_region_and_gender(df):
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='region', y='total_quantity_sold', hue='gender', style='product_name', markers=True)
    plt.title('Top 10 Produtos Mais Vendidos por Região e Gênero')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# 3. Categorias x Vendas
def category_sales():
    query = '''
    SELECT 
        c.name AS category_name,
        COUNT(op.product_id) AS total_sales
    FROM 
        "Order_Product" op
    JOIN 
        "Product" p ON op.product_id = p.id
    JOIN 
        "Product_Category" pc ON p.id = pc.product_id
    JOIN 
        "Category" c ON pc.category_id = c.id
    GROUP BY 
        c.name
    ORDER BY 
        total_sales DESC;
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
    plot_category_sales(df)

def plot_category_sales(df):
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='category_name', y='total_sales')
    plt.title('Categorias x Vendas')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# 4. Vendas não finalizadas x Produtos (com espaçamento maior no eixo x)
def uncompleted_sales_by_product():
    query = '''
    SELECT 
        p.name AS product_name,
        COUNT(o.id) AS uncompleted_orders
    FROM 
        "Order" o
    JOIN 
        "Order_Product" op ON o.id = op.order_id
    JOIN 
        "Product" p ON op.product_id = p.id
    WHERE 
        o.status != 'payed'
    GROUP BY 
        p.name
    ORDER BY 
        uncompleted_orders DESC;
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
    plot_uncompleted_sales(df)

def plot_uncompleted_sales(df):
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='product_name', y='uncompleted_orders')
    plt.title('Vendas Não Finalizadas por Produto')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# 5. Número de vendas x Rate do Produto
def sales_vs_product_rate():
    query = '''
    SELECT 
        p.rate,
        COUNT(op.product_id) AS total_sales
    FROM 
        "Order_Product" op
    JOIN 
        "Product" p ON op.product_id = p.id
    GROUP BY 
        p.rate
    ORDER BY 
        p.rate;
    '''
    df = pd.read_sql_query(query, conn)
    print(df)
    plot_sales_vs_product_rate(df)

def plot_sales_vs_product_rate(df):
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x='rate', y='total_sales', marker='o')
    plt.title('Número de Vendas por Avaliação do Produto')
    plt.tight_layout()
    plt.show()

# Função principal para executar todas as queries e exibir os gráficos
def main():
    print("1. Produto mais vendido por categoria (Top 10):")
    product_sales_by_category()
    
    print("\n2. Produto mais vendido por região e por gênero (Top 10):")
    product_sales_by_region_and_gender()
    
    print("\n3. Categorias x Vendas:")
    category_sales()
    
    print("\n4. Vendas não finalizadas x Produtos:")
    uncompleted_sales_by_product()
    
    print("\n5. Número de vendas x Rate do Produto:")
    sales_vs_product_rate()

# Executar o script
if __name__ == "__main__":
    main()

# Fechar a conexão com o banco de dados
conn.close()
