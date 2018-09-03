# -*- coding:utf-8 -*-

# 判断结束符信息是否正确

def terminator(data):
    if data[-1] == '16':
        # print('结束符：正确')
        return ('正确')

    else:
        # print('结束符：错误')
        return ('错误')