#
morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}


def encrypt(text):
    """Takes a random text and converts it to a morse code"""
    morse_code = ""
    for char in text.upper():
        if char != " ":
            morse_code += morse_dict[char] + " "
        else:
            morse_code += " "
    return morse_code


def decrypt(text):
    """Return the alphabet equivalent of a morse code """
    text += " "
    english = ""
    citext = ""
    for char in text:
        if char != " ":
            i = 0
            citext += char
        else:
            i += 1
            if i == 2:
                english += " "
            else:
                english += list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
                citext = ""
    return english


def main():
    user_text = input("Enter text to encode: ")
    if user_text.startswith('.') or user_text.startswith('-'):
        print(decrypt(user_text))
    else:
        print(encrypt(user_text))


if __name__ == '__main__':
    main()
