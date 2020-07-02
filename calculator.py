import tkinter as tk

value =''
def inp(n):  
    global value
    value += str(n)  
    var.set(value)

root=tk.Tk()
var = tk.StringVar()
root.geometry('180x242')
root.title('calculator_v_0.1')
root.configure(background='black')

def clear():
    global value
    value = ''
    var.set('')

def final():
    equal =var.get()
    var.set(eval(equal))
def prev():
    global value
    value = value[:-1]
    var.set(value)
    
Input = tk.Entry(root,relief=tk.RIDGE,textvar=var,width = 25,bd =10)
Input.grid(row=0,column=0,columnspan=4)

def buttons():
    button1 = tk.Button(root,text='1',height=2,width=5,command = lambda: inp(1))
    button1.grid(row=1,column=0)
    
    button2 = tk.Button(root,text='2',height=2,width=5,command = lambda: inp(2))
    button2.grid(row=1,column=1)
    
    button3 = tk.Button(root,text='3',height=2,width=5,command = lambda: inp(3))
    button3.grid(row=1,column=2)
    
    clr = tk.Button(root,text='clear',height=2,width=5,command = clear)
    clr.grid(row=5,column=3)
    
    button4 = tk.Button(root,text='4',height=2,width=5,command = lambda: inp(4))
    button4.grid(row=2,column=0)
    
    button5 = tk.Button(root,text='5',height=2,width=5,command = lambda: inp(5))
    button5.grid(row=2,column=1)
    
    button6 = tk.Button(root,text='6',height=2,width=5,command = lambda: inp(6))
    button6.grid(row=2,column=2)
    
    add = tk.Button(root,text='+',height=2,width=5,command = lambda: inp('+'))
    add.grid(row=1,column=3)
    
    button7 = tk.Button(root,text='7',height=2,width=5,command = lambda: inp(7))
    button7.grid(row=3,column=0)
    
    button8 = tk.Button(root,text='8',height=2,width=5,command = lambda: inp(8))
    button8.grid(row=3,column=1)
    
    button9 = tk.Button(root,text='9',height=2,width=5,command = lambda: inp(9))
    button9.grid(row=3,column=2)
                    
    mins = tk.Button(root,text='-',height=2,width=5,command = lambda: inp('-'))
    mins.grid(row=2,column=3)
    
    button0 = tk.Button(root,text='0',height=2,width=5,command = lambda: inp('0'))
    button0.grid(row=4,column=1)

    button00 = tk.Button(root,text ='00',height=2,width=5,command = lambda: inp('00'))
    button00.grid(row=4,column=0)
    
    point = tk.Button(root,text='.',height=2,width=5,command = lambda: inp('.'))
    point.grid(row=4,column=2)
    
                     
    mul = tk.Button(root,text='*',height=2,width=5,command = lambda: inp('*'))
    mul.grid(row=3,column=3)
   

    div = tk.Button(root,text='/',height=2,width=5,command = lambda: inp('/'))
    div.grid(row=4,column=3)
    
    result = tk.Button(root,text='=',height=2,width=11,command = final)
    result.grid(row=5,column=0,columnspan=2)

    back = tk.Button(root,text = 'back',height=2,width=5,command = prev)
    back.grid(row=5,column=2)
root.iconbitmap(bitmap = r"C:\Users\User\Desktop\training\tkinter_apps\accessories_calculator.ico")
buttons()


root.mainloop()
