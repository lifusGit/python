import tkinter
from tkinter import ttk # 导入ttk模块，下拉菜单控件位于ttk子模块中
import random
# 创建窗口
win = tkinter.Tk()
win.title("commbox insert test")
win.geometry('400x250+800+200')
win.resizable(0,0)
# 创建下拉菜单
cbox = ttk.Combobox(win)
# 使用 grid() 来控制控件的位置
cbox.grid(row = 0, column=0)
# 设置下拉菜单中的值
cbox['value'] = ('input or select','C','C++','Rust','Python','Java')

#通过 current() 设置下拉菜单选项的默认值
cbox.current(0)

# 编写回调函数，绑定执行事件,向文本插入选中文本
def func(event):
    text.insert('insert',cbox.get()+"\n")
# 绑定下拉菜单事件
cbox.bind("<<ComboboxSelected>>",func)

global values
values = []
global values_dic
values_dic = {}
def insert_combobox():
    global values
    global values_dic
    index = 0
    flag = 0
    str_value = cbox.get()
    index_val = 0
    if 0 == len(values):
        values_dic[str_value] = 1
    else:
        for i in values:
            if str_value == i:
                values_dic[i]+=1
                flag = 1
                continue
            if 100 != values_dic[i]:
                values_dic[i]+=1

        if len(values) == 5:
            if flag == 0:
                del values_dic[values[4]]
                values_dic[str_value] = 1
        else:
            if flag == 0:
                values_dic[str_value] = 1

    new_values_tup = sorted(values_dic.items(), key=lambda d: d[1], reverse=False)
    values_dic = dict(new_values_tup)
    values = list(values_dic.keys())
    cbox["value"] = values

button = tkinter.Button(text="insert combobox", command=insert_combobox)
button.grid(row=0, column=1)
# 新建文本框
text = tkinter.Text(win)
# 布局
# text.grid(pady = 5)
# insert_combobox()
#test
# i = 0
# while i < 1000:
#     print(random.randint(1,10))
#     cbox.set(random.randint(1,10))
#     insert_combobox()
#     i+=1
win.mainloop()