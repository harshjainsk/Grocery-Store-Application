import json

from flask import Flask, request, jsonify
import products_dao, order_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()


# routing for get_products

@app.route('/get_products', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)

    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# routing for deleting products

@app.route('/delete_products', methods=['POST'])
def delete_products():
    """
        1 here represents the product_id and once we connect with the frontend
        we need to use the `request.form['product_id']` and replace in the position of 1
    """

    deleted_return_id = products_dao.delete_product(connection, request.form['product_id'])

    response = jsonify({
        'deleted-product-with-id': deleted_return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/add_products', methods=['POST'])
def insert_product():
    """
        json.loads() function converts a valid json string to a python
        dictionary. Here we are using `request.form['data']` to get data from frontend.
        While using POSTMAN we need to go to Body and in body we need to go to form and
        there we need to give the name of variable in key and value we need to parse. In
        the above the key we are passing is `data` and the values we need to insert in
        database is given in the values column.
    """

    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)

    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/insert_order', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = order_dao.insert_order(connection, request_payload)

    response = jsonify({
        "order_id": order_id
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting flask server for Grocery Store Management')
    app.run(port=5000)




