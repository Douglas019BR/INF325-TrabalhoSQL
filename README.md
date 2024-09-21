
# INF325 - E-commerce Database Case Study

This repository contains the files and resources used in the **INF325 Group 7** academic project for the Database course in the postgraduate program at the State University of Campinas (UNICAMP). It focuses on the implementation of a relational database for an Order history of an e-commerce platform. The study explores the application of ACID principles (Atomicity, Consistency, Isolation, Durability) to manage and analyze data in an e-commerce environment.

## Project Overview

The project demonstrates the creation of representative tables for an e-commerce system, such as **Products**, **Sellers**, **Customers**, **Address** and **Orders**, as well as the relationships between them. Queries were performed to extract relevant information and generate insights into sales behavior. This repository includes SQL scripts, Docker configuration, and Python scripts to automate and visualize queries.

## Authors

- [Douglas Sermarini](https://github.com/Douglas019BR)
- [Gabriel Cesário](https://github.com/gcesario203)
- [Joseíto Júnior](https://github.com/JoseitoOliveira)
- [Stephenson Oliveira](https://github.com/stephensonsn)
- [Vitor Gomes](https://github.com/vitorgomes)

## Technologies Used

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![DBeaver](https://img.shields.io/badge/DBeaver-372923?style=for-the-badge&logo=dbeaver&logoColor=white)](https://dbeaver.io/)

## Project Structure

The repository is organized as follows:

```
├── docker-compose.yml
├── populate.sql
├── querie_category_sales.sql
├── querie_def_uncompleted_sales_by_product.sql
├── querie_product_sales_by_category.sql
├── querie_product_sales_by_region_and_gender.sql
├── querie_sales_vs_product_rate.sql
├── README.md
├── sqlite
│   ├── category_sales.png
│   ├── criar_db.py
│   ├── dados1.sql
│   ├── dados2.sql
│   ├── ecommerce.db
│   ├── gerar_dados.py
│   ├── product_sales_by_category.png
│   ├── product_sales_by_region_and_gender.png
│   ├── queries.py
│   ├── requirements.txt
│   ├── sales_vs_product_rate.png
│   └── uncompleted_sales_by_product.png
├── tables.sql
└── uml_image.jpeg
```

## How to Set Up

To run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Douglas019BR/INF325-TrabalhoSQL.git
   ```

2. Start the PostgreSQL container using Docker:
   ```bash
   cd INF325-TrabalhoSQL
   docker-compose up -d postgres
   ```

3. Create the tables:
   ```bash
   psql -h localhost -U postgres -d engsoft_unicamp -f tables.sql
   ```

4. Populate the database:
   ```bash
   psql -h localhost -U postgres -d engsoft_unicamp -f populate.sql
   ```

5. Execute queries:
   - All files starting with `querie_` are example queries. You can run these queries on the terminal or through a GUI tool, like DBeaver.

6. In the [`sqlite`](./sqlite) directory, you will find the same interaction with the database but using SQLite instead of PostgreSQL. This folder contains Python scripts to create, populate, run queries, and generate visual graphs from these queries. To run this, you need to create a Python virtual environment (Python 3.11 is recommended) and install the requirements found in [`sqlite/requirements.txt`](./sqlite/requirements.txt):

   ```bash
   pip install -r sqlite/requirements.txt
   ```

## Contributions

Feel free to submit issues or pull requests if you would like to contribute or improve the project.

## License

This project is licensed under the MIT License.