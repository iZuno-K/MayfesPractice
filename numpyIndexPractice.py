#-coding:utf-8-*-
# numpy流のインデックス指定を覚えよう

import numpy as np

if __name__=='__main__':

    a = np.array([1,0,1])
    b = np.array([1,2,3])
    c = []
    # aの中身が1のところの要素だけ取り出そう
    for i in range(len(a)):
        if a[i] == 1:
            c.append(b[i])

    print c
    print type(c)
    # numpy表記
    d = b[a==1]
    print d
    print type(d)
