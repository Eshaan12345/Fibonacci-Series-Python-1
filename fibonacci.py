#while loop and fibonacci

from tkinter import *

root = Tk()




root.title("This is Fibonacci")
root.geometry("400x400")





label_series = Label(root, text="Fibonacci series: ")
label_sum = Label(root, text="Fibonacci sum: ")
text_box = Entry(root, text="Enter maximum value to generate to")
listnum = []


#def command is used to create a function
#every function ends with a colon:
    
def funFibonacci():
    max = int(text_box.get())
    firstno = 0 
    secondno = 1
    sum_ = 0
    
    
    counter = 1 #used for counting in while loop
    
    while (counter <= max):
        if(sum_ != 0):
            listnum.append(sum_)
        label_series["text"] += str(sum_) + " ----"
        
        counter = counter + 1
        firstno = secondno
        secondno = sum_
        sum_ = firstno + secondno
        
        
    label_sum["text"]+= str(sum(listnum))   
       
        
# i'm outside the function


btn = Button(root, text="Show answer", command=funFibonacci)
btn.pack()



text_box.pack()
label_series.pack()
label_sum.pack()
root.mainloop()