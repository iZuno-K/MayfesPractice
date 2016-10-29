#-*- coding: utf-8 -*-
import cv2
import numpy as np
# 白い物を透過させよう

if __name__=="__main__":

    cap = cv2.VideoCapture(0)
    thresh = 170 #閾値
    flag = False
    while True:
        ret,frame = cap.read()
        key = cv2.waitKey(10)

        # スぺースキーで現在の画像を保存
        if key == ord(" "):
            background = frame
            flag = True

        # スペースキーが押されたらそれ以降実行
        if flag:
            ------------------------
            -----------------------
        cv2.imshow("Toumei",frame)

        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
