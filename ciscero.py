#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Michael Edie / @c0demech
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import socket
import argparse
import platform
from ipaddress import (
  ip_address,
  ip_network, IPv4Interface
)
__email__ = "michael@sawbox.net"
__description__ = "Calculates DHCP Option 121 for use with pfSense (RFC 3442)"

def cidr_to_hex():
  cidr_str = str(args.subnet[0]).split('/')[1]
  cidr_hex = f'{int(cidr_str):02x}'
  return cidr_hex

def netaddr_to_hex(netaddr,cidr):
  cidr = int(cidr, 16)
  ip = str(IPv4Interface(netaddr).ip)
  ip_hex = socket.inet_aton(ip).hex()
  ip_val = ""

  if (cidr > 0):
    ip_val += ip_hex[:2]
  if (cidr > 8):
    ip_val += ip_hex[2:-4]
  if (cidr > 16):
    ip_val += ip_hex[4:-2]
  if (cidr > 24):
    ip_val += ip_hex[-2:]

  return ip_val
  
def main():
  cidr = cidr_to_hex() 
  gateway = socket.inet_aton(str(args.gateway)).hex()
  value = []
  for netaddr in args.subnet:
    value.append(cidr)
    value.append(netaddr_to_hex(netaddr,cidr))
    value.append(gateway)

  option = ''.join(value)
  dhcp_option_value = ':'.join(option[n:n+2] for n in range(0, len(option), 2))
  print(dhcp_option_value)


if __name__ == '__main__':

  arg = argparse.ArgumentParser(description="cisero version 1")
  arg.add_argument("-v", "--version", action="version", version="%(prog)s v1")
  arg.add_argument("-s", "--subnet", help="Subnet in CIDR notation.",\
      type=ip_network, nargs='+', required=True) 
  arg.add_argument("-g", "--gateway", help="Default gateway for subnet(s).",\
      type=ip_address, required=True) 

  args = arg.parse_args()
  main()
