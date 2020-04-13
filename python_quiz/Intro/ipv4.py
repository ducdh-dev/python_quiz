def isIPv4Address(s):
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 and len(str(n)) == len(str(int(n))) for n in p)


import ipaddress


def isIPv4Address(inputString):
    try:
        ipaddress.ip_address(inputString)
    except:
        return False
    return True
