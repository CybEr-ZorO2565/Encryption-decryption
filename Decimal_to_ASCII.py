import struct

# Enter your decimal values here
decimal_values = [
    #provide the input decimal value from the JS page here
]

# Convert each decimal value to 4-byte Big-Endian
raw_bytes = b''.join(struct.pack('>I', value) for value in decimal_values)

# Display hexadecimal representation
print("Hexadecimal:")
print(raw_bytes.hex().upper())

# Display raw bytes
print("\nRaw Bytes:")
print(raw_bytes)

# Convert raw bytes to ASCII
print("\nASCII:")
print(raw_bytes.decode('ascii', errors='replace'))