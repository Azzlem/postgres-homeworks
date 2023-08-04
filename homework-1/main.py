"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from utils import get_list_from_file

customers_data = "customers_data.csv"
employees_data = "employees_data.csv"
orders_data = "orders_data.csv"

customers_data_list = get_list_from_file(customers_data)
employees_data_list = get_list_from_file(employees_data)
orders_data_list = get_list_from_file(orders_data)


conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="abc",
    password="abc"
)
cur = conn.cursor()
for customer in customers_data_list:
    if customer[0] != "customer_id":
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (
            customer[0],
            customer[1],
            customer[2]
        )
                    )

for employee in employees_data_list:
    if employee[0] != "employee_id":
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (
            employee[0],
            employee[1],
            employee[2],
            employee[3],
            employee[4],
            employee[5]
        )
                    )
for order in orders_data_list:
    if order[0] != "order_id":
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (
            order[0],
            order[1],
            order[2],
            order[3],
            order[4],
        )

                    )

cur.execute("SELECT * FROM orders")

conn.commit()

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
