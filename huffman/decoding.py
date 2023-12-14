def huffman_decoding(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_words = []
    current_code = ""
    for bit in encoded_text.split():
        current_code += bit
        if current_code in reverse_codes:
            decoded_words.append(reverse_codes[current_code])
            current_code = ""
    return " ".join(decoded_words)
