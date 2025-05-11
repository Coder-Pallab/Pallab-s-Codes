# Sign up interface for student management software

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
root = Tk()
root.geometry("700x400+450+200")
root.title("Sign-up")
root.config (bg = "#63F2E7")
root.resizable (0, 0)

def connect ():
    if (username_entry.get() == "" and "Username" or contact_entry.get() == "" and "Contact No" or pass_entry.get() == "" and "Password"):
          messagebox.showerror ("Error", "All fields are required")
    elif (cpass_entry.get() != pass_entry.get()):
          messagebox.showerror ("Error", "Please enter the password again")
    elif (checkbox.get() == 0):
          messagebox.showerror ("Error", "Please agree the terms and conditions")
    else:
        try:
            connection = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "pallab@123", database = "school")
            my_cursor = connection.cursor ()
            my_cursor.execute ("insert into signup_info values (%s,%s,%s,%s)",(username_entry.get (),pass_entry.get(),cpass_entry.get(), contact_entry.get()))

            connection.commit()
            connection.close()
            messagebox.showinfo ("Succesfull", "You are succesfully registered..", parent = root)
            root.destroy()
            import Login
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent = root)


# Inserting image --------------------------------------------------------------------

log_image = Image.open (r"Python_Programming\School management software\17.png")
log_image = log_image.resize ((300,250), Image.Resampling.LANCZOS)
log1 = ImageTk.PhotoImage (log_image)

label = Label (root, image = log1, bg = "#63F2E7")
label.place (x = 30, y = 90, width = 300, height = 250)

        
# Making frame --------------------------------------------------------------------

frame1 = Frame (root, borderwidth = 0, bg = "#63F2E7", relief = RIDGE)
frame1.place (x = 350, y = 20, width = 300, height = 350)


sign_label = Label (frame1, text = "CREATE AN ACCOUNT", bg = "#63F2E7", fg = "#EF5564", font = ("Microsoft YaHei UI Bold", 17))
sign_label.place (x = 15, y = 10)

# email = Label (frame1, text = "E-Mail...", bg = "#63F2E7", fg = "#EF5564", font = ("Microsoft YaHei UI Bold", 9, "bold"))
# email.place (x = 15, y = 55)

# Making Email entry
def on_enter (e):
        username_entry.delete (0, "end")
        
def on_leave (e):
        name = username_entry.get()
        if name == "":
            username_entry.insert (0, "Username")

usernameVar = StringVar ()
username_entry= Entry (frame1, textvariable = usernameVar, bg = "#63F2E7", fg = "#02020C", font = ("Microsoft YaHei UI Bold", 10), bd = 0)
username_entry.place (x = 20, y = 80, width = 250, height = 20)
username_entry.insert (0, "Username")
username_entry.bind ("<FocusIn>", on_enter)
username_entry.bind ("<FocusOut>", on_leave)
Frame (frame1, bg = "black").place (x = 20, y = 100, width = 250, height = 2)

# Making contact entry
def on_enter (e):
        contact_entry.delete (0, "end")
        
def on_leave (e):
        name = contact_entry.get()
        if name == "":
            contact_entry.insert (0, "Contact No")

contactVar = StringVar()
contact_entry = Entry (frame1, textvariable = contactVar, bg = "#63F2E7", fg = "#02020C", font = ("Microsoft YaHei UI Bold", 10), bd = 0)
contact_entry.place (x = 20, y = 120, width = 250, height = 20)
contact_entry.insert (0, "Contact No")
contact_entry.bind ("<FocusIn>", on_enter)
contact_entry.bind ("<FocusOut>", on_leave)
Frame (frame1, bg = "black").place (x = 20, y = 140, width = 250, height = 2)

# Making Password entry
def on_enter (e):
        pass_entry.delete (0, "end")
        
def on_leave (e):
        name = pass_entry.get()
        if name == "":
            pass_entry.insert (0, "Password")

passVar = StringVar()
pass_entry = Entry (frame1, textvariable = passVar, bg = "#63F2E7", fg = "#02020C", font = ("Microsoft YaHei UI Bold", 10), bd = 0)
pass_entry.place (x = 20, y = 160, width = 250, height = 20)
pass_entry.insert (0, "Password")
pass_entry.bind ("<FocusIn>", on_enter)
pass_entry.bind ("<FocusOut>", on_leave)
Frame (frame1, bg = "black").place (x = 20, y = 180, width = 250, height = 2)

# Making confirm Password entry
def on_enter (e):
        cpass_entry.delete (0, "end")
        
def on_leave (e):
        name = cpass_entry.get()
        if name == "":
            cpass_entry.insert (0, "Confirm Password")

cpassVar = StringVar()
cpass_entry = Entry (frame1, textvariable = cpassVar, bg = "#63F2E7", fg = "#02020C", font = ("Microsoft YaHei UI Bold", 10), bd = 0)
cpass_entry.place (x = 20, y = 200, width = 250, height = 20)
cpass_entry.insert (0, "Confirm Password")
cpass_entry.bind ("<FocusIn>", on_enter)
cpass_entry.bind ("<FocusOut>", on_leave)
Frame (frame1, bg = "black").place (x = 20, y = 220, width = 250, height = 2)

# Making checkbox 

checkbox = IntVar()
check = Checkbutton (frame1, variable = checkbox, text = "I agree the terms and conditions.. ", bg = "#63F2E7", fg = "#02020C", font = ("Microsoft YaHei UI Bold", 10), bd = 0, activebackground = "#63F2E7")
check.place (x = 20, y = 230)

# Making sign up Button

# def connect ():
    # if usernameVar == "" or "Username" and contactVar == "" or "Contact No" and passVar == "" or "Password":
        # messagebox.showerror ("Error", "All fields are required")
    # elif cpassVar != passVar and "Confirm Password":
        # messagebox.showerror ("Error", "Please enter the password again")
    # else:
        # messagebox.showinfo ("Sign up", "You are succesfully registered")
       


signup_btn = Button (frame1, text = "Sign up", bg = "#57a1f8", fg = "white", font = ("Microsoft YaHei UI Bold", 9, "bold"), bd = 0, relief = SUNKEN, cursor = "hand2", padx = 20, activebackground = "#63F2E7", command = connect)
signup_btn.place (x = 70, y = 270, width = 150, height = 30)

# Making Don't have an account and log in button

dont = Label (frame1, text = "Already have an account?", bg = "#63F2E7", fg = "black", font = ("Microsoft YaHei UI Bold", 9), bd = 0)
dont.place (x = 40, y = 320)

# Importing Login page
def log ():
       root.destroy()
       import Login

login_btn = Button (frame1, text = "Log-in", bg = "#63F2E7", fg = "#EF5564", font = ("Microsoft YaHei UI Bold", 9, "bold"), bd = 0, cursor = "hand2", activebackground = "#63F2E7", command = log)
login_btn.place (x = 200, y = 317)




root.mainloop()