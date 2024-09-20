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
    LIMIT 10;