import tobase64 as tb

def main():
    print("=" * 40)
    print("       CUSTOM BASE64 ENCODER")
    print("=" * 40)

    dirty_string = input("Enter text to encode: ")
    string = "".join(dirty_string.split())
    to_ascii = [ord(char) for char in string]

    rest = len(string) % 3
    equal_chars = (3 - rest) % 3
    amount_add =(6 - 2*rest) % 6

    initial_array = tb.get_array_ascii(to_ascii,amount_add)
    base_arr = tb.get_array_base64(initial_array)
    encoded_string = tb.get_encoded_string(base_arr)
    encoded_string += "=" * equal_chars

    print("\nEncoded result:")
    print("-" * 40)
    print(encoded_string)
    print("-" * 40)

if __name__ == "__main__":
    main()
