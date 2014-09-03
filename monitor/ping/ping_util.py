'''
Created on Sep 2, 2014

@author: gerard
'''

import ping
import ping6
import ping_config
from impacket import ICMP6

def ping_ipv4_is_ok (ipv4_dest_addr):
    """
    Return TRUE if the IPv4 ping to the destination address is successful, FALSE otherwise.
    """
    delay = ping.do_one(ipv4_dest_addr, ping_config.TIMEOUT)
    if delay:
        return True
    else:
        return False


def ping_ipv6_is_ok (ipv6_dest_addr):
    """
    Return TRUE if the IPv6 ping to the destination address is successful, FALSE otherwise.
    """
    code = ping6.do_one(ping_config.IPV6_SRC_ADDR, ipv6_dest_addr, ping_config.TIMEOUT)
    if code == ICMP6.ICMP6.ECHO_REPLY:
        return True
    else:
        return False

