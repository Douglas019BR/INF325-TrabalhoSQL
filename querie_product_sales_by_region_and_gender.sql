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
    LIMIT 10;