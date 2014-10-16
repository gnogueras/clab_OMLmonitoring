'''
Created on Sep 2, 2014

@author: gerard
'''

import utilities
import utilities
import utilities
from impacket import ICMP6

def ping_ipv4_is_ok (ipv4_dest_addr):
    """
    Return TRUE if the IPv4 utilities to the destination address is successful, FALSE otherwise.
    """
    delay = utilities.do_one(ipv4_dest_addr, ping_config.TIMEOUT)
    if delay:
        return 1
    else:
        return 0


def ping_ipv6_is_ok (ipv6_dest_addr):
    """
    Return TRUE if the IPv6 utilities to the destination address is successful, FALSE otherwise.
    """
    code = ping6.do_one(ping_config.IPV6_SRC_ADDR, ipv6_dest_addr, ping_config.TIMEOUT)
    if code == ICMP6.ICMP6.ECHO_REPLY:
        return 1
    else:
        return 0

