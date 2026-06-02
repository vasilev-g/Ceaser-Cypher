# models.py - Simple Caesar Cipher class

class CaesarCipher:
    
    def __init__(self, shift=3):
        self.shift = shift % 26
        self.alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def encrypt(self, text):
        encrypted_chars = []
        
        for char in text:
            if char.islower():
                original_index = self.alphabet_lower.index(char)
                new_index = (original_index + self.shift) % 26
                encrypted_chars.append(self.alphabet_lower[new_index])
            elif char.isupper():
                original_index = self.alphabet_upper.index(char)
                new_index = (original_index + self.shift) % 26
                encrypted_chars.append(self.alphabet_upper[new_index])
            else:
                encrypted_chars.append(char)
        
        return ''.join(encrypted_chars)
    
    def decrypt(self, text):
        decrypted_chars = []
        
        for char in text:
            if char.islower():
                original_index = self.alphabet_lower.index(char)
                new_index = (original_index - self.shift) % 26
                decrypted_chars.append(self.alphabet_lower[new_index])
            elif char.isupper():
                original_index = self.alphabet_upper.index(char)
                new_index = (original_index - self.shift) % 26
                decrypted_chars.append(self.alphabet_upper[new_index])
            else:
                decrypted_chars.append(char)
        
        return ''.join(decrypted_chars)
    
    def get_shift(self):
        return self.shift