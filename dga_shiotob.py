#  DGA of Shiotob - http://johannesbader.ch/2015/01/the-dga-of-shiotob/

import argparse
"""
Shiotob DGA 

Generates domains for the Shiotob malware 

- top level domains alternate between '.net' and '.com'
- domains are between 14 and 19 characters long
- domains consist of all letters and digits 123945

author: baderj@gmx.net
"""

qwerty = 'qwertyuiopasdfghjklzxcvbnm123945678'

def sum_of_characters(domain):
    return sum([ord(d) for d in domain[:-3]])

def get_next_domain(domain):
    sof = sum_of_characters(domain)
    ascii_codes = [ord(d) for d in domain] + 100*[0]
    old_hostname_length = len(domain) - 4
    for i in range(0, 66):
        for j in range(0, 66):
            edi = j + i
            if edi < 65:
                p = (old_hostname_length * ascii_codes[j]) 
                cl = p ^ ascii_codes[edi] ^ sof
                ascii_codes[edi] = cl & 0xFF

    """
        calculate the new hostname length
        max: 255/16 = 15
        min: 10
    """
    cx = ((ascii_codes[2]*old_hostname_length) ^ ascii_codes[0]) & 0xFF
    hostname_length = int(cx/16) # at most 15
    if hostname_length < 10:
        hostname_length = old_hostname_length

    """
        generate hostname
    """
    for i in range(hostname_length):
        index = int(ascii_codes[i]/8) # max 31 --> last 3 chars of qwerty unreachable
        bl = ord(qwerty[index])
        ascii_codes[i] = bl

    hostname = ''.join([chr(a) for a in ascii_codes[:hostname_length]])

    """
        append .net or .com (alternating)
    """
    tld = '.com' if domain.endswith('.net') else '.net'
    domain = hostname + tld

    return domain

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('nr_of_domains', type=int)
    parser.add_argument('seed')
    args = parser.parse_args()
    domain = args.seed
    for i in range(args.nr_of_domains):
        print(domain)
        domain = get_next_domain(domain)
