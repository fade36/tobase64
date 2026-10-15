def read_from_file(path):
    with open(path, "rb") as file:
        return list(file.read())

def output_encoded(s):
    with open("Output.txt", "w") as file:
        file.write(s)

def read_encoded_file(path):
    with open(path, "r") as file:
        return file.read()

def output_png(arr):
    with open("Decoded_png.png", "wb") as file:
        file.write(bytes(arr))

def output_jpg(arr):
    with open("Decoded_jpg.jpg", "wb") as file:
        file.write(bytes(arr))

def output_pdf(arr):
    with open("Decoded_pdf.pdf", "wb") as file:
        file.write(bytes(arr))

def output_txt(s):
    with open("Decoded_txt.txt", "w") as file:
        file.write(s)