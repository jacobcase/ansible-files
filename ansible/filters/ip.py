from netaddr import *

def in_subnet(value, subnet):
    """ 
    Checks if an ip address is in the subnet 
    """
    ip = IPAddress(value)
    ip_net = IPNetwork(subnet)
    return ip in ip_net


class FilterModule(object):
    """ Filter module for basic ip address manipulation and checking"""

    def filters(self):
        return {
            'in_subnet': in_subnet
            }
