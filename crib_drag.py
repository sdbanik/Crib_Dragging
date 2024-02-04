def xor_bytes(byte_string1, byte_string2):
    # XOR operation on two byte strings
    return bytes(a ^ b for a, b in zip(byte_string1, byte_string2))

def main():

    while True: 
        # Read content from a file as bytes
        with open('pyoutput.txt', 'rb') as file:
            file_content_bytes = file.read()
        # Given input string
        input_string = input("\n Enter the guess words: ")

        # Convert input string to bytes
        input_bytes = input_string.encode()

        # Iterate through the file content and XOR with the input string in chunks of the length of word
        chunk_size = len(input_string)
        a=0
        for i in range(0, len(file_content_bytes) - chunk_size + 1, 1):
            a+=1
            chunk = file_content_bytes[i:i + chunk_size]
            xor_result = xor_bytes(chunk, input_bytes)
            print(f"Iteration {a}: {xor_result.decode()}")


        # Ask the user if they want to continue
        continue_input = input("Do you want to continue? (y/n): ")
        if continue_input.lower() != 'y':
            break  # Exit the loop if the user enters 'n' or anything other than 'y'

if __name__ == "__main__":
    main()

