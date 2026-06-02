# main.py - Interactive program that uses the CaesarCipher class

from models import CaesarCipher

def show_menu():
    print("\n" + "=" * 40)
    print("      CAESAR CIPHER TOOL")
    print("=" * 40)
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Show current shift value")
    print("4. Change shift value")
    print("5. Exit")
    print("=" * 40)

def encrypt_message(cipher):
    print("\n--- ENCRYPTION MODE ---")
    
    message = input("Enter the message to encrypt: ")
    
    if not message.strip():
        print("Error: Cannot encrypt an empty message!")
        return
    
    encrypted_message = cipher.encrypt(message)
    
    print(f"\nOriginal message: {message}")
    print(f"Shift value used: {cipher.get_shift()}")
    print(f"Encrypted message: {encrypted_message}")
    
    save_choice = input("\nSave encrypted message to file? (y/n): ").lower()
    
    if save_choice == 'y' or save_choice == 'yes':
        with open('encrypted_message.txt', 'w', encoding='utf-8') as file:
            file.write(encrypted_message)
        print("Message saved to 'encrypted_message.txt'")

def decrypt_message(cipher):
    print("\n--- DECRYPTION MODE ---")
    
    print("How would you like to provide the encrypted message?")
    print("1. Type it manually")
    print("2. Read from file (encrypted_message.txt)")
    
    choice = input("Enter 1 or 2: ")
    
    encrypted_message = ""
    
    if choice == '1':
        encrypted_message = input("Enter the encrypted message: ")
        
        if not encrypted_message.strip():
            print("Error: Cannot decrypt an empty message!")
            return
            
    elif choice == '2':
        try:
            with open('encrypted_message.txt', 'r', encoding='utf-8') as file:
                encrypted_message = file.read()
            print("Message loaded from file successfully!")
            
            if not encrypted_message.strip():
                print("Error: The file is empty!")
                return
                
        except FileNotFoundError:
            print("Error: 'encrypted_message.txt' not found!")
            print("Please encrypt a message first or type the message manually.")
            return
            
    else:
        print("Invalid choice! Please enter 1 or 2.")
        return
    
    decrypted_message = cipher.decrypt(encrypted_message)
    
    print(f"\nEncrypted message: {encrypted_message}")
    print(f"Shift value used: {cipher.get_shift()}")
    print(f"Decrypted message: {decrypted_message}")

def show_shift(cipher):
    print(f"\nCurrent shift value: {cipher.get_shift()}")
    print("(Shift must be between 0 and 25, where 0 means no change)")

def change_shift(cipher):
    print("\n--- CHANGE SHIFT VALUE ---")
    print(f"Current shift: {cipher.get_shift()}")
    
    try:
        new_shift = int(input("Enter new shift value (1-25): "))
        
        if 1 <= new_shift <= 25:
            cipher.shift = new_shift
            print(f"Shift successfully changed to {cipher.get_shift()}")
        else:
            print("Error: Shift must be between 1 and 25!")
            
    except ValueError:
        print("Error: Please enter a valid number!")

def main():
    print("\n" + "=" * 50)
    print("WELCOME TO THE CAESAR CIPHER PROGRAM")
    print("=" * 50)
    print("\nWhat is a Caesar Cipher?")
    print("It's a simple encryption method where each letter is shifted")
    print("by a fixed number of positions in the alphabet.")
    print("\nExample with shift=3:")
    print("  'A' becomes 'D'")
    print("  'B' becomes 'E'")
    print("  'Hello' becomes 'Khoor'")
    print("=" * 50)
    
    cipher = CaesarCipher(shift=3)
    print(f"\nCipher created with default shift: {cipher.get_shift()}")
    
    print("\n--- QUICK DEMONSTRATION ---")
    test_message = "Python is fun!"
    encrypted = cipher.encrypt(test_message)
    decrypted = cipher.decrypt(encrypted)
    print(f"Original:  {test_message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    running = True
    
    while running:
        show_menu()
        
        user_choice = input("Enter your choice (1-5): ")
        
        if user_choice == '1':
            encrypt_message(cipher)
        elif user_choice == '2':
            decrypt_message(cipher)
        elif user_choice == '3':
            show_shift(cipher)
        elif user_choice == '4':
            change_shift(cipher)
        elif user_choice == '5':
            print("\nThank you for using Caesar Cipher!")
            print("Goodbye!")
            running = False
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")
        
        if running:
            input("\nPress Enter to continue...")

# if __name__ == "__main__":
main()