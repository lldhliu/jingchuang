

# 求反码
def get_adverse(bin_str):
    ad = list(bin_str)
    # a = ""
    for i in range(len(ad)):
        if ad[i] == '0':
            ad[i] = '1'
        else:
            ad[i] = '0'
    a = "".join(ad)
    return a