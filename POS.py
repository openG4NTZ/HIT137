from POS_variables import *
from POS_Classes import *
from time import ctime
from tkinter import *
from tkinter import messagebox


## This Function creates second tkinter window to show sales ##
def openNewWindow(name,index):
    global User_name
    newWindow[index] = Toplevel(Tk)
    newWindow[index].title(name)
    newWindow[index].attributes("-fullscreen", True)
    newWindow[index].configure(bg=BABYBLUE)
    User_name=name
    #Create Label on top screen of second window
    new_Label(newWindow[index],6,"User Name: " + name,font_lvl_1,0.523,0.05,'center',AZURE,BABYBLUE,FLAT)
    # Create Text for item list that is purchased
    new_Text(newWindow[index],text_Itemlist,"",txt_Height_1,txt_Width_2,font_lvl_1,0.19,0.5,'center',AZURE,WHITE,GROOVE)
    # Create Text for Total price
    new_Text(newWindow[index],text_Total_Price,"0",1,8,font_lvl_1,0.324,0.95,'center',AZURE,WHITE,GROOVE)

    # labels on second window such as Food,Drink etc
    new_Label(newWindow[index],7,text_Label_7,font_lvl_1,0.19,0.06,'center',WHITE,AZURE,FLAT)
    new_Label(newWindow[index],8,text_Label_8,font_lvl_1,0.146,0.95,'center',WHITE,AZURE,FLAT)
    new_Label(newWindow[index],9,text_Label_9,font_lvl_1,0.733,0.1,'center',WHITE,AZURE,FLAT)
    new_Label(newWindow[index],10,text_Label_10,font_lvl_1,0.882,0.1,'center',WHITE,AZURE,FLAT)

    # this for loop creates new buttons dynamicly
    #  nW_btn_items defined in POS_variables.py
    for i in range(len(nW_btn_items)):
        if nW_btn_items[i][0]==67:
            new_Button(newWindow[index],nW_btn_items[i][0],index,nW_btn_items[i][2],
                       nW_btn_items[i][3],nW_btn_items[i][4],nW_btn_items[i][5],nW_btn_items[i][6],
                       nW_btn_items[i][7],nW_btn_items[i][8],nW_btn_items[i][9],nW_btn_items[i][10],
                       nW_btn_items[i][11])
        else:
            new_Button(newWindow[index],nW_btn_items[i][0],nW_btn_items[i][1],nW_btn_items[i][2],
                       nW_btn_items[i][3],nW_btn_items[i][4],nW_btn_items[i][5],nW_btn_items[i][6],
                       nW_btn_items[i][7],nW_btn_items[i][8],nW_btn_items[i][9],nW_btn_items[i][10],
                       nW_btn_items[i][11])

# This function will be called when any button is clicked
# argument of i sepparetes 74 buttons from each other.
def Button_clicked(i,j):
    global Clock_On
    global Clock_Off
    global Enter
    global Logged_index
    global Login_Password
    global Login_ID
    global delete_Item
    global item_Quantity
    global string_Number
    global btn_Cash
    global total_price
    global received_Cash
    global given_Change
    global User_name

## When nummbers are clicked on main resgisteration page
## it is used for saving password and ID on main page
    if i >= mainWindow_btn_Number0 and i <= mainWindow_btn_Number9:
        # if enter is not cliked start saving numbers on first label
        if Enter=="Not Clicked":
            if array_Label[1]["text"]=="Password":
               array_Label[1]["text"]=""
            array_Label[1]["text"]+="*"
            Login_Password+=str(i)
       # if enter is cliked start saving numbers on second label
        elif Enter=="Clicked":
            if array_Label[2]["text"]=="ID     ":
               array_Label[2]["text"]=""
            array_Label[2]["text"]+="*"
            Login_ID+=str(i)
## When Enter button is clicked on main resgisteration page
    elif i==mainWindow_btn_Enter:
        if Enter=="Not Clicked":
            Enter="Clicked"
        # if Enter second time cliked then user entered both password and #
        # So we can check ID and Password in the class new_Employee
        # if there is a match allow user to Clock on
        else:
            Enter="second_Clicked"
            new_Employee.append(Registeration("",Login_ID,Login_Password,ctime()))
            new_Employee[len(new_Employee)-1].encrypt()
            Login_Password=""
            Login_ID=""
            ## check logged ID and password with registered employees
            for x in range(len(new_Employee)-1):
                Message=new_Employee[x].check(new_Employee[len(new_Employee)-1].ID,new_Employee[len(new_Employee)-1].Password)
                if Message=="ID and Password Matched":
                    ## save logged in user location in the array to Logged_index
                    Logged_index=x
                    messagebox.showinfo("Registeration", "Hi " +new_Employee[x].Name +"\nTo Clock On:\nClick Clock On button, then click one of the empty boxes on the right side"
                                        +"\nTo Clock Off:\nClick Clock Off button, then click the box you logged in")
                    del new_Employee[len(new_Employee)-1]
                    return
            messagebox.showwarning(title="Registeration", message="Login Failed")
## When Cleara button is clicked on main resgisteration page
    elif i==mainWindow_btn_Clear:
        Clock_On="Not clicked"
        Clock_Off="Not clicked"
        Enter="Not Clicked"
        Logged_index=""
        array_Label[1]["text"]="Password"
        array_Label[2]["text"]="ID     "
        Login_Password=""
        Login_ID=""

## When Clock on button is clicked on main resgisteration page
    elif i==mainWindow_btn_ClockOn and Enter=="second_Clicked":
        Clock_On="Clicked"
## When Clock off button is clicked on main resgisteration page
    elif i==mainWindow_btn_ClockOff and Enter=="second_Clicked":
        Clock_Off="Clicked"

## When Register button is clicked on main resgisteration page
    elif i==mainWindow_btn_Register:
        Name=array_Entry[0].get()
        ID=array_Entry[1].get()
        Password=array_Entry[2].get()
        Confim_Password=array_Entry[3].get()
        Warning=False
        ## password doesnt match
        if Password!=Confim_Password:
            messagebox.showwarning(title=None, message="Password did not match")
            Warning=True
        ## password and ID length is not long enough
        if len(Password) <= 3 or len(ID) <= 3:
            messagebox.showwarning(title=None, message="Choose more than 3 characters")
            Warning=True
        ## good password and ID is chooesen
        if Warning==False:
            ## add new employee to new_Employee class
            new_Employee.append(Registeration(Name,ID,Password,ctime()))
            new_Employee[len(new_Employee)-1].encrypt()
            ## check if thre is a same ID in the class
            for x in range(len(new_Employee)-1):
                Message=new_Employee[x].check(new_Employee[len(new_Employee)-1].ID,new_Employee[len(new_Employee)-1].Password)
                if Message=="ID Matched" or Message=="ID and Password Matched":
                    Warning=True
                    messagebox.showwarning(title=None, message="Employee "+new_Employee[x].Name+" Already Registered")
                    # ID is alread registered so delete the registered ID
                    del new_Employee[len(new_Employee)-1]
                    break
        # There is no same ID in the system so keep the class and welcom the user
        if Warning==False:
            messagebox.showinfo(title=None, message="Employee "+new_Employee[len(new_Employee)-1].Name+" Registered\nThank You!")

            # Clear Name,ID,Password
            array_Entry[0].delete(0,END)
            array_Entry[1].delete(0,END)
            array_Entry[2].delete(0,END)
            array_Entry[3].delete(0,END)


## When one of the empty boxes are clicked on main resgisteration page
    elif i >= mainWindow_btn_EmptyBox1 and i <= mainWindow_btn_EmptyBox15:
        ## if Logged_index which hold index of the logged employee index on the new_Employee class is not empty
        if Logged_index!="":
            # if Clock off cliked then delete employee name from the box and save clock off time in the class
            if Clock_Off=="Clicked" and array_Button[i]["text"]==new_Employee[Logged_index].Name:
                new_Employee[Logged_index].Clock_Off()
                array_Button[i]["text"]=""

            # if Clock off cliked then write employee name on the box and save clock on time in the class
            elif Clock_On=="Clicked" and array_Button[i]["text"]=="":
                if new_Employee[Logged_index].Clock=="Clocked On":
                    messagebox.showwarning(title=None, message="Employee already clocked on.")
                    Button_clicked(11,0)
                    return
                else:
                    array_Button[i]["text"]=new_Employee[Logged_index].Name
                    new_Employee[Logged_index].Clock_On()
                    new_Employee[Logged_index].set_Button_index(i)
            Button_clicked(11,0)
        # if the box does not have any name on it
        elif array_Button[i]["text"]!="":
            #check if employee already put their name one of the boxes
            for x in range(len(new_Employee)):
                if i==new_Employee[x].get_Button_index():
                    if Cipher(Encrypt_phrase=Login_Password,Decrypt_phrase=NONE).encrypt()==new_Employee[x].Password:
                        Button_clicked(11,0)
                        Tk.iconify()
                        openNewWindow(new_Employee[x].Name,i)
                    else:
                        messagebox.showwarning(title=None, message="Enter Your Password and Try Again")
    ## When nummbers are clicked on second window page
    ## it is used for multiplying item quatitiy
    elif i>=secondWindow_btn_Number0 and i<=secondWindow_btn_Number9:
        number=i%30
        string_Number+=str(number)
        item_Quantity=int(string_Number)
    ## When Enter button is clicked on second window page
    # it is used forrecording received customer money
    elif i==secondWindow_btn_Enter:
        #if enter  is cliked while cash was clicked the it is recording cash value
        if btn_Cash=="Clicked":
            received_Cash=int(string_Number)
            array_Text[text_Cash_Received].configure(state=NORMAL)
            array_Text[text_Cash_Received].delete('1.0', END)
            array_Text[text_Cash_Received].insert(END, received_Cash)
            array_Text[text_Cash_Received].configure(state=DISABLED)
            total_Amount=int(array_Text[text_Total_Price].get("1.0",END))
            given_Change=received_Cash-total_Amount
            array_Text[text_MoneyChange].configure(state=NORMAL)
            array_Text[text_MoneyChange].delete('1.0', END)
            array_Text[text_MoneyChange].insert(END, given_Change)
            if given_Change<0:
                array_Text[text_MoneyChange].configure(fg=WHITE,background=RED)
            array_Text[text_MoneyChange].configure(state=DISABLED)
            string_Number=""
            item_Quantity=1
    ## When Clear button is clicked on second window page
    elif i==secondWindow_btn_Clear:
        string_Number=""
        item_Quantity=1
        if btn_Cash=="Clicked":
            array_Text[text_Cash_Received].configure(state=NORMAL)
            array_Text[text_Cash_Received].delete('1.0', END)
            array_Text[text_Cash_Received].configure(state=DISABLED)
            array_Text[text_MoneyChange].configure(state=NORMAL)
            array_Text[text_MoneyChange].delete('1.0', END)
            array_Text[text_MoneyChange].configure(fg=AZURE,background=WHITE)
            array_Text[text_MoneyChange].configure(state=DISABLED)
            received_Cash=0
            given_Change=0

    ## When any items are clicked such as beer,coke, chips on second window page
    ## it used for calculating total price and putting items on list
    ## adjustsments are done to make it look all items on the smae line
    elif  i>=secondWindow_btn_Items1 and i<=secondWindow_btn_Items24:
        for x in range(len(Item)):
            # firs find item in item clas list
            if Item[x].Btn_Description==array_Button[i]["text"]:
                #second adjust the gaps to fit in the text box on the screen such as " Qty | Description         | Price "
                adjustment_1=delete_Item + str(item_Quantity)
                while len(adjustment_1)<7:
                    adjustment_1+=" "
                adjustment_2=""
                while len(Item[x].Description+adjustment_2)<20:
                    adjustment_2+=" "
                adjustment_2+=delete_Item+"$"

                string=adjustment_1+Item[x].Description+adjustment_2+str(item_Quantity*Item[x].Price) +"\n"

                array_Text[text_Itemlist].configure(state=NORMAL)
                array_Text[text_Itemlist].insert(END,string)
                array_Text[text_Itemlist].configure(state=DISABLED)

                array_Text[text_Total_Price].configure(state=NORMAL)
                previous_price=array_Text[text_Total_Price].get("1.0",END)
                array_Text[text_Total_Price].delete('1.0', END)
                # if delete button cliked put negative sign on the total price
                if delete_Item==" ":
                    array_Text[text_Total_Price].insert(END, str(int(previous_price)+item_Quantity*Item[x].Price))
                else:
                    array_Text[text_Total_Price].insert(END, str(int(previous_price)-item_Quantity*Item[x].Price))
                array_Text[text_Total_Price].configure(state=DISABLED)
        string_Number=""
        item_Quantity=1
    # if change clerk is cliked then kill the class and return to rehisteration page
    elif i == secondWindow_btn_ChangeClerk:
        newWindow[j].destroy()
        Tk.deiconify()
    # if cancel sale button is cliked on the second page
    elif  i==secondWindow_btn_CancelSale:
        array_Text[text_Itemlist].configure(state=NORMAL)
        array_Text[text_Itemlist].delete('1.0', END)
        array_Text[text_Itemlist].configure(state=DISABLED)
        array_Text[text_Total_Price].configure(state=NORMAL)
        array_Text[text_Total_Price].delete('1.0', END)
        array_Text[text_Total_Price].insert(END,"0")
        array_Text[text_Total_Price].configure(state=DISABLED)

    # if delete item is cliked on the secondpage
    # it deletes items from the list
    elif  i==secondWindow_btn_DeleteItem:
        if delete_Item==" ":
            delete_Item="-"
            array_Button[i].configure(fg=WHITE,bg=RED)
        else:
            delete_Item=" "
            array_Button[i].configure(fg=AZURE,bg=WHITE)
    # cash button is cliked create a third window.
    elif  i==secondWindow_btn_Cash:
        try:
            newWindow[16].configure(bg=WHITE)
        except :
            btn_Cash="Clicked"
            newWindow[16] = Toplevel(Tk)
            newWindow[16].title("CASH PAYMENT")
            newWindow[16].geometry('600x400')
            newWindow[16].configure(bg=WHITE)
            total_Amount=array_Text[1].get("1.0",END)
            new_Label(newWindow[16],11,"CASH PAYMENT",font_lvl_1,0.523,0.05,'center',AZURE,WHITE,FLAT)
            new_Button(newWindow[16],73,Single_Argument,"PRINT\nRECEIPT", btn_Height_1,btn_Width_4,font_lvl_1,0.8,0.3,'center',AZURE,WHITE,GROOVE)
            new_Button(newWindow[16],74,Single_Argument,"OK", btn_Height_1,btn_Width_4,font_lvl_1,0.8,0.7,'center',AZURE,WHITE,GROOVE)
            new_Label(newWindow[16],12,"TOTAL AMOUNT    $:",font_lvl_2,0.25,0.2,'center',AZURE,WHITE,FLAT)
            new_Text(newWindow[16],2,"0",1,8,font_lvl_2,0.13,0.32,'center',AZURE,WHITE,GROOVE)
            new_Label(newWindow[16],13,"RECEIVED AMOUNT $:",font_lvl_2,0.25,0.45,'center',AZURE,WHITE,FLAT)
            new_Text(newWindow[16],3,"0",1,8,font_lvl_2,0.13,0.57,'center',AZURE,WHITE,GROOVE)
            new_Label(newWindow[16],14,"CHANGE          $:",font_lvl_2,0.25,0.7,'center',AZURE,WHITE,FLAT)
            new_Text(newWindow[16],4,"0",1,8,font_lvl_2,0.13,0.82,'center',AZURE,WHITE,GROOVE)
            total_price=total_Amount
            array_Text[text_Total_Price2].configure(state=NORMAL)
            array_Text[text_Total_Price2].delete('1.0', END)
            array_Text[text_Total_Price2].insert(END, total_Amount)
            array_Text[text_Total_Price2].configure(state=DISABLED)
    # save the item list,date, user, total price, change in text
    elif  i==thirdWindow_btn_PrintReceipt:
        receipt=array_Text[0].get("1.0",END)
        f= open("receipt.txt","w+")
        f.write(text_Label_7+"\n")
        f.write(receipt+"\n")
        f.write(text_Label_11+str(total_price)+"\n")
        f.write(text_Label_12+str(received_Cash)+"\n")
        f.write(text_Label_13+str(given_Change)+"\n")
        f.write("Clerk:"+User_name + "\n")
        f.write("Transection Time:"+ ctime()+"\n")
        messagebox.showinfo(title=None, message="receipt.txt is created")
    # if button ok is cliked on third page kill the class return to second page
    elif  i==thirdWindow_btn_Ok:
        btn_Cash="Not Clicked"
        total_price=0
        received_Cash=0
        given_Change=0
        Button_clicked(68,0)
        newWindow[16].destroy()

#To create labes dynamicly
def new_Label(root,i,text,font,x,y,location,color_fg,color_bg,relif):
    array_Label[i] = Label(root,text=text,fg=color_fg,background = color_bg)
    array_Label[i].config(font=("Courier New", font), relief = relif)
    array_Label[i].place(relx = x, rely = y, anchor = location)

#To create buttons dynamicly
def new_Button(root,i,j,text,selfHeight,selfWidth,font,x,y,location,color_fg,color_bg,relief_type):
    array_Button[i] = Button(root, text=text,command=lambda: Button_clicked(i,j), height = selfHeight, width = selfWidth)
    array_Button[i].configure( font=("Courier New", font),fg=color_fg,background = color_bg, relief = relief_type)
    array_Button[i].place(relx = x, rely = y, anchor = location)

#To create canvas dynamicly
def new_Canvas(root,i,selfHeight,selfWidth,x,y,color,relief_type):
    array_Canvas[i] = Canvas(root, background = color, width = selfWidth, height = selfHeight,relief = relief_type)
    array_Canvas[i].place(relx = x, rely = y)

#To create text dynamicly
def new_Text(root,i,text,selfHeight,selfWidth,font,x,y,location,color_fg,color_bg,relief_type):
    array_Text[i] = Text(root,height = selfHeight, width = selfWidth)
    array_Text[i].configure( font=("Courier New", font),state=NORMAL,fg=color_fg,background = color_bg, relief = relief_type)
    array_Text[i].place(relx = x, rely = y, anchor = location)
    array_Text[i].insert(END, text)

#To create entry dynamicly
def new_Entry(root,i,text,visibility,font,x,y,location,color_fg,color_bg,relief_type):
    array_Entry[i] = Entry(root)
    array_Entry[i].configure( font=("Courier New", font),show=visibility,fg=color_fg,background = color_bg, relief = relief_type)
    array_Entry[i].place(relx = x, rely = y, anchor = location)
    array_Entry[i].insert(END, text)



## define Tk class
Tk = Tk()
Tk.title("POS")
Tk.attributes("-fullscreen", True)
Tk.configure(bg=WHITE)


new_Canvas(Tk,0, cnvs_Height_1,cnvs_Width_1,0.00,0.39,BABYBLUE,FLAT)
## create "Employee Login" label
new_Label(Tk,0,text_Label_0,font_lvl_3,0.5,0.1,'center',AZURE,WHITE,FLAT)
## create "Password" label
new_Label(Tk,1,text_Label_1,font_lvl_4,0.49,0.46,'center',WHITE,AZURE,SUNKEN)
## create "ID" label
new_Label(Tk,2,text_Label_2,font_lvl_4,0.592,0.46,'center',WHITE,AZURE,SUNKEN)
## create "Employee Name  " label
new_Label(Tk,3,text_Label_3,font_lvl_1,0.176,0.42,'e',AZURE,BABYBLUE,FLAT)
## create "ID  " label
new_Label(Tk,4,text_Label_4,font_lvl_1,0.176,0.50,'e',AZURE,BABYBLUE,FLAT)
## create "Password  " label
new_Label(Tk,5,text_Label_5,font_lvl_1,0.176,0.58,'e',AZURE,BABYBLUE,FLAT)
## create "Confirm Password  " label
new_Label(Tk,6,text_Label_6,font_lvl_1,0.176,0.66,'e',AZURE,BABYBLUE,FLAT)

# entries for ID,name,password and confirm password
new_Entry(Tk,0,"", "", font_lvl_1,0.115,0.46,'center',AZURE,WHITE,GROOVE)
new_Entry(Tk,1,"", "*",font_lvl_1,0.115,0.54,'center',AZURE,WHITE,GROOVE)
new_Entry(Tk,2,"", "*", font_lvl_1,0.115,0.62,'center',AZURE,WHITE,GROOVE)
new_Entry(Tk,3,"", "*", font_lvl_1,0.115 ,0.7,'center',AZURE,WHITE,GROOVE)

# create new buttons on the main page dynamicly
# mW_btn_items is defined in POS_variables
for i in range(len(mW_btn_items)):
    new_Button(Tk,mW_btn_items[i][0],mW_btn_items[i][1],mW_btn_items[i][2],
               mW_btn_items[i][3],mW_btn_items[i][4],mW_btn_items[i][5],mW_btn_items[i][6],
               mW_btn_items[i][7],mW_btn_items[i][8],mW_btn_items[i][9],mW_btn_items[i][10],
               nW_btn_items[i][11])
# create new items for sale such as coke,soda water, pizza
# items is defined in POS_variables
for i in range(len(items)):
    Item.append(new_Item(items[i][0],items[i][1],items[i][2],0))

Tk.mainloop()
