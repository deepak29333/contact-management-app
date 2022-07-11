import mysql.connector
import tkinter as tk
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_demo"
)
mycursor = mydb.cursor()

def storeData(name,mobile_no):
    sql = "INSERT INTO users (name,mobile_no) VALUES (%s, %s)"
    val = (name,mobile_no)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount>0:
        return True
    return False

def DisplayAllNumber():


    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    str="Name    Mobile NO \n"
    for x in myresult:
        str=str+x[1]+"   "+x[2]+"\n"
        
    contacts.set(str)

def searchNumber():
    sNumber=search_number.get()
    sql = "SELECT * FROM users where name=%s or mobile_no=%s"
    adr = (sNumber,sNumber)
    
    mycursor.execute(sql,adr)
    myresult = mycursor.fetchall()
    str="Name    Mobile NO \n"
    contacts.set(str)
    for x in myresult:
        str=str+x[1]+"   "+x[2]+"\n"
    contacts.set(str)

def checkValidation():
   #getting form data
    fname=name.get()
    mobile=mobile_no.get()
    #applying empty validation
    if fname=='' or mobile=='':
        message.set("fill the empty field!!!")
    else:
      if storeData(fname,mobile):
           message.set("Saved successfully")
      else:
       message.set("Please Correct details")
       
def Loginform():
    global login_screen
    login_screen = tk.Tk()
    #Setting title of screen
    login_screen.title("Contact Form")
    #setting height and width of screen
    login_screen.geometry("500x650")
    #declaring variable
    global  message;
    global name
    global contacts
    global mobile_no
    global search_number
    search_number=tk.StringVar()
    name = tk.StringVar()
    mobile_no = tk.StringVar()
    message=tk.StringVar()
    contacts=tk.StringVar()
    
    #Creating layout of login form
    tk.Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Name Label
    tk.Label(login_screen, text="Name * ").place(x=20,y=40)
    #Name textbox
    tk.Entry(login_screen, textvariable=name).place(x=90,y=42)
    #Mobile No Label
    tk.Label(login_screen, text="Mobile No * ").place(x=20,y=80)
    #Mobile No textbox
    tk.Entry(login_screen, textvariable=mobile_no).place(x=90,y=82)
    #Label for displaying login status[success/failed]
    tk.Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    tk.Button(login_screen, text="Save", width=10, height=1, bg="orange",command=checkValidation).place(x=105,y=130)
    tk.Label(login_screen, text="Search").place(x=20,y=160)
    tk.Entry(login_screen,textvariable=search_number).place(x=90,y=160)

    tk.Button(login_screen, text="Search", width=10, height=1, bg="orange",command=searchNumber).place(x=105,y=185)

    # all saved Contacts
    tk.Label(login_screen, text="",textvariable=contacts).place(x=40,y=210)
    DisplayAllNumber()
    login_screen.mainloop()
#calling function Loginform

Loginform()

