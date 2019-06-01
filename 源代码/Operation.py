<<<<<<< HEAD
from Product import product
from Stock import stock
import tkinter as tk
import time
s = stock()

window = tk.Tk()
window.title('石学舟的元器件仓库')
window.geometry('1000x500')
tk.Label(window, text='输入: (空格作为分割)',font=('',10)).place(x=1, y= 10)


def add(): # 绑定b1，用于添加物品
    text = e.get().split(" ")
    Pname = text[0]
    Pprice = eval(text[1])
    Pnumber =  eval(text[2])
    Pindex = eval(text[3])
    p = product(Pname,Pprice,Pnumber,Pindex)
    s.add(p)
    e.delete('0',tk.END)


def showlist(): # 绑定b2，用于显示清单
    t.delete(1.0, tk.END)
    text1 = s.List_all()
    t.insert('insert',text1)


def dele(): # 绑定b3，用于出库物品
    t.delete(1.0, tk.END)
    text = e.get().split(" ")
    data = text[0]
    mount = eval(text[1])
    text2 = s.dele(data,mount)
    t.insert('insert', text2)
    e.delete('0', tk.END)


def load():
    s.Load_To_Excel()

def read():
    s.Read_Excel()

# 创建输入框entry，用户输入任何内容都显示为*
e = tk.Entry(window,show="",bd=10,width=100)
e.pack()

# 创建一个文本框用于显示
t = tk.Text(window,height=10)
t.pack()

# p = []
# p.append(product(stm32,100,1,10001))
# p.append(product('keil 51',102,3,10002))
# p.append(product('keil 53',102,3,10003))
# for i in p:
#     s.add(i)

b1 = tk.Button(window,
               text="添加物品--\n"
                    "名称，价格，\n数量，序号",
               width=15,height=5,
               command=add)
b1.pack()
b2 = tk.Button(window,
               text="展示清单",
               width=15,height=2,
               command=showlist)
b2.pack()
b3 = tk.Button(window,
               text="出库物品",
               width=15,height=2,
               command=dele)
b3.pack()
b4 = tk.Button(window,
               text="存入数据库",
               width=15,height=2,
               command=load)
b4.pack()
b5 = tk.Button(window,
               text="读取数据库",
               width=15,height=2,
               command=read)
b5.pack()

window.mainloop()
=======
from Product import product
from Stock import stock
import tkinter as tk
import time
s = stock()

window = tk.Tk()
window.title('easy window')
window.geometry('1000x500')
tk.Label(window, text='输入: (空格作为分割)',font=('',10)).place(x=1, y= 10)

def add(): # 绑定b1，用于添加物品
    text = e.get().split(" ")
    Pname = text[0]
    Pprice = eval(text[1])
    Pnumber =  eval(text[2])
    Pindex = eval(text[3])
    p = product(Pname,Pprice,Pnumber,Pindex)
    s.add(p)
    e.delete('0',tk.END)

def showlist(): # 绑定b2，用于显示清单
    t.delete(1.0, tk.END)
    text1 = s.List_all()
    t.insert('insert',text1)

def dele(): # 绑定b3，用于出库物品
    t.delete(1.0, tk.END)
    text = e.get().split(" ")
    data = text[0]
    mount = eval(text[1])
    text2 = s.dele(data,mount)
    t.insert('insert', text2)
    e.delete('0', tk.END)


# 创建输入框entry，用户输入任何内容都显示为*
e = tk.Entry(window,show="",bd=10,width=100)
e.pack()

# 创建一个文本框用于显示
t = tk.Text(window,height=10)
t.pack()

# p = []
# p.append(product(stm32,100,1,10001))
# p.append(product('keil 51',102,3,10002))
# p.append(product('keil 53',102,3,10003))
# for i in p:
#     s.add(i)

b1 = tk.Button(window,
               text="添加物品",
               width=15,height=2,
               command=add)
b1.pack()
b2 = tk.Button(window,
               text="展示清单",
               width=15,height=2,
               command=showlist)
b2.pack()
b3 = tk.Button(window,
               text="出库物品",
               width=15,height=2,
               command=dele)
b3.pack()

window.mainloop()
>>>>>>> 5fe40353c98a751d8986a82087b7b574f0221770
