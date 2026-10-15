Custom Base64 Encoder / Decoder

A simple Base64 encoder and decoder implemented from scratch in Python, without using external Base64 libraries.

This project was created to understand how Base64 works internally, including byte representation, binary conversion, encoding, decoding, and binary file handling.

Features

Encode text — convert text into a Base64 string.

Encode files — read a file as bytes and encode its contents into Base64.

Decode text — decode a Base64 string back into readable text.

Decode files — decode Base64-encoded file data and restore the original content.

Binary file support — restore PNG, JPEG, and PDF files.

UTF-8 support — handle text containing characters from different languages.

Project Structure

toBase64/
├── main.py
├── tobase64_algo.py
├── file_handler.py
├── README.md
└── Output.txt

main.py — command-line interface and application logic.

tobase64_algo.py — Base64 encoding and decoding algorithms.

file_handler.py — file reading and writing operations.

Output.txt — output file containing encoded data.

Requirements

Python 3.10 or newer.

No external dependencies are required.

How to Run

Clone the repository:

git clone https://github.com/fade36/tobase64.git
cd tobase64

Run the application:

python3 main.py

Choose one of the available operations from the menu.

Usage

The application provides four options:

Encode text — enter a string and get its Base64 representation.

Encode file — enter a file path to encode its contents. The result is saved to Output.txt.

Decode text — enter a Base64 string to decode it into readable text.

Decode file — enter the path to a file containing Base64 data. The decoded result is saved according to the detected file type.

Supported output formats include PNG, JPEG, PDF, and text files.

How It Works

The encoding algorithm follows these steps:

Convert the input into bytes.

Convert each byte into its 8-bit binary representation.

Divide the resulting bit sequence into 6-bit groups.

Map each 6-bit value to a character from the Base64 alphabet.

Add = padding when necessary.

Decoding reverses this process by converting Base64 characters back into 6-bit values, reconstructing the original bytes, and writing the decoded data to a file or converting it into text.

Limitations

File type detection currently relies on file signatures for PNG, JPEG, and PDF.

Other decoded data is treated as UTF-8 text.

The implementation is intended for learning and experimentation rather than production use.

Invalid Base64 input and malformed data are not yet handled comprehensively.

Future Improvements

Improve input validation and error handling.

Support additional file formats.

Improve handling of large files.

Add automated tests to verify encoding and decoding.

Make output paths configurable.