import psycopg2
from api.models import User, Order
from pprint import pprint
import os


class DatabaseConnection:
    """Class for all database operations."""

    def __init__(self):

        try:
            self.connection = psycopg2.connect(
                # dbname='sendit',
                # user='sendit',
                # host='localhost',
                # password='beka',
                # port=5432 
                dbname='travis_ci_test'
            )
            
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            create_order_table = """CREATE TABLE IF NOT EXISTS orders(
            id SERIAL NOT NULL PRIMARY KEY,
            destination TEXT NOT NULL,
            price FLOAT NOT NULL,
            weight FLOAT NOT NULL,
            Pickup_location TEXT NOT NULL, 
            name TEXT NOT NULL, status TEXT NOT NULL,
            present_location TEXT NOT NULL,
            date TIMESTAMP
                );"""
            create_user_table = """CREATE TABLE IF NOT EXISTS users(
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            userId SERIAL NOT NULL PRIMARY KEY,
            admin VARCHAR(50) DEFAULT 'FALSE'
                );"""
            self.cursor.execute(create_order_table)
            self.cursor.execute(create_user_table)
        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)

    def insert_order(self, *args):
        destination = args[0]
        price = args[1]
        weight = args[2]
        Pickup_location = args[3]
        name = args[4]
        status = args[5]
        present_location = args[6]

        """Method for adding a new parcel to orders"""
        insert_order = """INSERT INTO orders(
            destination,
            price,
            weight,
            Pickup_location,
            name, status,
            present_location
            ) VALUES('{}', '{}', '{}', '{}','{}', '{}', '{}')""".format(
            destination,
            price,
            weight,
            Pickup_location,
            name,
            status,
            present_location
        )
        pprint(insert_order)
        self.cursor.execute(insert_order)

    def insert_user(self, name, email, password):
        """Method for adding a new user to users"""
        insert_user = """INSERT INTO users(
            name,
            email,
            password
            ) VALUES('{}', '{}', '{}')""".format(name, email, password)
        pprint(insert_user)
        self.cursor.execute(insert_user)

    def create_admin(self, userId, admin):
        "Method to create an admin"
        create_admin = """UPDATE  users SET admin='TRUE' WHERE userId='{}'""".format(admin, userId)
        pprint(create_admin)
        self.cursor.execute(create_admin)

    def update_destination(self, id, destination):
        query = """UPDATE orders SET destination='{}' WHERE userId='{}'""".format(
            destination,
            id
            )
        pprint(query)
        self.cursor.execute(query)

    def update_present_location(self, id, present_location):
        """Method to change a parcels current location."""
        query = """UPDATE orders SET present_location='{}' WHERE id='{}'""".format(
            present_location, id)
        pprint(query)
        self.cursor.execute(query)

    def login(self, name):
        """Method to login an existing user"""
        query = "SELECT * FROM users WHERE name='{}'".format(name)
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def check_name(self, name):
        """Method to find a name of a user in a database"""
        query = "SELECT * FROM users WHERE name='{}'".format(name)
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def check_email(self, email):
        query = "SELECT * FROM users WHERE email='{}'".format(email)
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def user(self, name):
        """Returning a user id from database"""
        query = "SELECT * FROM users WHERE name='{}'".format(name)
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def fetch_all_orders(self):
        """Method to return all existing parcels"""
        query_all = "SELECT * FROM orders"
        pprint(query_all)
        self.cursor.execute(query_all)
        orders = self.cursor.fetchall()
        return orders

    def fetch_order(self, id):
        """Method to return a given parcel by its id."""
        query_one = "SELECT * FROM orders WHERE id='{}'".format(id)
        pprint(query_one)
        self.cursor.execute(query_one)
        order = self.cursor.fetchone()
        return order

    def fetch_user(self, id):
        """Method to return a given parcel by its id."""
        query_one = "SELECT * FROM users WHERE id='{}'".format(id)
        pprint(query_one)
        self.cursor.execute(query_one)
        user = self.cursor.fetchone()
        return user

    def update_status(self, id, status):
        query = "UPDATE orders SET status='{}' WHERE id='{}'".format(status, id)
        pprint(query)
        self.cursor.execute(query)

    def drop_tables(self):
        drop = "DROP TABLE orders, users"
        pprint(drop)
        self.cursor.execute(drop)

if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.create_admin()  
# self.connection = psycopg2.connect(
# dbname = os.environ["DATABASE_URL"],
# dbname='travis_ci_test'                       