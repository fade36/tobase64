# Custom Base64 Encoder / Decoder

A simple Base64 encoder and decoder implemented from scratch in Python, without using external Base64 libraries.

This project was created to understand how Base64 works internally, including byte representation, binary conversion, encoding, decoding, and binary file handling.

---

## Features

- **Encode text** — convert text into a Base64 string.
- **Encode files** — read a file as bytes and encode its contents into Base64.
- **Decode text** — decode a Base64 string back into readable text.
- **Decode files** — decode Base64-encoded file data and restore the original content.
- **PNG, JPEG, and PDF support** — restore binary files after decoding.
- **UTF-8 support** — handle text containing characters from different languages.
- **No external dependencies** — the encoding and decoding algorithms are implemented manually.

---

## Project Structure

```text
toBase64/
│
├── main.py
├── tobase64_algo.py
├── file_handler.py
├── README.md
└── .gitignore
```

### File Description

| File | Description |
|---|---|
| `main.py` | Main application and command-line interface |
| `tobase64_algo.py` | Custom Base64 encoding and decoding algorithms |
| `file_handler.py` | Functions for reading and writing files |
| `README.md` | Project documentation |
| `.gitignore` | Specifies files that Git should ignore |

---

## Requirements

- Python 3.10 or newer
- No external libraries required

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/fade36/tobase64.git
```

### 2. Navigate to the project directory

```bash
cd tobase64
```

### 3. Run the application

```bash
python3 main.py
```

---

## Usage

After starting the application, a menu with four options will appear.

### 1. Encode Text

Enter a text string. The program converts it into bytes, encodes those bytes using Base64, and prints the result.

### 2. Encode File

Enter the path to a file. The program reads its binary contents, encodes the data into Base64, and saves the result to `Output.txt`.

### 3. Decode Text

Enter a Base64 string. The program decodes it and prints the resulting text.

### 4. Decode File

Enter the path to a text file containing Base64-encoded data. The program decodes the contents and attempts to restore the original file.

Supported output formats:

- PNG
- JPEG
- PDF
- TXT

---

## How It Works

### Encoding Process

The encoder implements the Base64 algorithm manually:

1. Convert the input text or file into bytes.
2. Convert each byte into its 8-bit binary representation.
3. Combine the bits into groups of 6.
4. Convert each 6-bit group into a number between 0 and 63.
5. Use the Base64 alphabet to map each number to a character.
6. Add `=` padding when necessary.

### Decoding Process

The decoder performs the reverse operations:

1. Convert Base64 characters into their corresponding numerical values.
2. Convert each value into a 6-bit binary representation.
3. Reconstruct the original sequence of bytes.
4. Interpret the bytes as UTF-8 text or write them to a binary file.

---

## Current Limitations

- File type detection currently relies on signatures for PNG, JPEG, and PDF.
- Other decoded data is treated as UTF-8 text.
- Invalid Base64 input is not yet handled comprehensively.
- The implementation is intended for learning and experimentation rather than production use.

---

## Future Improvements

- Improve input validation and error handling.
- Support additional file formats.
- Improve performance when processing large files.
- Add automated tests for encoding and decoding.
- Allow users to specify output filenames and paths.
- Improve detection of binary file formats.

---

## Purpose

This project is a learning exercise focused on understanding Base64 encoding, binary data, bitwise representation, and file handling in Python.

The main goal was to implement the algorithm from scratch rather than rely on Python's built-in Base64 module.

---
