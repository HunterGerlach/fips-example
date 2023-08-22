from flask import Flask
import requests
import os

app = Flask(__name__)

SERVER_URL = os.environ.get('SERVER_URL', 'https://default-server:8443')

@app.route('/')
def connect_to_server():
    try:
        # Disable verification for simplicity to highlight the server-side cipher suite
        response = requests.get(SERVER_URL, verify=False)
        return f'Successfully connected to {SERVER_URL}'
    except Exception as e:
        return f'Failed to connect to {SERVER_URL}. Error: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)