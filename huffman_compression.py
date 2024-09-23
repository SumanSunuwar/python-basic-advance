import heapq
from collections import defaultdict, Counter

# Define a class for the Huffman Tree Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for heapq
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree based on character frequencies
def build_huffman_tree(text):
    # Step 1: Count frequencies
    frequency = Counter(text)

    # Step 2: Create a priority queue (min-heap) using frequency data
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Step 3: Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with the sum of frequencies
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Push the merged node back to the heap
        heapq.heappush(heap, merged)

    # Step 4: Return the root node (Huffman Tree)
    return heap[0]

# Generate Huffman Codes by traversing the tree
def generate_huffman_codes(root):
    huffman_codes = {}

    def generate_codes_helper(node, current_code):
        if node is None:
            return

        if node.char is not None:
            # Leaf node, save the current code for this character
            huffman_codes[node.char] = current_code

        generate_codes_helper(node.left, current_code + '0')
        generate_codes_helper(node.right, current_code + '1')

    generate_codes_helper(root, "")
    return huffman_codes

# Compress the text using the generated Huffman codes
def huffman_compress(text, huffman_codes):
    compressed_text = ''.join(huffman_codes[char] for char in text)
    return compressed_text

# Decompress the binary data using the Huffman Tree
def huffman_decompress(compressed_text, root):
    decompressed_text = []
    current_node = root

    for bit in compressed_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decompressed_text.append(current_node.char)
            current_node = root

    return ''.join(decompressed_text)

# Main Function: Compress and Decompress using Huffman Coding
def huffman_coding(text):
    # Build Huffman Tree
    huffman_tree = build_huffman_tree(text)

    # Generate Huffman Codes
    huffman_codes = generate_huffman_codes(huffman_tree)
    
    # Print Huffman Codes for Debugging
    print("Huffman Codes:", huffman_codes)

    # Compress the text
    compressed_text = huffman_compress(text, huffman_codes)
    
    # Decompress the text
    decompressed_text = huffman_decompress(compressed_text, huffman_tree)

    # Verify if decompression matches original text
    if decompressed_text == text:
        print("Decompression successful!")
    else:
        print("Decompression failed.")

    # Output compressed size and original size
    original_size = len(text) * 8  # Original size in bits (assuming 1 char = 8 bits)
    compressed_size = len(compressed_text)  # Compressed size in bits
    
    print("Original Size:", original_size, "bits")
    print("Compressed Size:", compressed_size, "bits")

    return compressed_text, decompressed_text

# Example usage:
text = """Marley was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge’s name was good upon ’Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail. Mind! I don’t mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail. I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade. But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country’s done for. You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail."""

compressed_text, decompressed_text = huffman_coding(text)

# Debugging: Print results
print("\nCompressed Text:", compressed_text)
print("\nDecompressed Text:", decompressed_text)
