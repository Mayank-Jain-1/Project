from tkinter import *
import mysql.connector as mysql
from PIL import ImageTk, Image as I
import re


def build_connection(hostname, username, password, db):
    try:
        connection = mysql.connect(host=hostname, user=username, passwd=password, database=db)
        return connection
    except:
        raise Exception("Couldn't make the connection")


def valid_email(email):
    pattern = r"^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z0-9]+[.][a-z]{2,3}"
    invalid_pattern = r"[._@]{2}"
    if re.fullmatch(pattern, email) and not re.findall(invalid_pattern, email):
        return True
    else:
        return False


def valid_password(password):
    pattern = r"[0-9]"
    if len(password) >= 8 and password.isalnum() and re.findall(pattern, password):
        return True
    else:
        return False


def create_acc():
    login_page_remove()
    register_page()


def already_acc():
    register_page_remove()
    login_page()


def login_page():
    global username_l, password_l, usernamebox, passwordbox, loginb, create
    username_l = Label(window, text="Username: ", bg="white", font="OpenSans 10 bold", fg="black")
    username_l.place(x=310, y=200)
    password_l = Label(window, text="Password: ", bg="white", font="OpenSans 10 bold", fg="black")
    password_l.place(x=310, y=250)
    usernamebox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    usernamebox.place(x=400, y=200)
    passwordbox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    passwordbox.place(x=400, y=250)

    loginb = Button(window, text="Login", font="Calibri 12 bold", bg="#041045", fg="White",
                    command=lambda: login(usernamebox, passwordbox))
    loginb.place(x=450, y=320)

    create = Button(window, text="Create a new account?", bg="white", fg="#041045", relief=FLAT,
                    command=lambda: create_acc())
    create.place(x=457, y=275)


def login_page_remove():
    global username_l, password_l, usernamebox, passwordbox, loginb, create
    username_l.place_forget()
    password_l.place_forget()
    usernamebox.place_forget()
    passwordbox.place_forget()
    loginb.place_forget()
    create.place_forget()


def login(usernamebox, passwordbox):
    try:
        username = usernamebox.get()
        password = passwordbox.get()
        if not valid_email(username):
            err = Label(window, text="The entered username is not valid", fg="red", bg="White")
            err.place(x=400, y=150)
            err.after(2500, lambda: err.place_forget())
            return
        conn = build_connection("localhost", "root", "23080518", "data")
        cursor = conn.cursor()
        cursor.execute(f" SELECT * from accounts Where email = '{username}'")
        result = cursor.fetchone()
        if not result:
            err = Label(window, text="Account with this username not found", fg="red", bg="White")
            err.place(x=390, y=150)
            err.after(2500, lambda: err.place_forget())
            return
        password1 = result[1]
        cursor.close()
        conn.close()
        if password1 != password:
            err = Label(window, text="Invalid username or password", fg="red", bg="White")
            err.place(x=410, y=150)
            err.after(2500, lambda: err.place_forget())
            return
        login_page_remove()
        display_page(username)
    except Exception as e:
        print(e)
        err = Label(window, text="Invalid username or password", fg="red", bg="White")
        err.place(x=410, y=150)
        err.after(2500, lambda: err.place_forget())


def register_page():
    global username_l, password_l, c_password_l, namel, agel, p_numberl, genderl
    global usernamebox, passwordbox, c_passwordbox, namebox, agebox, p_numberbox, genderbox
    global registerb, already
    username_l = Label(window, text="               Username:", bg="white", justify=RIGHT, fg="black")
    username_l.place(x=280, y=90)
    password_l = Label(window, text="                Password:", bg="white", fg="black")
    password_l.place(x=280, y=130)
    c_password_l = Label(window, text="Confirm Password:", bg="white", fg="black")
    c_password_l.place(x=280, y=170)
    namel = Label(window, text="                      Name:", bg="white", fg="black")
    namel.place(x=280, y=210)
    agel = Label(window, text="                         Age:", bg="white", fg="black")
    agel.place(x=280, y=250)
    p_numberl = Label(window, text="     Phone Number:", bg="white", fg="black")
    p_numberl.place(x=280, y=290)
    genderl = Label(window, text="                   Gender:", bg="white", fg="black")
    genderl.place(x=280, y=330)

    usernamebox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    usernamebox.place(x=400, y=90)
    passwordbox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    passwordbox.place(x=400, y=130)
    c_passwordbox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    c_passwordbox.place(x=400, y=170)
    namebox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    namebox.place(x=400, y=210)
    agebox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    agebox.place(x=400, y=250)
    p_numberbox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    p_numberbox.place(x=400, y=290)
    genderbox = Entry(window, borderwidth=2, relief=GROOVE, width=30)
    genderbox.place(x=400, y=330)

    registerb = Button(window, text="Register", font="Calibri 12 bold", bg="#041045", fg="White",
                       command=lambda: register(usernamebox, passwordbox, c_passwordbox, namebox, agebox, p_numberbox,
                                                genderbox))
    registerb.place(x=450, y=380)
    already = Button(window, text="Already have an account?", bg="white", fg="#041045", relief=FLAT,
                     command=lambda: already_acc())
    already.place(x=440, y=350)


def register_page_remove():
    global username_l, password_l, c_password_l, namel, agel, p_numberl, genderl
    global usernamebox, passwordbox, c_passwordbox, namebox, agebox, p_numberbox, genderbox
    global registerb, already
    username_l.place_forget()
    password_l.place_forget()
    c_password_l.place_forget()
    namel.place_forget()
    agel.place_forget()
    p_numberl.place_forget()
    genderl.place_forget()
    usernamebox.place_forget()
    passwordbox.place_forget()
    c_passwordbox.place_forget()
    namebox.place_forget()
    agebox.place_forget()
    p_numberbox.place_forget()
    genderbox.place_forget()
    registerb.place_forget()
    already.place_forget()


def register(usernamebox, passwordbox, c_passwordbox, namebox, agebox, p_numberbox, genderbox):
    try:
        username = usernamebox.get()
        password = passwordbox.get()
        c_password = c_passwordbox.get()
        name = namebox.get()
        age = agebox.get()
        p_number = p_numberbox.get()
        gender = genderbox.get()
        conn = build_connection("localhost", "root", "23080518", "data")
        cursor = conn.cursor()
        cursor.execute(f" SELECT * from accounts Where email = '{username}'")
        result = cursor.fetchone()
        if not username or not valid_email(username):
            err = Label(window, text="Username is not valid", fg="red", bg="White")
            err.place(x=430, y=60)
            err.after(2500, lambda: err.place_forget())
            return
        if result:
            err = Label(window, text="An account is already linked with this Username", fg="red", bg="White")
            err.place(x=370, y=60)
            err.after(2500, lambda: err.place_forget())
            return
        if not password or not valid_password(password):
            err = Label(window,
                        text="Password can contain only digits and letter\n It must be 8 char long and contain atleast 1 number and 1 alphabet",
                        fg="red", bg="White")
            err.place(x=320, y=50)
            err.after(2500, lambda: err.place_forget())
            return
        if not c_password or password != c_password:
            err = Label(window, text="Passwords doesnt match", fg="red", bg="White")
            err.place(x=430, y=60)
            err.after(2500, lambda: err.place_forget())
            return
        temp = name.replace(" ","")
        if not name or not temp.isalpha():
            err = Label(window, text="Invalid name", fg="red", bg="White")
            err.place(x=430, y=60)
            err.after(2500, lambda: err.place_forget())
            return
        if not age or not age.isdecimal() or int(age) > 150 or int(age) <= 0:
            err = Label(window, text="Invalid Age", fg="red", bg="White")
            err.place(x=430, y=60)
            err.after(2500, lambda: err.place_forget())
            return
        if not p_number or not p_number.isdecimal() or len(p_number) != 10:
            err = Label(window, text="Invalid Phone_Number", fg="red", bg="White")
            err.place(x=430, y=60)
            err.after(2500, lambda: err.place_forget())
            return
        if not gender or gender not in ["male", "female"]:
            err = Label(window, text="GENDER CAN ONLY BE 'male' OR 'female'", fg="red", bg="White")
            err.place(x=370, y=60)
            err.after(2500, lambda: err.place_forget())
            return
        conn = build_connection("localhost", "root", "23080518", "data")
        cursor = conn.cursor()
        cursor.execute(
            f"Insert into accounts values ('{username}' , '{password}' , '{name}', {age} , {p_number} , '{gender}')")
        conn.commit()
        register_page_remove()
        display_page(username)

    except Exception as e:
        print(e)
        err = Label(window, text="Can't register at this moment", fg="red", bg="White")
        err.place(x=410, y=150)
        err.after(2500, lambda: err.place_forget())


def display_page(username):
    global label, nopfp, namel, username_l, agel, p_numberl, genderl
    global usernamet, aget, p_numbert, gendert, logoutb

    conn = build_connection("localhost", "root", "23080518", "data")
    cursor = conn.cursor()
    cursor.execute(f" SELECT * from accounts Where email = '{username}'")
    result = cursor.fetchone()
    email, password, name, age, phone, gender = result

    pfp = I.open(r"pfp.png")
    rpfp = pfp.resize((200, 200))
    pfp = ImageTk.PhotoImage(rpfp)
    label = Label(window, image=pfp, borderwidth=3)
    label.place(x=380, y=150)
    nopfp = Label(window, text="Profile Picture", fg="black")
    nopfp.place(x=440, y=240)

    namel = Label(window, text=name.upper(), background="white", fg="#041045", font="OpenSans 25 bold")
    namel.place(x=400, y=60)

    username_l = Label(window, text="          Username:", bg="white", fg="#041045", font="Calibri 10 bold")
    username_l.place(x=280, y=390)
    agel = Label(window, text="                     Age:", bg="white", fg="#041045", font="Calibri 10 bold")
    agel.place(x=280, y=415)
    p_numberl = Label(window, text="Phone Number:", bg="white", fg="#041045", font="Calibri 10 bold")
    p_numberl.place(x=280, y=440)
    genderl = Label(window, text="              Gender:", bg="white", fg="#041045", font="Calibri 10 bold")
    genderl.place(x=280, y=465)

    usernamet = Label(window, text=email, bg="white")
    usernamet.place(x=380, y=390)
    aget = Label(window, text=age, bg="white")
    aget.place(x=380, y=415)
    p_numbert = Label(window, text=str(int(phone)), bg="white")
    p_numbert.place(x=380, y=440)
    gendert = Label(window, text=gender, bg="white")
    gendert.place(x=380, y=465)

    logoutb = Button(window, text="Logout", font="Calibri 10 bold", bg="#041045",
                     fg="White", command=lambda: logout())
    logoutb.place(x=630, y=20)


def display_page_remove():
    global label, nopfp, namel, username_l, agel, p_numberl, genderl
    global usernamet, aget, p_numbert, gendert, logoutb
    label.place_forget()
    nopfp.place_forget()
    namel.place_forget()
    username_l.place_forget()
    agel.place_forget()
    p_numberl.place_forget()
    genderl.place_forget()
    usernamet.place_forget()
    aget.place_forget()
    p_numbert.place_forget()
    gendert.place_forget()
    logoutb.place_forget()


def logout():
    display_page_remove()
    login_page()


#####################

window = Tk()
window.geometry("700x500")
window.minsize(700, 500)
window.maxsize(700, 500)
window.title("VTOP")
window.config(background="white")
icon = PhotoImage(file=r"logo.png")
window.iconphoto(True, icon)

#############  LEFT BLUE FRAME

frm = Frame(window, bg="#041045", borderwidth=10)
frm.pack(side=LEFT, fill="both")
lbl = Label(frm, text="Welcome\nTo\nVTOP", font="CooperBlack 40 bold", pady=40, padx=5, justify="left",
            foreground="white", bg="#041045").pack()
vitlogo = I.open(r"vitlogo.png")
rvitlogo = vitlogo.resize((170, 170))
vitlogo = ImageTk.PhotoImage(rvitlogo)
label = Label(frm, image=vitlogo, background="#041045", pady=20)
label.pack(side=BOTTOM)

############ DRIVER CODE

login_page()

############ ENDING THE WINDOW
window.mainloop()
