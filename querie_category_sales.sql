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