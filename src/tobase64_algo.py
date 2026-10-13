import math

base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def string_to_bytes(string):
    return list(string.encode("utf-8"))

def bytes_to_padded_bits(data):
    data_len = len(data)
    bits = list()

    zero_add = (6 - 2 * (data_len % 3)) % 6

    for x in data:
        current_bits = list()
        for j in range(8):
            current_bits.append(x % 2)
            x = math.floor(x / 2)

        current_bits.reverse()
        bits.extend(current_bits)

    bits.extend([0] * zero_add)

    return bits, data_len

def encode(data):
    bits, data_len = bytes_to_padded_bits(data)
    encoded_chars = list()

    for i in range(len(bits) // 6):
        num = 0
        for j in range(6):
            num += bits[i * 6 + j] * 2 ** (5-j)

        encoded_chars.append(base64_table[num])

    padding = "=" * ((3 - data_len % 3) % 3)
    return "".join(encoded_chars) + padding

def get_from_encoded_string(s):
    arr = list()
    for x in s:
        for i in range(len(base64_table)):
            if x == base64_table[i]:
                arr.append(i)
            if x == "=": continue
    return arr




