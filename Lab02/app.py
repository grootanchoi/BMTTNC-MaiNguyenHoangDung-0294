from flask import Flask, render_template, request, json, jsonify
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

# ==========================================
# ROUTER ROUTES FOR DISPLAYING UI PAGES
# ==========================================
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')


# ==========================================
# 1. CAESAR CIPHER PROCESSORS
# ==========================================
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template('caesar.html', encrypted_text=encrypted_text, original_plain_text=text, key_plain=key)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return render_template('caesar.html', decrypted_text=decrypted_text, original_cipher_text=text, key_cipher=key)


# ==========================================
# 2. PLAYFAIR CIPHER PROCESSORS
# ==========================================
@app.route("/playfair/encrypt", methods=['POST'])
def web_playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
    return render_template('playfair.html', encrypted_text=encrypted_text, original_plain_text=text, key_plain=key)

@app.route("/playfair/decrypt", methods=['POST'])
def web_playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
    return render_template('playfair.html', decrypted_text=decrypted_text, original_cipher_text=text, key_cipher=key)


# ==========================================
# 3. RAIL FENCE CIPHER PROCESSORS
# ==========================================
@app.route("/railfence/encrypt", methods=['POST'])
def web_railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence_cipher = RailFenceCipher()
    encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
    return render_template('railfence.html', encrypted_text=encrypted_text, original_plain_text=text, key_plain=key)

@app.route("/railfence/decrypt", methods=['POST'])
def web_railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence_cipher = RailFenceCipher()
    decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
    return render_template('railfence.html', decrypted_text=decrypted_text, original_cipher_text=text, key_cipher=key)


# ==========================================
# 4. TRANSPOSITION CIPHER PROCESSORS
# ==========================================
@app.route("/transposition/encrypt", methods=['POST'])
def web_transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transposition_cipher = TranspositionCipher()
    encrypted_text = transposition_cipher.encrypt(text, key)
    return render_template('transposition.html', encrypted_text=encrypted_text, original_plain_text=text, key_plain=key)

@app.route("/transposition/decrypt", methods=['POST'])
def web_transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transposition_cipher = TranspositionCipher()
    decrypted_text = transposition_cipher.decrypt(text, key)
    return render_template('transposition.html', decrypted_text=decrypted_text, original_cipher_text=text, key_cipher=key)


# ==========================================
# 5. VIGENÈRE CIPHER PROCESSORS
# ==========================================
@app.route("/vigenere/encrypt", methods=['POST'])
def web_vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere_cipher = VigenereCipher()
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key) 
    return render_template('vigenere.html', encrypted_text=encrypted_text, original_plain_text=text, key_plain=key)

@app.route("/vigenere/decrypt", methods=['POST'])
def web_vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere_cipher = VigenereCipher()
    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key) 
    return render_template('vigenere.html', decrypted_text=decrypted_text, original_cipher_text=text, key_cipher=key)

# ==========================================
# EXISTING API ENDPOINTS (FOR POSTMAN)
# ==========================================
@app.route('/api/transposition/encrypt', methods=['POST'])
def api_transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    transposition_cipher = TranspositionCipher()
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def api_transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    transposition_cipher = TranspositionCipher()
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)