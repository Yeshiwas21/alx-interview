# 0x04. UTF-8 Validation

## About

UTF-8 (Unicode Transformation Format - 8-bit) is a widely-used character encoding that represents each character in a text as a unique numerical code point. It was designed to handle the vast majority of characters in the Unicode character set, which includes most of the world's written languages, as well as a large number of symbols and special characters.

UTF-8 has the following properties:

- It uses 1 to 4 bytes to represent a character, depending on the code point of the character.
- Characters that have code points between 0 and 127 (inclusive) are represented using 1 byte, which is identical to the ASCII encoding.
- Characters that have code points between 128 and 2047 (inclusive) are represented using 2 bytes.
- Characters that have code points between 2048 and 65535 (inclusive) are represented using 3 bytes.
- Characters that have code points between 65536 and 1114111 (inclusive) are represented using 4 bytes.
- This allows for efficient use of storage space for the most common characters, while still providing support for a wide range of characters.

UTF-8 is particularly useful for transmitting text over the internet because it is compatible with ASCII, which means that any ASCII text is also valid UTF-8 text. This allows for easy integration with existing systems and applications that were designed for ASCII.

UTF-8 is also a good choice for storing text in databases or file systems because it is compact and can handle a wide range of characters. Additionally, it is supported by most modern software and programming languages, which makes it easy to use in a variety of contexts.

In summary, UTF-8 encoding is a widely used character encoding that can represent a wide range of characters using 1 to 4 bytes, it is backward compatible with ASCII, it's compact and efficient and supported by most modern software and programming languages.

## Tasks

- **0. UTF-8 Validation**
  - [0-validate_utf8.py](./0-validate_utf8.py): Write a method that determines if a given data set represents a valid UTF-8 encoding.
  &NewLine;

    - Prototype: def validUTF8(data)
    - Return: True if data is a valid UTF-8 encoding, else return False
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

  ```bash
  carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
  True
  True
  False
  carrie@ubuntu:~/0x04-utf8_validation$
  ```
