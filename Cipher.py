print('''
    #Welcome To The Encryption/Decryption Program.
    #This Version Maynot Include Custom Encryption
''')

print('''
    # Process

    # ==> Type "1" to encrypt a message
    # ==> Type "2" to decrypt a message
''')

                        # Casear Cipher Encryptor (LoadUp Process)

def encrypt(text, s):
    result = ""
 # transverse the plain text
    for i in range(len(text)):
        char = text[i]
       # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Space Error Resolved.
        elif (char == " "):
            result += char
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
            
    return result


                        # Casear Cipher Decryptor (LoadUp Process)

    
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():
            # Space Error Resolved.
            if (c == " "):
                c_og += c
            # if it's a number,shift its actual value 
            else:
                c_og += (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted

Get_The_Value = input("What Do You Want To Do: ")
print(end="\n")

if Get_The_Value == "1":
    text_before_encrytion = input("Enter Text To Encrypt: ")
    text_Transfered = text_before_encrytion
    s = int(input("Enter Shift Value: "))

    print ("Plain Text : " + text_Transfered)
    print ("Shift Key : " + str(s))
    print ("Cipher: " + encrypt(text_Transfered, s)) #Executing The Encryptor

elif Get_The_Value == "2":
    text_before_decrytion = input("Enter Text To Decrypt: ")
    text_Transfered = text_before_decrytion
    s = int(input("Enter Shift Value: "))

    print ("Cipher Text : " + text_Transfered)
    print ("Shift Key : " + str(s))
    print ("Plain Text: " + cipher_decrypt(text_Transfered, s)) #Executing The Decryptor
else:
    print("Invalid Input", "\n")
    exit()



                                                # The End
