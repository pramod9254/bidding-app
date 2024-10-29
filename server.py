import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# MySQL Connection Setup
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'test_db'
}

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Respond with a 200 status code
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Connect to MySQL database
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor(dictionary=True)
            
            # Execute SQL query
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            
            # Send data as JSON
            self.wfile.write(bytes(json.dumps(rows), "utf8"))
            
        except mysql.connector.Error as err:
            self.send_error(500, f"MySQL Error: {str(err)}")
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Setup the server
def run(server_class=HTTPServer, handler_class=MyServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
