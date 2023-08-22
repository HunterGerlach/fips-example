from flask import Flask
import hashlib

app = Flask(__name__)

@app.route('/')
def md5_hash():
    hash_object = hashlib.md5(b'non-compliant with FIPS')
    return f'MD5 Hash: {hash_object.hexdigest()}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
