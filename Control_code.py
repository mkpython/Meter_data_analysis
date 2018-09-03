# -*- coding:utf-8 -*-

# 控制码表示要求执行的操作
from slicing_data import slicing

D5_D0 = {'000001':'读当前数据',       '000111':'实时写对象参数',       '001000':'写对象参数',       '001111':'短信唤醒协议',
         '010001':'集中器实时召测命令',       '010010': '集中器抄收日常综合数据',         '010011':'集中器抄收重点户负荷数据',
         '010100':'集中器对表拉合闸控制',     '010101':'集中器抄收电表表号',              '010110':'集中器抄收测量点其他数据',
         '010111':'级联命令，用于集中器采集配变终端电量数据',    '011000':'级联命令，用于实现主终端定时轮询从终端上报需求的功能',
         '011001':'集中器异常告警、告警确认',          '100000':'取消集中器召测命令',                       '100001':'登录',
         '100010': '登录退出',    '100100':'心跳检验',      '101000':'级联传输控制命令,用于实现主终端允许从终端主动上报的功能'
         }
def Cc(data):
    # 由前面主站地址与命令序号获得通讯方式，是主站与集中器通讯，还是主站对象间通讯，
    # 这里暂时用MSTA1的二进制代码第一位代替。实际标志位未知（待求解）
    MSTA1 = data[2][0:2]
    method1 = bin(int(MSTA1, 16))
    method2 = (str(method1))[2:]
    method3 = method2.zfill(8)
    return (method3[0])

# 16进制字符串转换为高位补零的八位2进制字符串
def conversion(data):
    c = bin(int(data, 16))
    d = (str(c))[2:]
    e = d.zfill(8)
    return (e)
    # # 16进制字符串转换为高位补零的八位2进制字符串
    # c = bin(int(data[4], 16))
    # d =(str(c))[2:]
    # e = d.zfill(8)
    # # print(e)


# 解析D7：传送方向
def Cc_D7(data1,data2):
    if data1 == '0':
        if data2[0] == '0':
            # print('主站与集中器通讯：由主站发出的命令帧或应答帧')
            return ('由主站发出的命令帧或应答帧')
        else:
            # print('主站与集中器通讯：由集中器发出的请求帧或应答帧')
            return ('由集中器发出的请求帧或应答帧')
    else:
        if data2[0] == '0':
            # print('为主站对象间通讯：主站编号小的对象发出')
            return ('主站编号小的对象发出')
        else:
            # print('为主站对象间通讯：主站编号大的对象发出')
            return ('主站编号大的对象发出')

# 解析D6：异常标志
def Cc_D6(data):
    if data[1] == '0':
        # print('异常标志为：确认帧')
        return ('确认帧')
    else:
        # print('异常标志为：否定帧')
        return ('否定帧')

# 解析D5~D0：功能码
def Cc_D5_D0(data):
    if data[2:8] in D5_D0:
        # print('功能为：{0}'.format(D5_D0.get(conversion(data)[2:8])))
        return ('{0}'.format(D5_D0.get(data[2:8])))



# a = slicing('68960020006000682100000716')
# print(a)
# b = Cc_D7(Cc(a),conversion(a[4]))
# c = Cc_D6(conversion(a[4]))
# d = Cc_D5_D0(conversion(a[4]))
# print(b)
# # print(a[4])
# # b = Cc_D7(a[4])[0]
# # c = Cc_D6(a[4])[1]
# # d = Cc_D5_D0(a[4])[2:8]
# # print(a)
# # print(b)
# print(c)
# print(d)