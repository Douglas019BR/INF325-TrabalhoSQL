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