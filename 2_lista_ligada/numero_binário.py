def decimal_para_binario(num):
    if num == 0:
        return ''
    return decimal_para_binario(num//2) + str(num%2)
