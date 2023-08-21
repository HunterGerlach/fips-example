from flask import Flask
import hashlib

app = Flask(__name__)

@app.route('/')
def sha256_hash():
    hash_object = hashlib.sha256(b'compliant with FIPS')
    return f'SHA-256 Hash: {hash_object.hexdigest()}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
