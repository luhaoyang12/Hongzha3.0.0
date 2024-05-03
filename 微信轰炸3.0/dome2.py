# -*- coding:utf-8 -*-

import tkinter as tk
import os
import dome1
import main

def sss():
    r = tk.Tk()
    def qAq():
        r.destroy()
        main.main()
    r.title("更多")
    r.geometry('300x150+700+400')
    text = tk.Label(r, text="微信自动发送\n设置", fg="black", font=('conslas', 20))
    text.pack()
    tk.Button(r, text="   bilibili   ", command=bilibili).place(x=50, y=100)
    tk.Button(r, text='   激活   ', command=l).place(x=170, y=60)
    tk.Button(r, text='查看源代码', command=code).place(x=50, y=60)
    tk.Button(r, text=' github ', command=github).place(x=170, y=100)
    tk.Button(r, text="←", command=qAq).place(x=0, y=0)
    r.mainloop()

def github():
    os.system('start https://github.com/luhaoyang12')
def l():
    dome1.asd()
def code():
    os.startfile(os.path.join(os.getcwd(), 'a.txt\\code.txt'))
def bilibili():
    os.system('start https://space.bilibili.com/3546557691464607?spm_id_from=333.1007.0.0')
