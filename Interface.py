from module_test import encrypt, decrypt


def interface():
    # keeps tabs on all typed encryption(s)
    stored_encryption = {}

    while True:
        user_input = input('Type "encode" to encrypt, type "decode" to decrypt, or "exit" to end program:\n')

        if user_input == "exit":
            break

        if user_input == "encode":
            e_msg = input("Type your message:\n")
            e_shift = int(input("Type the shift number:\n"))

            e = encrypt(e_msg, e_shift)

            # stores result of encryption in dictionary to access if needed
            stored_encryption[e[0]] = e[1]
            print(f"Here's the encoded result: {e[0]}")

        if user_input == "decode":
            d_msg = input("Type your message:\n")
            d = decrypt(stored_encryption, d_msg)

            if d == "Couldn't find word.": print("Couldn't find message.")
            else: print(f"Here's the decoded result: {d}")

            try_again = input('Type "yes" if you want to continue:\n')
            if try_again == "yes": continue
            else: break


interface()


























