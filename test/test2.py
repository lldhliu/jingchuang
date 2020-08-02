# 求反码


def Getadverse(trueform):
    ad = list(trueform)
    a = ""
    for i in range(len(ad)):
        if ad[i] == '0':
            ad[i] = '1'
        else:
            ad[i] = '0'
    a = "".join(ad)
    return a


# 由原码求反码
def Convert(form):
    ad = list(form)
    a = ""
    l = len(ad) - 1
    flag = False
    for i in range(len(ad)):
        if ad[l - i] == '1' and flag == False:
            flag = True
            continue
        if flag == True:
            if ad[l - i] == '0':
                ad[l - i] = '1'
            else:
                ad[l - i] = '0'
    a = "".join(ad)
    return a


def main():
    truform = input("put string: ")
    print('反码:', Getadverse(truform))
    print('补码:', Convert(truform))
    print('求得原码:', Convert(Convert(truform)))
    print('真正原码:', truform)



main()
