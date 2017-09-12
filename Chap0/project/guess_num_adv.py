"""
程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
用户输入 4 位数进行猜测，程序返回相应提示
用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
用户猜测后，程序返回 A 和 B 的数量
比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
猜对或用完 10 次机会，游戏结束
"""

import random

def compare_posi_value(targ_list=None,gue_list=None):
    a=0
    posi_value_flag=0
    value_flag=0
    while a<len(targ_list):
        #print(targ_list)#for debug
        #print(f"the 第{a}次循环")
        #print(f"gue_list[a]:{gue_list[a]}")# for debug
        #print(type(gue_list[a]))
        #print(f"targ_list[a]:{targ_list[a]}")# for debug
        #print(type(targ_list[a]))
        #print(int(gue_list[a]) == targ_list[a])#for debug
        # 挨个比较位置、数值都相同的情况
        if int(gue_list[a]) == targ_list[a]:#相同数据类型才可比较。
            posi_value_flag+=1
            a+=1
            #print(f"posi_value_flag{posi_value_flag}")
        #计算值相等，但是位置不同的情况
        else:
            #print(f"gue_list[a]{gue_list[a]}")#for debug
            #g_l=[x for x in targ_list if int(gue_list[a])!=x]#生成除位置，值都相等的元素之外剩余数组#
            #print(g_l)#for debug
            if int(gue_list[a]) in targ_list: #判定gue_list[a]是否包含在目标数组中，如果在则，值-flag+1，不管位置。
                a+=1
                value_flag+=1
                #print("运行了第一个else")#for debug
            else:
                a+=1
                #print("运行了最后一个else")#for debug

    print (f"{posi_value_flag}A{value_flag}B")
    return posi_value_flag

#从range(0,9)取出四个不相同的数，组成list类型的数组。
tag_list=random.sample(range(0,9),4)#生成的是list，list元素为int类型。

#判断得到的第一个数组是否是0，如果是则，重新将所取得的数组乱序排列，直到第一个不是0为止。
while tag_list[0]==0:
    random.shuffle(tag_list)

#print(tag_list)# for debug
i=0
j=0
while i<10:
    g=input("Please input a number between 1000~9999:")#input输入的为str类型。
    if g.isdigit() and len(g)==4:#是否全由数字组成，且字符串长度为4
        j=compare_posi_value(tag_list,g)
        print(f"you have {9-i} opptunity left.")
        i+=1
        if j==4:
            print("OK, you got it!")
            break
    else:
        print("Please input a xxxx number!NO other type!\n")
