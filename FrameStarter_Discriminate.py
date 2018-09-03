# -*- coding:utf-8 -*-


# 判断帧头信息是否正确

def framestarter(data):
    if data[0] == '68':
        #print('帧头：正确')
        return ('正确')

    else:
        #print('帧头：错误')
        return ('错误')

