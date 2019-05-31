from tkinter import *

choice = 0
choice1 = 0

cashheader = "Null"
manageheader = "Null"

class Demo(object):
    header = "Null"
    def __init__(self,name,prps):
        self.name = name
        self.prps = prps
        self.next = "Null"
    
    @staticmethod 
    def print_content():
        global data 
        global data2 
        
        content = data.get()
        content2 = data2.get()
        
        print ('------------------------------------')
        print ('Name of Customer    : ',content) 
        print ('Purpose of Customer : ',content2) 
        print ('------------------------------------')
        print ()
        print ("Above new customer added ...")
        print ()
        name = content
        prps = content2
        print ("")
        if Demo.header == "Null":
            Demo.header = Demo(name,prps)
        else:
            temp = Demo.header
            while temp.next != "Null":
                temp = temp.next

            newNodel = Demo(name,prps)
            temp.next = newNode

        temp = Demo.header
        if temp.next == "Null":
            print ("")
            print ("|", temp.name ," : ",temp.prps,"|")
            print ("")
        else:         
            print ("")
            while temp.next != "Null":
                print ("|", temp.name ," : ",temp.prps,"|",end='')
                temp = temp.next
            print ("|", temp.name ," : ",temp.prps,"|")        
            print ("")

top = Tk()
top.title('The Main Window')
top.geometry("500x500")
top.resizable(0,0)

data = StringVar() 
data2 = StringVar()

Label(top,text="Name of Customer : ").grid(row=1,sticky=W)
Entry(top,textvariable=data).grid(row=1,column=1)

Label(top,text="PRPS of Customer :").grid(row=2,sticky=W)
Entry(top,textvariable=data2).grid(row=2,column=1)

b1 = Button(top,text="continue",command=Demo.print_content)
b1.grid(row=4,column=1)

b2 = Button (top,text="Quit",command=top.destroy)
b2.grid(row=6,column=1)

top.mainloop()

while choice != "4":
    print("")
    print("1. Enqiry Officer 2. Casiear 3. Manager 4. Exit")
    choice = input("Enter your choice : ")

    if choice == "1":
        print("")
        print("     -----     Welcome Enquiry Officier     -----     ")        
        eopassword = input("Enter your password : ")

        if eopassword == "eo":
            print("")
            temp = Demo.header
            if temp.next == "Null":
                print ("")
                print ("|", temp.name ," : ",temp.prps,"|")
                print ("Please enter where to shift this appointment : ")
                shiftapp = input("1. Cashier 2. Manager ")
                if shiftapp == "1":
                    if cashheader == "Null":
                        cashheader = Demo(temp.name,temp.prps)
                        Demo.header = "Null"
                    else:
                        tempcash = cashheader
                        while tempcash.next != "Null":
                            tempcash = tempcash.next
                        tempcash.next = Demo(temp.name,temp.prps)
    
                elif shiftapp == "2":
                    if manageheader == "Null":
                        manageheader = Demo(temp.name,temp.prps)
                        Demo.header = "Null"
                    else:
                        tempcash = manageheader
                        while tempcash.next != "Null":
                            tempcash = tempcash.next
                        tempcash.next = Demo(temp.name,temp.prps)
                print("")
                print ("The Queue is empty ...")        
                print("")
            elif temp.next.next == "Null":
                print ("")
                print ("|", temp.name ," : ",temp.prps,"|")
                print ("Please enter where to shift this appointment : ")
                shiftapp = input("1. Cashier 2. Manager ")
                if shiftapp == "1":
                    if cashheader == "Null":
                        cashheader = Demo(temp.name,temp.prps)
                        Demo.header = "Null"
                    else:
                        tempcash = cashheader
                        while tempcash.next != "Null":
                            tempcash = tempcash.next
                        tempcash.next = Demo(temp.name,temp.prps)
    
                elif shiftapp == "2":
                    if manageheader == "Null":
                        manageheader = Demo(temp.name,temp.prps)
                        Demo.header = "Null"
                    else:
                        tempcash = manageheader
                        while tempcash.next != "Null":
                            tempcash = tempcash.next
                        tempcash.next = Demo(temp.name,temp.prps)

                temp = temp.next
                print ("")
                print ("|", temp.name ," : ",temp.prps,"|")
                print ("Please enter where to shift this appointment : ")
                shiftapp = input("1. Cashier 2. Manager ")
                if shiftapp == "1":
                    if cashheader == "Null":
                        cashheader = Demo(temp.name,temp.prps)
                        Demo.header = "Null"
                    else:
                        tempcash = cashheader
                        while tempcash.next != "Null":
                            tempcash = tempcash.next
                        tempcash.next = Demo(temp.name,temp.prps)
    
                elif shiftapp == "2":
                    if manageheader == "Null":
                        manageheader = Demo(temp.name,temp.prps)
                        Demo.header = "Null"
                    else:
                        tempcash = manageheader
                        while tempcash.next != "Null":
                            tempcash = tempcash.next
                        tempcash.next = Demo(temp.name,temp.prps)
                print("")
                print ("The Queue is empty ...")        
                print("")
            else:
                temp = Demo.header
                while(temp.next != "Null"):
                    print ("")
                    print ("|", temp.name ," : ",temp.prps,"|")
                    print ("Please enter where to shift this appointment : ")
                    shiftapp = input("1. Cashier 2. Manager ")
                    if shiftapp == "1":
                        if cashheader == "Null":
                            cashheader = Demo(temp.name,temp.prps)
                            Demo.header = "Null"
                        else:
                            tempcash = cashheader
                            while tempcash.next != "Null":
                                tempcash = tempcash.next
                            tempcash.next = Demo(temp.name,temp.prps)
        
                    elif shiftapp == "2":
                        if manageheader == "Null":
                            manageheader = Demo(temp.name,temp.prps)
                            Demo.header = "Null"
                        else:
                            tempcash = manageheader
                            while tempcash.next != "Null":
                                tempcash = tempcash.next
                            tempcash.next = Demo(temp.name,temp.prps)
                    temp = temp.next        
                print ("")
                print ("|", temp.name ," : ",temp.prps,"|")
                print ("Please enter where to shift this appointment : ")
                shiftapp = input("1. Cashier 2. Manager ")
                if shiftapp == "1":
                    if cashheader == "Null":
                        cashheader = Demo(temp.name,temp.prps)
                        Demo.header = "Null"
                    else:
                        tempcash = cashheader
                        while tempcash.next != "Null":
                            tempcash = tempcash.next
                        tempcash.next = Demo(temp.name,temp.prps)
    
                elif shiftapp == "2":
                    if manageheader == "Null":
                        manageheader = Demo(temp.name,temp.prps)
                        Demo.header = "Null"
                    else:
                        tempcash = manageheader
                        while tempcash.next != "Null":
                            tempcash = tempcash.next
                        tempcash.next = Demo(temp.name,temp.prps)
                print(" Queue is empty ...")        
            
    elif choice == "2":
        print("")
        print("     -----     Welcome Cashier     -----     ")        
        copassword = input("Enter your password : ")
        if copassword == "co":
            print("")
            temp = cashheader
            if temp.next == "Null":
                print ("")
                print ("|", temp.name ," : ",temp.prps,"|")
                print ("    -----   Is task completed   -----   ")
                
                chcashier = input(" | When task is comleted press 1 |")

                while temp.next != "Null":
                    print ("|", temp.name ," : ",temp.prps,"|",end='')
                    temp = temp.next
                print ("|", temp.name ," : ",temp.prps,"|")        
                print ("")
                print(" Queue is empty now ... ")
            else:         
                print ("")
                while temp.next != "Null":
                    print ("|", temp.name ," : ",temp.prps,"|",end='')
                    print ("    -----   Is task completed   -----   ")
                    chcashier = input(" | When task is comleted press 1 |")
                    temp = temp.next
                print ("|", temp.name ," : ",temp.prps,"|")        
                print ("    -----   Is task completed   -----   ")
                chcashier = input(" | When task is comleted press 1 |")
                print ("")
                print (" Queue is empty ... ")
        else:
            print(" ******************** Wrong password *************************")     

    elif choice == "3":
        print("")
        print("     -----     Welcome Manager     -----     ")        
        copassword = input("Enter your password : ")
        if copassword == "mo":
            print("")
            temp = manageheader
            if temp.next == "Null":
                print ("")
                print ("|", temp.name ," : ",temp.prps,"|")
                print ("    -----   Is task completed   -----   ")
                
                chcashier = input(" | When task is comleted press 1 |")

                while temp.next != "Null":
                    print ("|", temp.name ," : ",temp.prps,"|",end='')
                    temp = temp.next
                print ("|", temp.name ," : ",temp.prps,"|")        
                print ("")
                print(" Queue is empty now ... ")
            else:         
                print ("")
                while temp.next != "Null":
                    print ("|", temp.name ," : ",temp.prps,"|",end='')
                    print ("    -----   Is task completed   -----   ")
                    chcashier = input(" | When task is comleted press 1 |")
                    temp = temp.next
                print ("|", temp.name ," : ",temp.prps,"|")        
                print ("    -----   Is task completed   -----   ")
                chcashier = input(" | When task is comleted press 1 |")
                print ("")
                print (" Queue is empty ... ")
        else:
            print(" ******************** Wrong password *************************")    
    elif choice == "4":
        print("Thanks for using our application ... ")         


