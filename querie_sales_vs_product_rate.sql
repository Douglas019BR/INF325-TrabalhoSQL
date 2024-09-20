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