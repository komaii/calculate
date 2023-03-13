import tkinter as tk

window = tk.Tk()
window.geometry("410x550")
window.title("電卓")


#数字ボタン機能
def b1_func():
    if display['text'] == '0':
        display['text'] = '1'
    else:
        display['text'] = display['text'] +'1'
def b2_func():
    if display['text'] == '0':
        display['text'] = '2'
    else:
        display['text'] = display['text'] +'2'
def b3_func():
    if display['text'] == '0':
        display['text'] = '3'
    else:
        display['text'] = display['text'] +'3'
def b4_func():
    if display['text'] == '0':
        display['text'] = '4'
    else:
        display['text'] = display['text'] +'4'
def b5_func():
    if display['text'] == '0':
        display['text'] = '5'
    else:
        display['text'] = display['text'] +'5'
def b6_func():
    if display['text'] == '0':
        display['text'] = '6'
    else:
        display['text'] = display['text'] +'6'
def b7_func():
    if display['text'] == '0':
        display['text'] = '7'
    else:
        display['text'] = display['text'] +'7'
def b8_func():
    if display['text'] == '0':
        display['text'] = '8'
    else:
        display['text'] = display['text'] +'8'
def b9_func():
    if display['text'] == '0':
        display['text'] = '9'
    else:
        display['text'] = display['text'] +'9'
def b0_func():
    if display['text'] == '0':
        display['text'] = '0'
    else:
        display['text'] = display['text'] +'0'


#計算ボタン機能
def ac_func():
    display['text'] = ''

def pl_func():
    if display['text'] == '':
        def ac_func():
            display['text'] = '0'
    else:
        display['text'] = display['text'] + '+'

def mi_func():
    if display['text'] == '':
        def ac_func():
            display['text'] = '0'
    else:
        display['text'] = display['text'] + '-'

def mu_func():
    if display['text'] == '':
        def ac_func():
            display['text'] = '0'
    else:
        display['text'] = display['text'] + '*'

def di_func():
    if display['text'] == '':
        def ac_func():
            display['text'] = '0'
    else:
        display['text'] = display['text'] + '/'

def eq_func():
    if display['text'] == '':
        def ac_func():
            display['text'] = '0'
    else:
        exec(display['text'])
        display['text'] = exec(display['text'])
       

#結果表示
display=tk.Label(text='',font=('System',24),background='#F0F8FF')
display.place(x=50,y=40,width=300,height=100)


#ボタン配置
botton0 = tk.Button(window, text= '0',command=b0_func)
botton0.place(x=30,y=440,width=70,height=85)

bottonequal = tk.Button(window, text= '=',command=eq_func)
bottonequal.place(x=120,y=440,width=70,height=85)

bottonac = tk.Button(window, text= 'AC',command=ac_func)
bottonac.place(x=210,y=440,width=70,height=85)

bottonplus = tk.Button(window, text= '+',command=pl_func)
bottonplus.place(x=300,y=440,width=70,height=85)

botton1 = tk.Button(window, text= '1',command=b1_func)
botton1.place(x=30,y=350,width=70,height=85)

botton2 = tk.Button(window, text= '2',command=b2_func)
botton2.place(x=120,y=350,width=70,height=85)

botton3 = tk.Button(window, text= '3',command=b3_func)
botton3.place(x=210,y=350,width=70,height=85)

bottonminus = tk.Button(window, text= '-',command=mi_func)
bottonminus.place(x=300,y=350,width=70,height=85)

botton4 = tk.Button(window, text= '4',command=b4_func)
botton4.place(x=30,y=260,width=70,height=85)

botton5 = tk.Button(window, text= '5',command=b5_func)
botton5.place(x=120,y=260,width=70,height=85)

botton6 = tk.Button(window, text= '6',command=b6_func)
botton6.place(x=210,y=260,width=70,height=85)

bottonmulti = tk.Button(window, text= '*',command=mu_func)
bottonmulti.place(x=300,y=260,width=70,height=85)

botton7 = tk.Button(window, text= '7',command=b7_func)
botton7.place(x=30,y=170,width=70,height=85)

botton8 = tk.Button(window, text= '8',command=b8_func)
botton8.place(x=120,y=170,width=70,height=85)

botton9 = tk.Button(window, text= '9',command=b9_func)
botton9.place(x=210,y=170,width=70,height=85)

bottondived = tk.Button(window, text= '/',command=di_func)
bottondived.place(x=300,y=170,width=70,height=85)



window.mainloop()
