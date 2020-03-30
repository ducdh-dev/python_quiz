""" convert số n hệ x sang hệ thập lục phân """


def base_conversion(n, x):
    return hex(int(n, x)).split('x')[-1]  # nhị phân là bin(int(n, x)).split('x')[-1]
