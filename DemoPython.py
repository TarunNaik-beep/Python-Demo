from tkinter import *

root = Tk()

root.title("Addition")
root.geometry("400x400")

result = Label(root)

def add():
    answer = 3+6
    result["text"]=answer

btn = Button(root , text="Add" , command = add)

btn.pack()
result.pack()

    

root.mainloop()
