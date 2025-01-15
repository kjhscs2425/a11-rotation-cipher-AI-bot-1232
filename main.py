import string

alphabet = string.ascii_lowercase
print(alphabet)

password = "hi potato zzz"
# eve wants to steal my password

# make my password secret
key = 4

def encrypt(plaintext):
    ciphertext = ""
    for letter in plaintext:
        old_position = alphabet.find(letter)
        if old_position == -1:
            ciphertext += " "
        else:
            new_position = old_position + key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            ciphertext += new_letter
    return ciphertext

print(encrypt(password))

# Your task:
# figure out what key I used to encrypt this message:
secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"

def decrypt(ciphertext, test_key):
    for I in range(10):
        plaintext = ""
    for letter in ciphertext:
        old_position = alphabet.find(letter)
        if old_position == -1:
            plaintext += ''
        else:
            new_position = old_position - test_key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            plaintext += new_letter
    return plaintext

for possible_key in range(17):
    decrypted = decrypt(secret_message, possible_key)
    print(f"Key {possible_key}: {decrypted}")