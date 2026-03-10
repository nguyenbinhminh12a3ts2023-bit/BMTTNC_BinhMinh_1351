class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set()
        matrix = []
        for letter in key:
            if letter not in key_set and letter.isalpha():
                matrix.append(letter)
                key_set.add(letter)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in key_set:
                matrix.append(letter)
                key_set.add(letter)
        
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper().replace(" ", "")
        prepared_text = ""
        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            b = plain_text[i+1] if i+1 < len(plain_text) else "X"
            if a == b:
                prepared_text += a + "X"
                i += 1
            else:
                prepared_text += a + b
                i += 2

        encrypted_text = ""
        for i in range(0, len(prepared_text), 2):
            row1, col1 = self.find_letter_coords(matrix, prepared_text[i])
            row2, col2 = self.find_letter_coords(matrix, prepared_text[i+1])

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            row1, col1 = self.find_letter_coords(matrix, cipher_text[i])
            row2, col2 = self.find_letter_coords(matrix, cipher_text[i+1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return decrypted_text