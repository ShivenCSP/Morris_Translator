alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

decoder = {}
letters = list(alphabet.keys())
morse = list(alphabet.values())

for i in range(len(morse)):
    decoder[morse[i]] = letters[i]


def encode(word):
    message = ""
    for i in word:
        message += alphabet[i]
    return message

def decode(message):
    words = message.split('/')
    revealed_message = ""
    for i in words:
        characters = i.split(" ")
        for letter in characters:
            revealed_message += decoder[letter]
        revealed_message += " "
    return revealed_message.strip()


encodeMode = input(str("Would you like to encode in Morse(y/n)?"))

if encodeMode == "y":
    word_to_encode = (input(str("What would you like to encode?"))).upper()
    print(encode(word_to_encode))
elif encodeMode == "n":
    word_to_decode = input(str("What would you like to decode?"))
    print(decode(word_to_decode))
else:
    print("Invalid statement, please try again...")
