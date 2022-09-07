from datetime import datetime

from sql_connection import get_sql_connection


def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = ("INSERT INTO orders "
                   "(customer_name, grand_total, date_time) "
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], order['datetime'])

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    # fetching order_details and adding the entries to database

    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price) "
                           "VALUES (%s, %s, %s, %s)"
                           )

    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])

    cursor.executemany(order_details_query, order_details_data)
    connection.commit()

    return order_id


def get_all_orders(connection):
    cursor = connection.cursor()

    query = ("SELECT * FROM orders")
    cursor.execute(query)

    response = []

    for (order_id, customer_name, grand_total, date_time) in cursor:
        response.append({
            "order_id": order_id,
            "customer_name": customer_name,
            "grand_total": grand_total,
            "date_time": date_time
        })

    return response


def get_order_details(connection, order_id):

    cursor = connection.cursor()

    query = ("SELECT * FROM order_details WHERE order_id = %s")

    order_id = [order_id]
    cursor.execute(query, order_id)

    response = []

    for (order_id, product_id, quantity, total_price) in cursor:
        response.append({
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price
        })

    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(insert_order(connection, {
    #     'customer_name': 'Hulk',
    #     'datetime': datetime.now(),
    #     'grand_total': 859,
    #     'order_details': [
    #         {
    #             'product_id': 5,
    #             'quantity': 3,
    #             'total_price': 90
    #         },
    #         {
    #             'product_id': 3,
    #             'quantity': 2,
    #             'total_price': 50
    #         }
    #     ]
    # }))

    # print(get_all_orders(connection))

    print(get_order_details(connection, 16))