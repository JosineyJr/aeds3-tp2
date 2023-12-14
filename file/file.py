import json
from huffman.encoding import huffman_encoding
from huffman.decoding import huffman_decoding

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
        return huffman_encoding(text)
    except FileNotFoundError:
        return "Arquivo não encontrado.", {}


def compress_file(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            text = file.read()
        encoded_text, codes = huffman_encoding(text)
        with open(output_file, "w") as file:
            file.write(json.dumps(codes) + "\n" + encoded_text)
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado.")


def decompress_file(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            codes = json.loads(file.readline().rstrip("\n"))
            encoded_text = file.readline()
        decoded_text = huffman_decoding(encoded_text, codes)
        with open(output_file, "w") as file:
            file.write(decoded_text)
    except FileNotFoundError:
        print("Arquivo de saída não encontrado.")
