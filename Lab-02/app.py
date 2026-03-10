from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt_route():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere_obj = VigenereCipher()
    encrypted_text = vigenere_obj.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt_route():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere_obj = VigenereCipher()
    decrypted_text = vigenere_obj.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt_route():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    obj = RailFenceCipher()
    res = obj.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {res}"

@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt_route():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    obj = RailFenceCipher()
    res = obj.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {res}"

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/api/playfair/creatematrix", methods=['POST'])
def api_creatematrix():
    data = request.get_json()
    key = data.get('key')
    obj = PlayfairCipher()
    matrix = obj.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": matrix})

@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt_route():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    obj = PlayfairCipher()
    matrix = obj.create_playfair_matrix(key)
    res = obj.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {res}"

@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt_route():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    obj = PlayfairCipher()
    matrix = obj.create_playfair_matrix(key)
    res = obj.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {res}"

@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition_encrypt", methods=['POST'])
def transposition_encrypt_route():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    obj = TranspositionCipher()
    res = obj.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {res}"

@app.route("/transposition_decrypt", methods=['POST'])
def transposition_decrypt_route():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    obj = TranspositionCipher()
    res = obj.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {res}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)