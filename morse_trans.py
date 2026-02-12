# Morse code alphabet dictionary

alphabet = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '`': '.----.',
    '~': '.-.-', '[': '-.--.', ']': '-.--.-', '{': '-.--.', '}': '-.--.-',
    '\\': '-..-.', '|': '.-..-.', '<': '.-.-.', '>': '-...-', '^': '..--.',
    '%': '------', '*': '-..-'
}

decoder = {}
letters = list(alphabet.keys())
morse = list(alphabet.values())

for i in range(len(morse)):
    decoder[morse[i]] = letters[i]

# Makes dictionary for decoding


# Encoder function

def encode(word):
    message = ""
    for i in word:
        if i != ' ':
            # Adds mores code letter to string
            message += alphabet[i] 
        # Adds a / after every word
        message +=  "/"
    # Removes extra / at the end
    message = message[:len(message) - 1]
    return message

def decode(message):
    # Splits the message into list of words
    words = message.split('//')
    revealed_message = ""
    for i in words:
        #splits each word into each character
        characters = i.split("/")
        for letter in characters:
            revealed_message += decoder[letter]
        revealed_message += " "
    # removes trailing white space
    return revealed_message.strip()


encodeMode = input(str("Would you like to encode in Morse(y/n)? "))

# Checks if they would like to encode, otherwise decodes.

if encodeMode == "y":
    word_to_encode = input("What would you like to encode? ")
    word_to_encode = word_to_encode.upper()
    print(encode(word_to_encode))
elif encodeMode == "n":
    word_to_decode = input(str("What would you like to decode? "))
    print(decode(word_to_decode))
else:
    print("Invalid statement, please try again...")