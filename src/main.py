import tobase64_algo as tba
import file_handler as fh

def main():
    print("=" * 40)
    print("       CUSTOM BASE64 ENCODER")
    print("=" * 40)

    print("1. Encode text")
    print("2. Encode file")
    print("3. Decode text")
    print("4. Decode file")
    option = int(input("Type your option:"))
    match option:
        case 1:
            string = input("Type text to encode: ")
            arr = tba.string_to_bytes(string)
            print(tba.encode(arr))
        case 2:
            path = input("Type the path: ")
            arr = fh.read_from_file(path)
            s = tba.encode(arr)
            with open("Output.txt", "w") as file:
                file.write(s)
        case 3:
            string = input("Type text to decode: ")
            print(tba.get_from_encoded_string(string))
        case 4:
            path = input("Type the path: ")

        case _:
            print("Invalid option")
            return


   # print("\nEncoded result:")
   # print("-" * 40)
    #print(encoded_string)
    #print("-" * 40)

if __name__ == "__main__":
    main()
