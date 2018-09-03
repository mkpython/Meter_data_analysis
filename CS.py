# -*- coding:utf-8 -*-

# 从帧起始符开始到校验码之前的所有各字节的和模 256 的余。即各字节二进制算术和，不计超过 256 的溢出值

import re

# 按固定长度分割字符串
def cut_text(text, lenth):
    textArr = re.findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
    return textArr

# 16进制字符串转换为高位补零的八位2进制字符串
def conversion(data):
    c = bin(int(data, 16))
    d = (str(c))[2:]
    e = d.zfill(8)
    return(e)


# 得到我们要求和运算的部分
def A(data):
    b = data[:-3]
    c = []
    for i in range(len(b)):
        c.append(conversion(b[i]))
    return c

# 求和
def B(data):
    a = 0
    for i in range(len(data)):
        a = a + int(data[i],2)
    # print(type(a))
    return a

# 取出低八位
def C(data):
    b = bin(data)[2:]
    # print(type(b))
    # print(b)
    d = b[-8:]
    return d

# 将2进制数转换成16进制字符串
def D(data):
    c = hex(int(data, 2))
    d = (str(c))[2:]
    # print(type(d))
    # print(d)
    return d

def cs(data):
    end = D(C(B(A(cut_text(data, 2)))))
    # print(type(cut_text(data, 2)))
    # xxx = cut_text(data, 2)
    # print(xxx[-3])
    if end == cut_text(data, 2)[-3]:
        # print('校验位：正确')
        return ('正确')
    else:
        # print('校验位：错误')
        return ('错误')


