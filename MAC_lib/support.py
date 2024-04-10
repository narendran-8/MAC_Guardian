import hashlib

def sha256_hash(input_string):
    # Convert the input string to bytes (UTF-8 encoding)
    input_bytes = input_string.encode('utf-8')
    # Calculate the SHA-256 hash
    sha256_hash = hashlib.sha256(input_bytes)
    # Get the hexadecimal representation of the hash
    hash_hex = sha256_hash.hexdigest()
    print(hash_hex)
    return hash_hex
 
#  def store_hash_value(hash_value):