# -*- coding:utf-8 -*-

import time
import os
import tkinter as tk
from tkinter import messagebox

def asd():
    with open(os.path.join(os.getcwd(), 'a.txt\\activation.txt'), "r+", encoding='UTF-8')as f:
        if f.read() == '12344321':
            messagebox.showinfo('提示','     您已激活      ')
        else:
            q = tk.Tk()
            q.geometry('+760+470')
            tk.Label(q, text="激活码:", fg="black", font=('Times', 12)).pack()
            m = tk.Entry(q, width=20, relief='solid',show='•')
            m.pack()

            def qwe():
                if m.get() == '12344321':
                    with open(os.path.join(os.getcwd(), 'a.txt\\activation.txt'), "r+", encoding='UTF-8')as f:
                        f.seek(0)
                        f.truncate()
                        f.write('12344321')
                        q.destroy()
                        messagebox.showinfo('提示','   激活成功!    ')
                else:
                    messagebox.showwarning('警告','   激活码错误   ')
                    q.destroy()
            tk.Button(q, text="确定", command=qwe).pack()

def dome0():
    a = tk.Tk()
    a.geometry('200x75+750+400')
    tk.Label(a, text="秒后开始\n\n请将光标移至输入框   ", fg="black", font=('Times', 10)).place(x=50, y=20)
    b = 3
    c = tk.Entry(a, width=2)
    c.place(x=70, y=20)
    for s in range(b + 2):
        c.insert(0, b)
        time.sleep(1)
        a.update()
        c.delete(0, tk.END)
        b -= 1
        if b == -1:
            break
    a.destroy()
