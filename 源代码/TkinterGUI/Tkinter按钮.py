<<<<<<< HEAD
import tkinter as tk

window = tk.Tk()
window.title('easy window')
window.geometry('300x200')


def insert_point():
    var = e.get()
    t.insert('insert',var)


def insert_end():
    var = e.get()
    t.insert('end',var)


b1 = tk.Button(window,
               text="insert point",
               width=15,height=2,
               command=insert_point)
b1.pack()

b2 = tk.Button(window,
               text="insert end",
               command=insert_end)
b2.pack()

# 创建输入框entry，用户输入任何内容都显示为*
e = tk.Entry(window,show="*")
e.pack()

# 创建一个文本框用于显示
t = tk.Text(window,height=2)
t.pack()

window.mainloop()
=======
import tkinter as tk

window = tk.Tk()
window.title('easy window')
window.geometry('300x200')


def insert_point():
    var = e.get()
    t.insert('insert',var)


def insert_end():
    var = e.get()
    t.insert('end',var)


b1 = tk.Button(window,
               text="insert point",
               width=15,height=2,
               command=insert_point)
b1.pack()

b2 = tk.Button(window,
               text="insert end",
               command=insert_end)
b2.pack()

# 创建输入框entry，用户输入任何内容都显示为*
e = tk.Entry(window,show="*")
e.pack()

# 创建一个文本框用于显示
t = tk.Text(window,height=2)
t.pack()

window.mainloop()
>>>>>>> 5fe40353c98a751d8986a82087b7b574f0221770
