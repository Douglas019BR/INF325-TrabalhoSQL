import random

orders_product_gerados = set()

# Função para gerar 1000 pedidos e pedidos_produtos em SQL sem duplicar (product_id, order_id)
def generate_orders_sql(num_orders=1000):
    orders_sql = ""
    order_products_sql = ""
    
    # Definindo faixas de IDs existentes para customer_id, customer_address_id e product_id
    customer_ids = range(1, 51)  # Supondo 50 clientes já existentes
    address_ids = range(1, 51)  # Supondo 50 endereços já existentes
    product_ids = range(1, 51)  # Supondo 50 produtos já existentes
    status_options = ['pending', 'payed', 'waiting', 'canceled']
    
    order_id = 0
    while num_orders:
        # Gerar uma ordem
        customer_id = random.choice(customer_ids)
        customer_address_id = random.choice(address_ids)
        status = random.choice(status_options)
        
        orders_sql += f"INSERT INTO \"Order\" (customer_id, customer_address_id, status) " \
                      f"VALUES ({customer_id}, {customer_address_id}, '{status}');\n"
        
        # Gerar 1 a 5 produtos únicos para cada pedido
        num_products = random.randint(1, 5)
        selected_products = random.sample(product_ids, num_products)  # Garante produtos únicos por pedido
        for product_id in selected_products:
            quantity = random.randint(1, 10)
            discount = round(random.uniform(0, 50), 2)

            if (product_id, order_id) in orders_product_gerados:
                continue
            
            order_products_sql += f"INSERT INTO \"Order_Product\" (product_id, order_id, discount, quantity) " \
                                  f"VALUES ({product_id}, {order_id}, {discount}, {quantity});\n"

        num_orders -= 1
        order_id += 1
    
    return orders_sql, order_products_sql

# Gerar os dados de orders e order_products
orders_sql, order_products_sql = generate_orders_sql(1000)

# Salvar em um arquivo .sql
with open("dados2.sql", "w") as f:
    f.write("-- Inserindo 1000 ordens\n")
    f.write(orders_sql)
    f.write("\n-- Inserindo order_products relacionados\n")
    f.write(order_products_sql)
