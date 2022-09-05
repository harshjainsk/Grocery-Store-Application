from sql_connection import get_sql_connection


def get_all_products(connection):

    cursor = connection.cursor()

    query = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM " \
            "products INNER JOIN uom ON products.uom_id=uom.uom_id "

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    connection.close()
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['name'], product['um_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()

    print(insert_new_product(connection, {
        'name': 'potatoes',
        'um_id': '1',
        'price_per_unit': 10
    }))

    print(get_all_products(connection))
