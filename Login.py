# Login interface for student management software

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("700x400+450+200")
root.title("Login")
root.config (bg = "#63F2E7")
root.resizable (0, 0)

# Inserting image --------------------------------------------------------------------

log_image = Image.open (r"Python_Programming\School management software\16.png")
log_image = log_image.resize ((350,250), Image.Resampling.LANCZOS)
log = ImageTk.PhotoImage (log_image)

label = Label (root, image = log, bg = "#63F2E7")
label.place (x = 50, y = 90, width = 350, height = 250)

        
# Making frame --------------------------------------------------------------------

frame1 = Frame (root, borderwidth = 0, bg = "#63F2E7", relief = RIDGE)
frame1.place (x = 360, y = 40, width = 300, height = 350)

# Making Login label --------------------------------------------------------------------

log_label = Label (frame1, text = "LOGIN", bg = "#63F2E7", fg = "#EF5564", font = ("Microsoft YaHei UI Bold", 20))
log_label.place (x = 100, y = 10)

# Making functions for user_entry --------------------------------------------------------------------
def on_enter (e):
        username_entry.delete (0, "end")
        
def on_leave (e):
        name = username_entry.get()
        if name == "":
            username_entry.insert (0, "Username")

#  Making a entry named user_entry --------------------------------------------------------------------

userVar = StringVar()
username_entry = Entry (frame1,textvariable = userVar, bd = 0, font = ("Microsoft YaHei UI Bold", 11), cursor = "hand2", bg = "#63F2E7")
username_entry.place (x =50, y = 80, width = 200, height = 22)
username_entry.insert (0, "Username")
username_entry.bind ("<FocusIn>", on_enter )
username_entry.bind ("<FocusOut>", on_leave)

Frame (frame1, bg = "black",  width = 200, height = 2).place (x = 50, y = 101)

         
def on_enter (e):
        pass_entry.delete (0, "end")
        
def on_leave (e):
        name = pass_entry.get()
        if name == "":
            pass_entry.insert (0, "Password")

def changeye ():
      openeye.config (file = r"Python_Programming\School management software\closeye.png")
      pass_entry.config (show = "*")
      eye_btn.config (command = change2)

def change2():
      openeye.config (file = r"Python_Programming\School management software\openeye.png")
      pass_entry.config (show = "")
      eye_btn.config (command = changeye)

# Making a Entry named pass_entry--------------------------------------------------------------------

passVar = StringVar()
pass_entry = Entry (frame1, textvariable = passVar, bd = 0, font = ("Microsoft YaHei UI Bold", 11), cursor = "hand2", bg = "#63F2E7")
pass_entry.place (x =50, y = 150, width = 200, height = 22)
pass_entry.insert (0, "Password")
pass_entry.bind ("<FocusIn>", on_enter)
pass_entry.bind ("<FocusOut>", on_leave)

# openeye = Image.open (r"School management software\openeye.png")
# openeye = openeye.resize ((20,20), Image.Resampling.LANCZOS)
openeye = PhotoImage(file = r"Python_Programming\School management software\openeye.png")
eye_btn = Button (frame1, image = openeye, bg = "#63F2E7", bd = 0, cursor = "hand2", activebackground = "#63F2E7", command = changeye)
eye_btn.place (x =230, y = 150, width = 20, height = 20)

Frame (frame1, bg = "black",  width = 200, height = 2).place (x = 50, y = 170)

forgot_pass = Button (frame1, text = "Forgot password?", bd = 0, font = ("Microsoft YaHei UI Bold", 8, "bold"), bg = "#63F2E7", fg = "black", activebackground = "#63F2E7")
forgot_pass.place (x = 150, y = 175, width =100, height = 20)

# Function making for login ------------------------------------------------------

def signin ():
    if  (username_entry.get() == "" and "Username" or  pass_entry.get() == "" and "Password"):
        messagebox.showerror ("Error", "All fields are required..")
    else:
        try:
            connection = mysql.connector.connect (host = "127.0.0.1", user = "root", password = "pallab@123", database = "school")
            my_cursor = connection.cursor ()
            query = "SELECT COUNT(*) FROM signup_info WHERE user_name = %s and password = %s"
            my_cursor.execute (query, [username_entry.get(), pass_entry.get()])
            row = my_cursor.fetchone()[0]
            if row == 0:
                 messagebox.showerror ("Error", "Password is incorrect..\nDoesn't match from our database..\nPlease try again >>")
            else:
                 messagebox.showinfo ("Success", "Data found ..\nYou are logged in succesfully")
                 root.destroy()
                 import Main_Project

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}", parent=root)
        except Exception as es:
              messagebox.showerror("Error", f"Due to :{str(es)}", parent = root)
        finally:
            if connection.is_connected():
                my_cursor.close()
                connection.close()
              


# Making login button ---------------------------------------------------------------------

login_btn = Button (frame1, text = "Login", bg = "#57a1f8", fg = "white", font = ("Microsoft YaHei UI Bold", 9, "bold"), bd = 0, relief = SUNKEN, cursor = "hand2", padx = 20, command = signin)
login_btn.place (x = 77, y = 230, width = 150, height = 30)

# Making sign uo option ----------------------------------------------------------------------

Label (frame1, text = "Don't have an account?", bg = "#63F2E7", fg = "black", font = ("Microsoft YaHei UI Bold", 9, "bold")). place (x = 40, y = 290)

def signup ():
      root.destroy ()
      import Signup
signup_btn = Button (frame1, text = "Sign-up", fg = "#EF5564",bg = "#63F2E7", font = ("Microsoft YaHei UI Bold", 9, "bold"), bd = 0, relief = SUNKEN, activebackground = "#63F2E7", cursor = "hand2", command = signup)
signup_btn.place (x = 190, y = 288)






root.mainloop()