def mod26_inv(a):
    """
    Form equation 1 = inv(a)*a mod m.
    """
    if a < 0:
        a = 26 - a
    for i in range(2, 26):
        if (a * i) % 26 == 1:
            return i
    return -1
