# -*- coding:utf-8 -*-

from slicing_data import slicing


# 解析集中器逻辑地址
# 标识通讯的最终发起端和接收端
A1_mapping = {'80':'省公司','81':'广州','82':'深圳','83':'东莞','84':'佛山','85':'江门','86':'惠州','87':'珠海',
              '88':'中山','89':'肇庆','8A':'云浮','8B':'韶关','8C':'清远','8D':'湛江','8E':'茂名','90':'汕头',
              '91':'揭阳','92':'潮州', '93': '汕尾', '94': '梅州', '95': '河源'}
A2_D6_D5 = {'00':'大客户现场终端','01':'配变终端',
            '10':'低压抄表集中器','11':'其他'}
def rtua(data):
    A1 = data[1][0:2]    # 地市码
    if A1 in A1_mapping:
        # print('地市供电局为：{0}'.format(A1_mapping.get(A1)))
        return ('{0}'.format(A1_mapping.get(A1)))
    else:
        # print('地市供电局信息：未知')
        return ('未知')

def rtua1(data):

    A2 = data[1][2:4]    # 区县码
    B1 = data[1][4:6]    # 集中器地址
    B2 = data[1][6:8]    # 集中器地址

    # 16进制字符串转换为高位补零的八位2进制字符串
    c = bin(int(A2, 16))
    d =(str(c))[2:]
    e = d.zfill(8)
    # print(e[3:8])
    if e[1:3] in A2_D6_D5:
       # print('客户端类型为：{0}'.format(A2_D6_D5.get(e[1:3])))
       return ('{0}'.format(A2_D6_D5.get(e[1:3])))
    else:
        pass
    if B1 =='FF' and B2 == 'FF':
        # print('广播类型')
        if e[0] =='1' and e[3:8] == '11111':
            # print('地市系统内所有同类型终端广播')
            return ('地市系统内所有同类型终端广播')
        elif e[4:8] in ('区县供电局代码字典'):
            # print('该区县供电局下的所有同类型终端广播')
            return ('该区县供电局下的所有同类型终端广播')
    else:pass


