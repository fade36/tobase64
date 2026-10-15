import tobase64_algo as tba
import file_handler as fh

png = [137, 80, 78, 71, 13, 10, 26, 10]
jpeg = [255, 216, 255]
pdf = [37, 80, 68, 70, 45]

def main():
    print("=" * 40)
    print("     CUSTOM BASE64 ENCODER/DECODER")
    print("=" * 40)

    print("1. Encode text")
    print("2. Encode file")
    print("3. Decode text")
    print("4. Decode file")

    option = int(input("Type your option:"))

    match option:
        case 1:
            string = input("Type text to encode: ")
            bytes_arr = tba.string_to_bytes(string)
            print(tba.encode(bytes_arr))

        case 2:
            path = input("Type the path: ")
            bytes_arr = fh.read_from_file(path)
            encoded_res = tba.encode(bytes_arr)
            fh.output_encoded(encoded_res)

        case 3:
            string = input("Type text to decode: ")
            from_base = tba.from_base64(string)
            bytes_arr = tba.to_bytes(from_base)
            res = tba.decode(bytes_arr)
            print(res)

        case 4:
            path = input("Type the path: ") # .txt
            s = fh.read_encoded_file(path)
            temp_arr = tba.from_base64(s)
            bytes_arr = tba.to_bytes(temp_arr)

            if png == bytes_arr[:len(png)]:
                fh.output_png(bytes_arr)
            elif jpeg == bytes_arr[:len(jpeg)]:
                fh.output_jpg(bytes_arr)
            elif pdf == bytes_arr[:len(pdf)]:
                fh.output_pdf(bytes_arr)
            else:
                res = tba.decode(bytes_arr)
                fh.output_txt(res)
        case _:
            print("Invalid option")
            return


if __name__ == "__main__":
    main()
