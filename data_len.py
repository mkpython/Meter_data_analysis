# -*- coding:utf-8 -*-

# 16进制字符串转换为高位补零的八位2进制字符串
def conversion(data):
    c = bin(int(data, 16))
    d = (str(c))[2:]
    e = d.zfill(8)
    return(e)

# 将分开的二进制高低位数据组合
def combination(str1,str2):
    return str1 + str2

# L为数据域的字节数，十六进制编码，低字节在前，高字节在后
def L(data):
    low = data[5][0:2]
    high = data[5][2:4]
    # 调用函数conversion函数,得到高低位的二进制编码
    # 调用combination函数将数据组合，最终得到数据长度L的16位二进制编码
    data_all = combination(conversion(high), conversion(low))
    # 得到数据域DATA的字节数
    bytes_of_DATA = int(data_all, 2)  # 将2进制字符串转换为10进制，并输出
    # print('数据域DATA的字节数为：{0}'.format(bytes_of_DATA))
    return ('{0}'.format(bytes_of_DATA))



