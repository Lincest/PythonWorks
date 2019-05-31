import tkinter as tk

window = tk.Tk()
window.title('Rocco')
window.geometry('200x200')

def print_selection():
    l.config(text='you have selected'+var.get())


var = tk.StringVar()
l = tk.Label(window,
             bg='gray',width=20,
             text='empty')
l.pack()

# 其中variable=var, value='A'的意思就是
# 当我们鼠标选中了其中一个选项，
# 把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window,
                    text='Option A',
                    variable=var,value='A',
                    command=print_selection)
r2 = tk.Radiobutton(window,
                    text='Option B',
                    variable=var,value='B',
                    command=print_selection)
r1.pack()
r2.pack()
window.mainloop()