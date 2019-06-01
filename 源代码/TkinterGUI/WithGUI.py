<<<<<<< HEAD
import tkinter as tk

window = tk.Tk()
window.title('easy window')
window.geometry('300x200')


on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set("")


# # 设置文字内容，背景颜色，字体和字体大小，标签长宽
# l = tk.Label(window,
#              text = "OMG,This is tk",
#              bg = 'green',
#              font = ('Arial',12),
#              width=15,height=2)
# # 加载窗口
# l.pack()

var = tk.StringVar()    # 这是文字变量储存器
l = tk.Label(window,
    textvariable = var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

b = tk.Button(window,
              text = 'hit me',
              width=15,height=2,
              command=hit_me)  # 点击按钮所执行的命令
b.pack()

# 开始
window.mainloop()

=======
import tkinter as tk

window = tk.Tk()
window.title('easy window')
window.geometry('300x200')


on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set("")


# # 设置文字内容，背景颜色，字体和字体大小，标签长宽
# l = tk.Label(window,
#              text = "OMG,This is tk",
#              bg = 'green',
#              font = ('Arial',12),
#              width=15,height=2)
# # 加载窗口
# l.pack()

var = tk.StringVar()    # 这是文字变量储存器
l = tk.Label(window,
    textvariable = var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

b = tk.Button(window,
              text = 'hit me',
              width=15,height=2,
              command=hit_me)  # 点击按钮所执行的命令
b.pack()

# 开始
window.mainloop()

>>>>>>> 5fe40353c98a751d8986a82087b7b574f0221770
