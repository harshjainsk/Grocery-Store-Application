from datetime import datetime

from sql_connection import get_sql_connection


def insert_order(connection, order):
    cursor = connection.cursor()

    # order_query = "INSERT INTO order (customer_name, total, datetime) VALUES (%s, %s, %s)"

    # order_query = ("INSERT INTO order "
    #                "(customer_name, total, datetime) "
    #                "VALUES (%s, %s, %s)")
    # order_data = (order['customer_name'], order['grand_total'], datetime.now())

    order_query = ("INSERT INTO orders "
                   "(customer_name, grand_total, date_time) "
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], order['datetime'])

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    connection.commit()

    return order_id


if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_order(connection, {
        'customer_name': 'neha',
        'datetime': datetime.now(),
        'grand_total': 500,
        'order_details': [
            {
                'product_id': 2,
                'quantity': 4,
                'total_price': 400
            },
            {
                'product_id': 3,
                'quantity': 2,
                'total_price': 50
            }
        ]
    }))
