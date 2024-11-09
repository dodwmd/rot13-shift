def shift_char(c, shift):
    # Only shift alphabetic characters
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + shift) % 26 + base)
    return c  # Non-alphabetic characters remain the same

def encode_text(plain_text):
    result = []
    
    # Split text into words
    words = plain_text.split()

    # Process each word
    for word in words:
        shifted_word = ''.join(shift_char(c, 13 + i) for i, c in enumerate(word))
        result.append(shifted_word)
    
    # Join the shifted words back into a sentence
    return ' '.join(result)

def decode_text(encoded_text):
    result = []
    
    # Split text into words
    words = encoded_text.split()

    # Process each word
    for word in words:
        shifted_word = ''.join(shift_char(c, -(13 + i)) for i, c in enumerate(word))
        result.append(shifted_word)
    
    # Join the shifted words back into a sentence
    return ' '.join(result)

# Example usage
plain_text = 'Did you ever figure out my encryption?'
encoded = encode_text(plain_text)
decoded = decode_text(encoded)

print("Plain Text: ", plain_text)
print("Encoded Text: ", encoded)
print("Decoded Text: ", decoded)
