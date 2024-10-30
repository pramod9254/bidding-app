import json

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

connection = create_connection("localhost", "root", "password", "biddingapp")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()

        if cursor.rowcount == 1:
            print("Query executed successfully")
            return True
        else:
            print("Insert may have failed.")
            return False
        
    except Error as e:
        print(f"The error '{e}' occurred")
        return False

def fetch_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
       
        field_names = [i[0] for i in cursor.description]
        response = [dict(zip(field_names, row)) for row in result]
        return response
    except Error as e:
        print(f"The error '{e}' occurred")

# Example usage
select_users_query = "SELECT * from users"
users2 = fetch_query(connection, select_users_query)

# print('users---',users2)
# if users2 is not None:
for usr in users2:
    print(usr)


class DBActions:
    def getUserByUsername(self, username):
        select_users_query = f"SELECT * from users WHERE username = '{username}'"
        user = fetch_query(connection, select_users_query)
        return user
    
    def login(self, username, password):
        select_users_query = f"SELECT * from users WHERE username = '{username}' AND password = '{password}'"
        user = fetch_query(connection, select_users_query)
        return user
    
    def getUsers(self):
        select_users_query = "SELECT * from users"
        users = fetch_query(connection, select_users_query)
        return users
    
    def create_user(self, user):
        print('user---',user)
        insert_user_query = f"INSERT INTO users (name, username, password, is_seller) VALUES ('{user['name']}', '{user['username']}', '{user['password']}', {user['is_seller']})"
        result = execute_query(connection, insert_user_query)
        print('result---',result)
        return result

    def getContract(self, user_id):
        print('user_id---',user_id)
        select_contracts_query = f"""select contracts.id as contract_id, selleruser.name as seller, 
        buyeruser.name as buyer, bid.item, bid.description, bid.quantity, bid.amount, 
        bid.date_created as bid_date_created, date_signed, CASE contracts.status when 1 then 'Signed' else contracts.status end as contract_status 
        from contracts join users selleruser on contracts.seller = selleruser.id
        join users buyeruser on buyeruser.id = contracts.buyer 
        join bids bid on bid.id = contracts.bid_id WHERE buyer = {user_id} OR seller = {user_id}"""
        contracts = fetch_query(connection, select_contracts_query)
        print('contracts---',contracts)
        return contracts
    
    def createContract(self, contract):
        print('contract---',contract)
        insert_query = f"INSERT INTO contracts (seller, buyer, bid_id, date_created, date_signed, status) VALUES ( {contract['seller']}, {contract['buyer']}, {contract['bid_id']}, '{contract['date_created']}', '{contract['date_signed']}', 1)"
        print('insert_query---',insert_query)
        result = execute_query(connection, insert_query)
        print('result---',result)
        return result
    
    def getMyBids(self, user_id):
        select_bids_query = f"SELECT bids.id, users.name as seller, initiator, item, description, quantity, amount, date_created, date_closed, CASE bids.status when 1 then 'Open' when 2 then 'Closed' else bids.status end as status from bids join users on users.id = bids.initiator WHERE initiator = {user_id}"
        bids = fetch_query(connection, select_bids_query)
        return bids
    
    def getAllBids(self, status):
        select_bids_query = f"SELECT bids.id, users.name as seller, initiator, item, description, quantity, amount, date_created, date_closed, CASE bids.status when 1 then 'Open' when 2 then 'Closed' else bids.status end as status from bids join users on users.id = bids.initiator where bids.status = {status}"
        bids = fetch_query(connection, select_bids_query)
        return bids
    
    def createBid(self, bid):
        print('bid---',bid)
        insert_query = f"INSERT INTO bids (initiator, item, description, quantity, amount, date_created, date_closed, status) VALUES ( {bid['initiator']}, '{bid['item']}', '{bid['description']}', {bid['quantity']}, {bid['amount']}, '{bid['date_created']}', '{bid['date_closed']}', 1)"
        print('insert_query---',insert_query)
        result = execute_query(connection, insert_query)
        print('result---',result)
        return result
    
    def updateBidStatus(self, bid_id, status):
        update_query = f"UPDATE bids SET status = {status} WHERE id = {bid_id}"
        bids = execute_query(connection, update_query)
        return bids

