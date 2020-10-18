from tkinter import *

# Choose the font for your screen resolution
# Best resolution is 1920x1080
# please uncomment the lines for your screen resolution
#1920x1080
font_lvl_1=24
font_lvl_2=19
font_lvl_3=44
font_lvl_4=30
#1680x1050
#font_lvl_1=22
#font_lvl_2=19
#font_lvl_3=44
#font_lvl_4=26
#1600x900
#font_lvl_1=19
#font_lvl_2=19
#font_lvl_3=44
#font_lvl_4=24
#1440x900
#font_lvl_1=18
#font_lvl_2=19
#font_lvl_3=44
#font_lvl_4=22
#1360x768  #1366x768
#font_lvl_1=17
#font_lvl_2=19
#font_lvl_3=44
#font_lvl_4=20
#1280x1024
#font_lvl_1=12
#font_lvl_2=19
#font_lvl_3=44
#font_lvl_4=15
#1280x720
#font_lvl_1=16
#font_lvl_2=19
#font_lvl_3=44
#font_lvl_4=19
#800x600
#font_lvl_1=10
#font_lvl_2=19
#font_lvl_3=44
#font_lvl_4=11





# Global variables
Clock_On="Not Clicked"
Clock_Off="Not Clicked"
Enter="Not Clicked"
Logged_index=""
Login_Password=""
Login_ID=""
new_Employee=[]
delete_Item=" "
item_Quantity=1
string_Number=""
btn_Cash="Not Clicked"
total_price=0
received_Cash=0
given_Change=0
User_name=""

# button, canvas, text heights
btn_Height_1=3
btn_Height_2=6
btn_Height_4=2
cnvs_Height_1=900
txt_Height_1=1
txt_Height_1=25


#Button, canvas, text widths
btn_Width_1=6
btn_Width_2=12
btn_Width_3=13
btn_Width_4=9
btn_Width_5=20
btn_Width_6=41
cnvs_Width_1=1920
txt_Width_1=18
txt_Width_2=35

# colour codes
WHITE='#FFFFFF'
WHITE='#FFFFFF'
GRAY='#D2D2D2'
AZURE='#0976B9'
RED="#FF0000"
BABYBLUE='#CDEAF7'

array_Label={}
array_Canvas={}
array_Button={}
array_Text={}
array_Entry={}
newWindow={}
Item=[]

Single_Argument=20
text_Label_0="Employee Login"
text_Label_1="Password"
text_Label_2="ID     "
text_Label_3="Employee Name   "
text_Label_4="ID              "
text_Label_6="Confirm Password"
text_Label_5="Password        "
text_Label_7=" Qty | Description         | Price "
text_Label_8="                  Total: $"
text_Label_9="   DRINKS   "
text_Label_10="    FOOD    "
text_Label_11="              Total AMOUNT: $"
text_Label_12="           Received AMOUNT: $"
text_Label_13="             Change AMOUNT: $"


text_Itemlist=0
text_Total_Price=1
text_Total_Price2=2
text_Cash_Received=3
text_MoneyChange=4
#first window button numbers
mainWindow_btn_Number0=0
mainWindow_btn_Number9=9
mainWindow_btn_Enter=10
mainWindow_btn_Clear=11
mainWindow_btn_ClockOn=12
mainWindow_btn_ClockOff=13
mainWindow_btn_Register=14
mainWindow_btn_EmptyBox1=15
mainWindow_btn_EmptyBox15=29

#second window button numbers
secondWindow_btn_Number0=30
secondWindow_btn_Number9=39
secondWindow_btn_Enter=40
secondWindow_btn_Clear=41
secondWindow_btn_Items1=42
secondWindow_btn_Items24=66
secondWindow_btn_ChangeClerk=67
secondWindow_btn_CancelSale=68
secondWindow_btn_DeleteItem=69
secondWindow_btn_Cash=70
thirdWindow_btn_PrintReceipt=73
thirdWindow_btn_Ok=74

items = [["Soda Water","Soda\nWater",2,0],              ["Pot Beer","Pot\nBeer",4,0],      ["Garlic Bread","Garlic\nBread",6,0],     ["Schnitzel","Schnit",20,0],
        ["Lemon Squash","Lemon\nSquash",4,0],           ["Schooner Beer","Sch\nBeer",6,0], ["Bowl of Chips","Bowl\nof\nChips",7,0],  ["Fish & Chips","Fish\n&\nChips",18,0],
        ["Coke","Coke",4,0],                            ["Pint Beer","Pint\nBeer",8,0],    ["Squid","Squid",10,0],                   ["Pizza","Pizza",16,0],
        ["Coke Zero","Coke\nZero",4,0],                 ["Red Wine","Red\nWine",7,0],      ["Oyster","Oyster",10,0],                 ["Steak","Steak",24,0],
        ["Lemon Lime Bitter","Lemon\nLime\nBitter",5,0],["White Wine","White\nWine",7,0],  ["Spring Rolls","Spring\nRolls",11,0],    ["Pork Ribs","Pork\nRibs",26,0],
        ["Dry Ginger","Dry\nGinger",4,0],               ["Spirit 30ml","Spirit\n30ml",8,0],["Salad","Salad",14,0],                   ["Veg Curry","Veg\nCurry",21,0]]

#first window button ittems
mW_btn_items =[
    [1,Single_Argument,"1", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.545,'center',AZURE,WHITE,GROOVE],
    [2,Single_Argument,"2", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.545,'center',AZURE,WHITE,GROOVE],
    [3,Single_Argument,"3", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.545,'center',AZURE,WHITE,GROOVE],
    [4,Single_Argument,"4", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.675,'center',AZURE,WHITE,GROOVE],
    [5,Single_Argument,"5", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.675,'center',AZURE,WHITE,GROOVE],
    [7,Single_Argument,"7", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.805,'center',AZURE,WHITE,GROOVE],
    [6,Single_Argument,"6", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.675,'center',AZURE,WHITE,GROOVE],
    [8,Single_Argument,"8", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.805,'center',AZURE,WHITE,GROOVE],
    [9,Single_Argument,"9", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.805,'center',AZURE,WHITE,GROOVE],
    [10,Single_Argument,"Enter", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.935,'center',AZURE,WHITE,GROOVE],
    [0,Single_Argument,"0", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.935,'center',AZURE,WHITE,GROOVE],
    [11,Single_Argument,"Clear", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.935,'center',AZURE,WHITE,GROOVE],
    [12,Single_Argument,"Clock On", btn_Height_1,btn_Width_5,font_lvl_1,0.116,0.935,'center',WHITE,AZURE,GROOVE],
    [13,Single_Argument,"Clock Off", btn_Height_1,btn_Width_5,font_lvl_1,0.324,0.935,'center',WHITE,AZURE,GROOVE],
    [14,Single_Argument,"Register New Employee", btn_Height_1,btn_Width_6,font_lvl_1,0.22,0.805,'center',WHITE,AZURE,GROOVE],
    [15,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.7,0.492,'center',WHITE,AZURE,FLAT],
    [16,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.82,0.492,'center',WHITE,AZURE,FLAT],
    [17,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.94,0.492,'center',WHITE,AZURE,FLAT],
    [18,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.7,0.604,'center',WHITE,AZURE,FLAT],
    [19,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.82,0.604,'center',WHITE,AZURE,FLAT],
    [20,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.94,0.604,'center',WHITE,AZURE,FLAT],
    [21,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.7,0.716,'center',WHITE,AZURE,FLAT],
    [22,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.82,0.716,'center',WHITE,AZURE,FLAT],
    [23,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.94,0.716,'center',WHITE,AZURE,FLAT],
    [24,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.7,0.828,'center',WHITE,AZURE,FLAT],
    [25,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.82,0.828,'center',WHITE,AZURE,FLAT],
    [26,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.94,0.828,'center',WHITE,AZURE,FLAT],
    [27,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.7,0.94,'center',WHITE,AZURE,FLAT],
    [28,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.82,0.94,'center',WHITE,AZURE,FLAT],
    [29,Single_Argument,"", btn_Height_4,btn_Width_4,font_lvl_4,0.94,0.94,'center',WHITE,AZURE,FLAT]
    ]
#second window button numbers
nW_btn_items =[
    [31,Single_Argument,"1", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.465,'center',AZURE,WHITE,GROOVE],
    [32,Single_Argument,"2", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.465,'center',AZURE,WHITE,GROOVE],
    [33,Single_Argument,"3", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.465,'center',AZURE,WHITE,GROOVE],
    [34,Single_Argument,"4", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.595,'center',AZURE,WHITE,GROOVE],
    [35,Single_Argument,"5", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.595,'center',AZURE,WHITE,GROOVE],
    [36,Single_Argument,"6", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.595,'center',AZURE,WHITE,GROOVE],
    [37,Single_Argument,"7", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.725,'center',AZURE,WHITE,GROOVE],
    [38,Single_Argument,"8", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.725,'center',AZURE,WHITE,GROOVE],
    [39,Single_Argument,"9", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.725,'center',AZURE,WHITE,GROOVE],
    [40,Single_Argument,"Enter", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.855,'center',AZURE,WHITE,GROOVE],
    [30,Single_Argument,"0", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.855,'center',AZURE,WHITE,GROOVE],
    [41,Single_Argument,"Clear", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.855,'center',AZURE,WHITE,GROOVE],
    [42,Single_Argument,"Soda\nWater", btn_Height_1,btn_Width_1,font_lvl_1,0.7,0.205,'center',AZURE,WHITE,GROOVE],
    [43,Single_Argument,"Pot\nBeer", btn_Height_1,btn_Width_1,font_lvl_1,0.767,0.205,'center',AZURE,WHITE,GROOVE],
    [44,Single_Argument,"Garlic\nBread", btn_Height_1,btn_Width_1,font_lvl_1,0.850,0.205,'center',AZURE,WHITE,GROOVE],
    [45,Single_Argument,"Schnit", btn_Height_1,btn_Width_1,font_lvl_1,0.917,0.205,'center',AZURE,WHITE,GROOVE],
    [46,Single_Argument,"Lemon\nSquash", btn_Height_1,btn_Width_1,font_lvl_1,0.7,0.335,'center',AZURE,WHITE,GROOVE],
    [47,Single_Argument,"Sch\nBeer", btn_Height_1,btn_Width_1,font_lvl_1,0.767,0.335,'center',AZURE,WHITE,GROOVE],
    [48,Single_Argument,"Bowl\nof\nChips", btn_Height_1,btn_Width_1,font_lvl_1,0.850,0.335,'center',AZURE,WHITE,GROOVE],
    [49,Single_Argument,"Fish\n&\nChips", btn_Height_1,btn_Width_1,font_lvl_1,0.917,0.335,'center',AZURE,WHITE,GROOVE],
    [50,Single_Argument,"Coke", btn_Height_1,btn_Width_1,font_lvl_1,0.7,0.465,'center',AZURE,WHITE,GROOVE],
    [51,Single_Argument,"Pint\nBeer", btn_Height_1,btn_Width_1,font_lvl_1,0.767,0.465,'center',AZURE,WHITE,GROOVE],
    [52,Single_Argument,"Squid", btn_Height_1,btn_Width_1,font_lvl_1,0.850,0.465,'center',AZURE,WHITE,GROOVE],
    [53,Single_Argument,"Pizza", btn_Height_1,btn_Width_1,font_lvl_1,0.917,0.465,'center',AZURE,WHITE,GROOVE],
    [55,Single_Argument,"Coke\nZero", btn_Height_1,btn_Width_1,font_lvl_1,0.7,0.595,'center',AZURE,WHITE,GROOVE],
    [56,Single_Argument,"Red\nWine", btn_Height_1,btn_Width_1,font_lvl_1,0.767,0.595,'center',AZURE,WHITE,GROOVE],
    [57,Single_Argument,"Oyster", btn_Height_1,btn_Width_1,font_lvl_1,0.850,0.595,'center',AZURE,WHITE,GROOVE],
    [58,Single_Argument,"Steak", btn_Height_1,btn_Width_1,font_lvl_1,0.917,0.595,'center',AZURE,WHITE,GROOVE],
    [59,Single_Argument,"Lemon\nLime\nBitter", btn_Height_1,btn_Width_1,font_lvl_1,0.7,0.725,'center',AZURE,WHITE,GROOVE],
    [60,Single_Argument,"White\nWine", btn_Height_1,btn_Width_1,font_lvl_1,0.767,0.725,'center',AZURE,WHITE,GROOVE],
    [61,Single_Argument,"Spring\nRolls", btn_Height_1,btn_Width_1,font_lvl_1,0.850,0.725,'center',AZURE,WHITE,GROOVE],
    [62,Single_Argument,"Pork\nRibs", btn_Height_1,btn_Width_1,font_lvl_1,0.917,0.725,'center',AZURE,WHITE,GROOVE],
    [63,Single_Argument,"Dry\nGinger", btn_Height_1,btn_Width_1,font_lvl_1,0.7,0.855,'center',AZURE,WHITE,GROOVE],
    [64,Single_Argument,"Spirit\n30ml", btn_Height_1,btn_Width_1,font_lvl_1,0.767,0.855,'center',AZURE,WHITE,GROOVE],
    [65,Single_Argument,"Salad", btn_Height_1,btn_Width_1,font_lvl_1,0.850,0.855,'center',AZURE,WHITE,GROOVE],
    [66,Single_Argument,"Veg\nCurry", btn_Height_1,btn_Width_1,font_lvl_1,0.917,0.855,'center',AZURE,WHITE,GROOVE],
    [67,Single_Argument,"Change\nClerk", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.155,'center',AZURE,WHITE,GROOVE],
    [68,Single_Argument,"Cancel\nSale", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.155,'center',AZURE,WHITE,GROOVE],
    [69,Single_Argument,"Delete\nItem", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.155,'center',AZURE,WHITE,GROOVE],
    [70,Single_Argument,"CASH", btn_Height_1,btn_Width_1,font_lvl_1,0.471,0.285,'center',AZURE,WHITE,GROOVE],
    [71,Single_Argument,"EFT", btn_Height_1,btn_Width_1,font_lvl_1,0.538,0.285,'center',AZURE,WHITE,GROOVE],
    [72,Single_Argument,"HOLD\nSALE", btn_Height_1,btn_Width_1,font_lvl_1,0.605,0.285,'center',AZURE,WHITE,GROOVE]
]
