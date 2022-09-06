from flask import Flask, request, jsonify
import products_dao
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

    deleted_return_id = products_dao.delete_product(connection, 1)

    response = jsonify({
        'deleted-product-with-id': deleted_return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting flask server for Grocery Store Management')
    app.run(port=5000)
