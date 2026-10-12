import math

def get_array_ascii(arr,num):
    binary_arr = list()

    for x in arr:
        current_bits = list()
        for j in range(8):
            current_bits.append(x % 2)
            x = math.floor(x/2)

        current_bits.reverse()
        binary_arr.extend(current_bits)

    if num>0:
        binary_arr.extend([0] * num )

    return binary_arr

def get_array_base64(arr):
    num = 0
    enc_nums_base64 = list()

    for i in range(int(len(arr) / 6)):
        k = 5
        num = 0
        for j in range(6):
            num += arr[i*6+j] * 2**k
            k-=1
        enc_nums_base64.append(num)
    return enc_nums_base64

def get_encoded_string(arr):
    string = ""
    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for x in arr:
        string += base64_table[x]
    return string