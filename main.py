from MAC_lib import support

import netifaces
import pickle
import os


class Mac_Guardian:
    def __init__(self):
        print("\n______________MAC_GUARDIAN______________\n")

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

    def print_mac_addresses(self):
        # Print the MAC addresses
        count = 0
        for interface, mac in self.mac_addresses.items():
            print(f"Interface: [{count}] {interface}, MAC Address: {mac}")
            count +=1

    def select_mac_addresses(self):
        # Choose the required MAC address
        selected_option = int(input("Select MAC: "))
        selected_mac = list(self.mac_addresses.items()) 
        mac_add = selected_mac[selected_option][1]
        # conver string to SHA256 hash
        self.mac_hash = support.sha256_hash(mac_add)

    def store_hash_value(self):
        # Store hash value into pickle file
        file_path = f"{os.getcwd()}/db"
        with open(file_path, 'wb') as f:
            pickle.dump(self.mac_hash, f)
        

mac= Mac_Guardian()
mac.get_mac_addresses()
mac.print_mac_addresses()
mac.select_mac_addresses()
mac.store_hash_value()