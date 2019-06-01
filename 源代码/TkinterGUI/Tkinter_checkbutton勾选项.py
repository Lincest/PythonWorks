<<<<<<< HEAD
import tkinter as tk
window=tk.Tk()
window.title('Rocco')
window.geometry('200x200')

var = tk.StringVar()    # 这是文字变量储存器
l = tk.Label(window,
 #   textvariable = var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='gray', font=('Arial', 12), width=15, height=2)
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             #如果两个选项都选中


var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
var2 = tk.IntVar()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()

window.mainloop()

=======
import tkinter as tk
window=tk.Tk()
window.title('Rocco')
window.geometry('200x200')

var = tk.StringVar()    # 这是文字变量储存器
l = tk.Label(window,
 #   textvariable = var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='gray', font=('Arial', 12), width=15, height=2)
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             #如果两个选项都选中


var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
var2 = tk.IntVar()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()

window.mainloop()

>>>>>>> 5fe40353c98a751d8986a82087b7b574f0221770
