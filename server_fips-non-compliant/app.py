from flask import Flask
from OpenSSL import crypto
import ssl
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from the non-FIPS compliant server!'

def generate_self_signed_cert():
    if not os.path.exists('cert.pem') or not os.path.exists('key.pem'):
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA, 4096)

        cert = crypto.X509()
        cert.get_subject().CN = "localhost"
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(31536000)  # Valid for one year
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(key)
        cert.sign(key, 'sha256')

        with open('cert.pem', 'wb') as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

        with open('key.pem', 'wb') as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

if __name__ == '__main__':
    generate_self_signed_cert()

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.set_ciphers('AES128-SHA') # non-FIPS compliant cipher; you may need to change this for your system
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

    app.run(host='0.0.0.0', port=8443, ssl_context=context)
