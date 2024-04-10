import os
import hashlib
import pickle

from MAC_lib import support

import netifaces

class Authentic:
    def __init__(self):
        # Read and conver MAC
        file_path = f"{os.getcwd()}/db"
        try:
            with open(file_path, 'rb') as f:
                self.string_value = pickle.load(f)
        except FileNotFoundError:
            print("Unable to locate File")
    

    def get_mac_addresses(self):
        self.mac_addresses = {}
        # Get a list of all network interfaces
        interfaces = netifaces.interfaces()
        for interface in interfaces:
            try:
                # Get the MAC address of the interface
                mac = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
                self.mac_addresses[interface] = mac
            except KeyError:
                # If MAC address is not found, continue to the next interface
                continue
        return self.mac_addresses

    def check_mac_addresses(self):
        # check assigined MAC == System MAC
        for interface, mac in self.mac_addresses.items():            
            if self.sha256_hash(str(mac)) == self.string_value:
                print("Correct MAC")
        # print("not mac found")

    def sha256_hash(self, input_string):
        # Convert the input string to bytes (UTF-8 encoding)
        input_bytes = input_string.encode('utf-8')
        # Calculate the SHA-256 hash
        sha256_hash = hashlib.sha256(input_bytes)
        # Get the hexadecimal representation of the hash
        hash_hex = sha256_hash.hexdigest()
        return hash_hex

auth = Authentic()
auth.get_mac_addresses()
auth.check_mac_addresses()