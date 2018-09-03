# -*- coding:utf-8 -*-

# 主站地址在通讯时用来唯一识别通讯的主站端对象（如应用服务器、 厂商分析模块、 前置机等）
# 命令序号用于在异步通讯过程中，区分发送和应答的对应关系

def channel(coding):
    switcher = {
        31: "短信编码",
        32: "GPRS/CDMA",
        33: "PSTN",
        34: "CSD",
    }
    return switcher.get(coding, "保留位")

def MSTA(data):
    MSTA1 = data[2][0:2]
    MSTA2 = data[2][2:4]
    # print(MSTA1,MSTA2)
    # 16进制字符串转换为高位补零的八位2进制字符串
    c = bin(int(MSTA1, 16))
    d =(str(c))[2:]
    e = d.zfill(8)
    # print(int(e[2:8],2))

    if int(e[2:8],2) == 0:
        # print('主站端对象为：集中器主动上报')
        return ('集中器主动上报')
    elif 0 <= int(e[2:8],2) <=9:
        # print('主站端对象为：应用服务器')
        return ('应用服务器')
    elif 10 <= int(e[2:8],2) <=29:
        # print('主站端对象为：厂商分析模块')
        return ('厂商分析模块')
    elif 30 <= int(e[2:8],2) <=39:
        # print('前置机')
        # print('前置机信道为:{0}'.format(channel(int(e[2:8],2))))
        return ('前置机信道为-{0}'.format(channel(int(e[2:8],2))))
    elif 50 <= int(e[2:8],2) <=62:
        # print('保留')
        return ('保留')
    elif int(e[2:8],2) == 63:
        # print('主站端对象为：主站广播地址')
        return ('主站广播地址')
    else:
        # print('主站地址有错')
        return ('主站地址有错')

