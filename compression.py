from collections import Counter

def create_hex_mapping(text):
    """Creates a mapping of characters to hex codes based on frequency."""
    frequency = Counter(text)
    sorted_chars = sorted(frequency.keys(), key=lambda char: (-frequency[char], char))

    hex_mapping = {}
    for i, char in enumerate(sorted_chars):
        if i < 14:
            hex_mapping[char] = format(i, 'X')  # 0 to E
        else:
            hex_index = (i - 14) // 16
            nibble_index = (i - 14) % 16
            hex_mapping[char] = f'F{hex_index:X}{nibble_index:X}'

    return hex_mapping

def compress(text, hex_mapping):
    """Compresses the text into a hex representation."""
    return ''.join(hex_mapping.get(char, '?') for char in text)

def decompress(compressed_text, hex_mapping):
    """Decompresses the hex representation back into the original text."""
    reverse_mapping = {v: k for k, v in hex_mapping.items()}
    decompressed = []
    index = 0
    length = len(compressed_text)

    while index < length:
        if compressed_text[index] == 'F':
            # Collect characters for codes starting with 'F'
            code = compressed_text[index:index + 3]  # For F0, F1, ..., FFF
            index += 3
        else:
            code = compressed_text[index]
            index += 1
        
        original_char = reverse_mapping.get(code, '?')
        decompressed.append(original_char)

    return ''.join(decompressed)


# Original text as a single long string
text = (
    "Marley was dead: to begin with. There is no doubt whatever about that. The register of "
    "his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. "
    "Scrooge signed it: and Scrooge’s name was good upon ’Change, for anything he chose to put "
    "his hand to. Old Marley was as dead as a door-nail. Mind! I don’t mean to say that I know, "
    "of my own knowledge, what there is particularly dead about a door-nail. I might have been "
    "inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade. "
    "But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb "
    "it, or the country’s done for. You will therefore permit me to repeat, emphatically, that Marley "
    "was as dead as a door-nail."
)


# Create hex mapping
hex_mapping = create_hex_mapping(text)
print("Hex Mapping:", hex_mapping)

# Compress the text
compressed_text = compress(text, hex_mapping)
print("Compressed Text:", compressed_text)


# Decompress the text
decompressed_text = decompress(compressed_text, hex_mapping)
print("Decompressed Text:", decompressed_text)

# Verify that the original text matches the decompressed text
assert text == decompressed_text, "Decompressed text does not match the original."
