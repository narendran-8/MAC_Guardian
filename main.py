import netifaces

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

mac= Mac_Guardian()
mac.get_mac_addresses()
mac.print_mac_addresses()
