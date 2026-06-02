==========================================
SIMPLIFIED CAESAR CIPHER PROJECT
==========================================

WHAT IS THIS PROJECT?
---------------------
This is a simple encryption/decryption program that implements the 
Caesar cipher - one of the oldest known encryption techniques.

HOW THE CAESAR CIPHER WORKS:
---------------------------
Each letter in the message is shifted by a fixed number of positions:
- With shift=3: A→D, B→E, C→F, ..., Z→C (wraps around)
- Non-letters (spaces, numbers, punctuation) remain unchanged
- Letter case is preserved (uppercase stays uppercase)

EXAMPLE:
--------
Shift=3:
Original:  "Hello World!"
Encrypted: "Khoor Zruog!"
Decrypted: "Hello World!"

FILE DESCRIPTIONS:
-----------------
1. models.py     - Contains the CaesarCipher class with encrypt/decrypt methods
2. main.py       - The main program that uses the class with a menu interface
3. requirements.txt - Lists dependencies (none needed)
4. readme.txt    - This documentation file

HOW TO RUN THE PROGRAM:
----------------------
1. Make sure Python 3.6+ is installed on your computer
2. Save all files in the same folder
3. Open terminal/command prompt in that folder
4. Run: python main.py
5. Follow the on-screen menu

MENU OPTIONS EXPLAINED:
----------------------
Option 1 - ENCRYPT: Type a message and get the encrypted version
Option 2 - DECRYPT: Type an encrypted message or load from file
Option 3 - SHOW SHIFT: Display the current shift value
Option 4 - CHANGE SHIFT: Set a new shift value (1-25)
Option 5 - EXIT: Close the program

DETAILED EXAMPLES:
-----------------
Example 1: Encrypting
> Choose option 1
> Enter: "cat"
> Shift=3
> Output: "fdw"

Example 2: Decrypting
> Choose option 2
> Enter: "fdw"
> Shift=3
> Output: "cat"

Example 3: With spaces and punctuation
> Enter: "Hello, World!"
> Output: "Khoor, Zruog!"

Example 4: Changing shift
> Option 4 → Enter 5
> Now encrypt "cat" → "hfy"

WHAT HAPPENS WHEN YOU RUN THE CODE:
----------------------------------
1. main.py imports the CaesarCipher class from models.py
2. Creates a cipher object with shift=3
3. Shows a demo to illustrate how it works
4. Enters a loop that keeps showing the menu
5. Waits for your input and responds accordingly
6. Continues until you choose Exit

CLASS METHODS (from models.py):
-----------------------------
__init__(self, shift)  - Creates a new cipher with given shift
encrypt(self, text)    - Encrypts a message
decrypt(self, text)    - Decrypts a message
get_shift(self)        - Returns current shift value

KEY PROGRAMMING CONCEPTS DEMONSTRATED:
-------------------------------------
1. Object-Oriented Programming (classes, objects, methods, self)
2. File I/O (reading from and writing to files)
3. Loops (while loop for menu)
4. Conditionals (if/elif/else for menu choices)
5. String manipulation (.lower(), .index(), .join())
6. Exception handling (try/except for user input)
7. Lists (storing characters during encryption/decryption)
8. Modulo arithmetic (wrapping around the alphabet)

TROUBLESHOOTING:
---------------
Problem: "ModuleNotFoundError: No module named 'models'"
Solution: Make sure both files are in the same folder

Problem: "FileNotFoundError" when decrypting from file
Solution: Encrypt a message first to create the file, or type the message manually

Problem: Getting wrong decryption result
Solution: Make sure the shift value is the same as when you encrypted

Problem: "ValueError" when entering shift
Solution: Enter only numbers (1-25), not letters

LIMITATIONS:
-----------
- Only works with English alphabet (A-Z, a-z)
- Does not encrypt numbers or special characters
- Shift 0 would do nothing to the message
- Shift values >25 are reduced using modulo

EXTENDING THE PROJECT:
--------------------
Ideas for improvement:
- Add option to encrypt/decrypt entire files
- Add brute force option to try all 25 shifts
- Add support for numbers and symbols
- Create a graphical user interface (GUI)
- Save encryption history

GITHUB REPOSITORY:
-----------------
[Insert your GitHub repository link here]

CREATED FOR:
------------
Python Course Project - May 2026