def xor_files(file1_path, file2_path, output_file_path):
    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        # Read the content of the files as bytes
        file1_content = file1.read()
        file2_content = file2.read()

        # Perform XOR operation on the bytes
        xor_result = bytes([a ^ b for a, b in zip(file1_content, file2_content)])

    # Write the XOR result to a new file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(xor_result)

# Example usage
file1_path = '33.1'
file2_path = '33.2'
output_file_path = 'pyoutput.txt'

xor_files(file1_path, file2_path, output_file_path)
print(f"XOR operation completed and saved to {output_file_path}")
