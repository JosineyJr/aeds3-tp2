import collections
from huffman.tree import build_huffman_tree

def calculate_frequencies(text):
    words = text.split()
    return collections.Counter(words)


def build_codes(node, prefix="", code={}):
    if node is not None:
        if node.word is not None:
            code[node.word] = prefix
        build_codes(node.left, prefix + "0", code)
        build_codes(node.right, prefix + "1", code)
    return code


def huffman_encoding(text):
    frequencies = calculate_frequencies(text)
    print(frequencies)
    root = build_huffman_tree(frequencies)
    codes = build_codes(root)
    encoded_text = " ".join([codes[word] for word in text.split()])
    return encoded_text, codes
