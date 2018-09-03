# -*- coding:utf-8 -*-

def slicing(data):
    d = len(data)
    tag0 = data[0:2]
    tag1 = data[2:10]
    tag2 = data[10:14]
    tag3 = data[14:16]
    tag4 = data[16:18]
    tag5 = data[18:22]
    tag6 = data[22:(d-4)]
    tag7 = data[-4:-2]
    tag8 = data[-2:]
    # print('按数据结构划分：''帧起始符：{0}，集中器逻辑地址：{1}，主站地址与命令序号：{2}，'
    #       '帧起始符：{3}，控制码C：{4}，数据长度L：{5}，'
    #       '数据内容DATA：{6}，校验CS：{7}，帧尾:{8}'.format(tag0,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8))

    return (tag0,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8)


