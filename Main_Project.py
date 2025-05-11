from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import webbrowser

# Making School class

class School:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("1600x800+0+0")
        self.root.title("AHDHS School Management")
        self.root.config (bg = "red")
# Image no 1
        about = LabelFrame (self.root, text = "About : ", font =("Microsoft YaHei UI Bold", 10), bd = 0, bg = "#14F39A")
        about.place (x = 5, y = 5, width = 515, height = 150)

        label1 = Label (about, text = "AUNIATIA HEMCHANDRA DEV HSS was established in 1943 and it is managed \nby the Department of Education. It is located in Urban area. It is located in AMGURI block of \nSIBSAGAR district of Assam. \nThe school consists of Grades from 6 to 12. \nThe school is Co-educational and it doesn't have an \nattached pre-primary section. The school is Not Applicable in nature and \nis not using school building as a shift-school...", font = ("Microsoft YaHei UI Bold", 8, "bold"), bg = "#14F39A")
        label1.place (x = 0, y = 5)

        about2 = LabelFrame (self.root, text = "School Contact : ", font =("Microsoft YaHei UI Bold", 10), bd = 0, bg = "#11B1DE")
        about2.place (x = 1040, y = 5, width = 490, height = 150)

        lb1 = Label (about2, text = "Ward No - 10, AMGURI ", font =("Comicsanms", 10, "bold"), bd = 0, bg = "#11B1DE")
        lb1.place (x = 180, y = 0)
        lb2 = Label (about2, text = "Sibsagar, ASSAM ", font =("Microsoft YaHei UI Bold", 15), bd = 0, bg = "#11B1DE")
        lb2.place (x = 166, y = 20)
        lb3 = Button (about2, text = "PIN Code : 785680(Assam)", font =("Microsoft YaHei UI Bold", 15), bd = 0, bg = "#11B1DE", activebackground = "#11B1DE", command = self.map, cursor = "hand2")
        lb3.place (x = 125, y = 54, height = 20)
        lb4 = Label (about2, text = "Mobile No : +91600XXX8031", font =("Comicsanms", 10), bd = 0, bg = "#11B1DE")
        lb4.place (x = 170, y = 80)
        lb5 = Label (about2, text = "E-mail : duarahXXXXXX0@gmail.com", font =("Comicsanms", 10), bd = 0, bg = "#11B1DE")
        lb5.place (x = 150, y = 100)
        
        # i1 = Image.open (r"School management software\4.png")
        # i1 = i1.resize((533,160),Image.Resampling.LANCZOS)
        # self.photoimage1 = ImageTk.PhotoImage (i1)

        # self.label = Label (self.root, image = self.photoimage1)
        # self.label.place (x = 0, y = 0)
# Image no 2
        i2 = Image.open (r"Python_Programming\School management software\4.png")
        i2 = i2.resize((510,160),Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage (i2)
# 
        self.label = Button (self.root, image = self.photoimage2, bd = 0)
        self.label.place (x = 525, y = 5, width = 510, height = 150)
    
# Image no 3
        # i3 = Image.open (r"School management software\6.png")
        # i3 = i3.resize((533,160),Image.Resampling.LANCZOS)
        # self.photoimage3 = ImageTk.PhotoImage (i3)

        # self.label = Label (self.root, image = self.photoimage3)
        # self.label.place (x = 1066, y = 0)

# Background image
        bg_img = Image.open (r"Python_Programming\School management software\2.png")
        bg_img = bg_img.resize ((1600,710),Image.Resampling.LANCZOS)
        self.bg_photoimage = ImageTk.PhotoImage (bg_img)

        b_g = Label (self.root, image = self.bg_photoimage, relief = SUNKEN, bd = 4)
        b_g.place (x = 0, y = 160, width =1600, height = 710)

# Title of the Project
        
        # title_img = Image.open (r"School management software\12.png")
        # title_img = title_img.resize ((680,100),Image.Resampling.LANCZOS)
        # self.title_photoimage = ImageTk.PhotoImage (title_img)

        title_ = Frame (self.root, bg =  "#EE677D")
        title_.place (x = 340, y = 165, width =900, height = 50)

        icon = Image.open (r"Python_Programming\School management software\ahsec.png")
        icon = icon.resize ((50, 50), Image.Resampling.LANCZOS)
        self.icon_img = ImageTk.PhotoImage (icon)

        icon_label = Label (title_, image = self.icon_img, bg = "#EE677D")
        icon_label.place (x = 105, y = 0, width = 50, height = 50)

        icon2 = Image.open (r"Python_Programming\School management software\ahsec.png")
        icon2 = icon2.resize ((50, 50), Image.Resampling.LANCZOS)
        self.icon_img2 = ImageTk.PhotoImage (icon2)

        icon_label2 = Label (title_, image = self.icon_img2, bg = "#EE677D")
        icon_label2.place (x = 730, y = 0, width = 50, height = 50)

        title_name = Button (title_, text = "A. H. D. H. S. School, AMGURI, 785680", font = ("Microsoft YaHei UI Bold", 20), fg ="#14F39A", bg = "#EE677D", activebackground = "#EE677D", command = self.scl, bd = 0, cursor = "hand2")
        title_name.place (x = 180, y = 0, height = 25)
        blog = Label (title_, text = "Auniatiya Hemchandra Dev Higher Secondary School. Established in the year 1943.", font = ("Microsoft YaHei UI Bold", 10), fg ="#14F39A", bg = "#EE677D")
        blog.place (x = 165, y = 25)



# Making frame

        frame1 = Frame (b_g, bg = "light blue", padx = 20, pady = 20)
        frame1.place (x = 15, y = 55, width = 1500, height = 560)

        developer_name = Button (self.root, text = "Developed by @Pallab Duarah ", font = ("Microsoft YaHei UI Bold", 7), fg = "black", bg = "light blue", bd = 0, activebackground = "light blue", command = self.openlink, cursor = "hand2")
        developer_name.place (x = 1370, y = 763, height = 10)

# Left side student info frame 

        frame2 = Frame (frame1, bg = "light blue", bd = 0)
        frame2.place (x = 0, y = 10, width = 730, height = 530)

        under_img = Image.open (r"Python_Programming\School management software\1.png")
        under_img = under_img.resize((730, 160), Image.Resampling.LANCZOS)
        self.under_img = ImageTk.PhotoImage (under_img)

        self.label = Label (frame2, image = self.under_img)
        self.label.place (x = 0, y = 0, width = 730, height = 160)

        # Current academics info

        frame2_2 = LabelFrame (frame2, text = " Current Academics Information ... ", font = ("Microsoft YaHei UI Bold", 10), fg = "#EA2E1D", bd = 0, bg = "#D5BCE2")
        frame2_2.place (x = 0, y = 160, width = 730, height = 120)

        # Variable of all entrys and combo boxes

        self.clsVar = StringVar ()
        self.yearVar = StringVar ()
        self.boardVar = StringVar ()
        self.academicsVar = StringVar ()
        self.nameVar = StringVar()
        self.idVar = StringVar()
        self.rollVar = StringVar()
        self.emailVar = StringVar()
        self.contactVar = StringVar()
        self.addressVar = StringVar()
        self.dobVar = StringVar()
        self.guardianVar = StringVar ()
        self.genderVar = StringVar ()
        self.divisionVar = StringVar ()

        # Conbo box in frame2_2

        cls = Label (frame2_2, text = "Class : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 10, bg = "#D5BCE2")
        cls.grid (row = 0, column = 0, sticky = "w")

        combo1 = ttk.Combobox (frame2_2, font = ("Microsoft YaHei UI Light", 8, "bold"), textvariable = self.clsVar, width = 15, state = "readonly",cursor = "hand2")
        combo1["values"] = ("Select Class", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "HS 1st year", "HS 2nd year")
        combo1.current (0)
        combo1.grid (row = 0, column = 1)

        # Combo box 2 in frame2_2
        
        year = Label (frame2_2, text = "Year : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 10, bg = "#D5BCE2")
        year.grid (row = 0 , column = 2)

        combo2 = ttk.Combobox (frame2_2, font = ("Microsoft YaHei UI Light", 8, "bold"), textvariable = self.yearVar, width = 15, state = "readonly", cursor = "hand2")
        combo2["values"] = ("Select Year", "2024", "2023", "2022", "2021", "2020", "2019", "2018")
        combo2.current (0)
        combo2.grid (row = 0, column = 3)

        # Combo box 3 in frame 2_2

        board = Label (frame2_2, text = "Board : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 10, bg = "#D5BCE2")
        board.grid (row = 1, column = 0)

        combo3 = ttk.Combobox (frame2_2, font = ("Microsoft Yahei UI Light", 8, "bold"), textvariable = self.boardVar, width = 15, state = "readonly", cursor = "hand2")
        combo3["values"] = ("Select Board", "AHSEC", "SEBA", "CBSE")
        combo3.current(0)
        combo3.grid (row = 1 , column = 1)

        # Combo box 4 in frame2_2

        academics_type = Label (frame2_2, text = "Academics : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 10, bg = "#D5BCE2")
        academics_type.grid (row = 1, column = 2)

        academics_type = ttk.Combobox (frame2_2, font = ("Microsoft YaHei UI Light", 8, "bold"), textvariable = self.academicsVar, width = 15, state = "readonly", cursor = "hand2")
        academics_type["values"] = ("Select Academics", "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        academics_type.current(0)
        academics_type.grid (row = 1 , column = 3)

        ahsecicon = Image.open (r"Python_Programming\School management software\10.png")
        ahsecicon = ahsecicon.resize((200,100),Image.Resampling.LANCZOS)
        self.iconimage = ImageTk.PhotoImage (ahsecicon)

        self.icon1 = Label (frame2, image = self.iconimage, bg = "#D5BCE2")
        self.icon1.place (x = 500, y = 170, width = 200, height = 100)

        # Student personal information

        frame2_3 = LabelFrame (frame2, text = " Student Personal Information ... ", font = ("Microsoft YaHei UI Bold", 10), fg = "#EA2E1D", bg = "#63F2E7", bd = 0)
        frame2_3.place (x = 0, y = 280, width = 730, height = 230)

        name = Label (frame2_3, text = "Student Name : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        name.grid (row = 0, column = 0)

        name_entry = Entry (frame2_3, textvariable = self.nameVar, width = 30, cursor = "hand2", bd = 0)
        name_entry.grid (row = 0, column = 1)

        id = Label (frame2_3, text = "Student ID : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        id.grid (row = 0, column = 2)

        id_entry = Entry (frame2_3, textvariable = self.idVar, width = 30, cursor = "hand2", bd = 0)
        id_entry.grid (row = 0, column = 3)

        roll = Label (frame2_3, text = "Roll No : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        roll.grid (row = 1, column = 0)

        roll_entry = Entry (frame2_3, textvariable = self.rollVar, width = 30, cursor = "hand2", bd = 0)
        roll_entry.grid (row = 1, column = 1)

        dob = Label (frame2_3, text = "DOB : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        dob.grid (row = 1, column = 2)
        
        def binding (event):
            dob_entry.delete(0, "end")
        dob_entry = Entry (frame2_3, textvariable = self.dobVar, width = 30, cursor = "hand2", bd = 0)
        dob_entry.grid (row = 1, column =3)
        dob_entry.insert (0, "YYYY-MM-DD")
        dob_entry.bind ("<FocusIn>", binding)

        contact = Label (frame2_3, text = "Contact no : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        contact.grid (row = 2, column = 0)

        contact_entry = Entry (frame2_3, textvariable = self.contactVar, width = 30, cursor = "hand2", bd = 0)
        contact_entry.grid (row = 2, column =1)

        email = Label (frame2_3, text = "Email ID : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        email.grid (row = 2, column = 2)

        email_entry = Entry (frame2_3, textvariable = self.emailVar, width = 30, cursor = "hand2", bd = 0)
        email_entry.grid (row = 2, column = 3)

        gender = Label (frame2_3, text = "Gender : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        gender.grid (row = 3, column = 0)

        gendercombo = ttk.Combobox (frame2_3, font = ("Microsoft YaHei UI Light", 8, "bold"), textvariable = self.genderVar, width = 15, state = "readonly", cursor = "hand2")
        gendercombo["values"] = ("Select Gender", "Male", "Female")
        gendercombo.current(0)
        gendercombo.grid (row = 3 , column = 1)

        division = Label (frame2_3, text = "Division : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        division.grid (row = 3, column = 2)

        divisioncombo = ttk.Combobox (frame2_3, font = ("Microsoft YaHei UI Light", 8, "bold"), textvariable = self.divisionVar, width = 15, state = "readonly", cursor = "hand2")
        divisioncombo["values"] = ("Select Division", "A", "B", "C", "Commerce", "Science")
        divisioncombo.current(0)
        divisioncombo.grid (row = 3 , column = 3)

        address = Label (frame2_3, text = "Address : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        address.grid (row = 4, column = 0)

        address_entry = Entry (frame2_3, textvariable = self.addressVar, width = 30, cursor = "hand2", bd = 0)
        address_entry.grid (row = 4, column = 1)

        gardian = Label (frame2_3, text = "Guardian Name : ", font = ("Microsoft YaHei UI Bold", 10), padx = 10, pady = 5, bg = "#63F2E7")
        gardian.grid (row = 4, column = 2)

        gardian_entry = Entry (frame2_3, textvariable = self.guardianVar, width = 30, cursor = "hand2", bd = 0)
        gardian_entry.grid (row = 4, column = 3)
        
        # Button frame 

        button_frame = Frame (frame2_3, bg = "#E7F70A", bd = 0)
        button_frame.place (x = 5, y = 170, width = 720, height = 35)

        save_button = Button (button_frame, text = "Save", font = ("Comicsanms", 12, "bold"), command = self.save_info, bg = "green", fg = "white", width = 17, cursor = "hand2", bd = 0)
        save_button.grid(row = 0, column = 0, padx = 2, pady = 2)

        update_button = Button (button_frame, text = "Update", font = ("Comicsanms", 12, "bold"), bg = "blue", fg = "white", width = 17, cursor = "hand2", bd = 0, command = self.update)
        update_button.grid(row = 0, column = 1, padx = 2, pady = 2)

        delete_button = Button (button_frame, text = "Delete", font = ("Comicsanms", 12, "bold"), bg = "red", fg = "white", width = 17, cursor = "hand2", command = self.delete, bd = 0)
        delete_button.grid(row = 0, column = 2, padx = 2, pady = 2)

        Reset_button = Button (button_frame, text = "Reset", font = ("Comicsanms", 12, "bold"), bg = "#9323E2", fg = "white", width = 17, cursor = "hand2", bd = 0, command = self.reset)
        Reset_button.grid(row = 0, column = 3, padx = 2, pady = 2)


# Right side frame

        frame3 = Frame (frame1, bg = "light blue")
        frame3.place (x = 740, y = 10, width = 730, height = 530)

        # Right side image
        rightside_img = Image.open (r"Python_Programming\School management software\9.png")
        rightside_img = rightside_img.resize((720,200),Image.Resampling.LANCZOS)
        self.rightside = ImageTk.PhotoImage (rightside_img)

        self.right = Label (frame3, image = self.rightside, cursor = "hand2")
        self.right.place (x = 0, y = 0, width = 720, height = 200)

        # Search frame
        frame3_2 = LabelFrame (frame3, text = "Search Student information ... ", font = ("Microsoft YaHei UI Bold", 10), fg = "#63F2E7", bg = "#D55959", bd = 0)
        frame3_2.place (x = 0, y = 200, width = 720, height = 50)

        search_lbl = Label (frame3_2, text = " Search by : ", font = ("Comicsanms", 10, "bold"), fg = "black",bg = "#D55959", width = 20)
        search_lbl.grid (row = 0 , column = 0, padx = 5)
        
        self.searchcomboVar = StringVar ()
        searchcombo = ttk.Combobox (frame3_2, font = ("Microsoft YaHei UI Light", 8, "bold"), textvariable = self.searchcomboVar, width = 15, state = "readonly", cursor = "hand2")
        searchcombo["values"] = ("Select Option", "By ID", "By Name", "By Roll No")
        searchcombo.current(0)
        searchcombo.grid (row = 0, column = 1, padx = 5)

        self.searchVar = StringVar ()
        search_entry = Entry (frame3_2, font = ("Comicsanms", 10), width = 20, textvariable = self.searchVar, cursor = "hand2", bd = 0)
        search_entry.grid (row = 0 , column = 2, padx = 5)

        search_btn = Button (frame3_2, text = "Search", font = ("Comicsanms", 10, "bold"), bg = "blue", fg = "white", width = 13, cursor = "hand2", bd = 0, command = self.search)
        search_btn.grid (row = 0, column  = 3, padx = 5)

        showall_btn = Button (frame3_2, text = "Show all", font = ("Comicsanms", 10, "bold"), bg = "blue", fg = "white", width = 13, cursor = "hand2", bd = 0, command = self.fetch_data)
        showall_btn.grid (row = 0, column  = 4, padx = 5)

        # Table frame making
        table_frame = Frame (frame3)
        table_frame.place (x = 0, y = 250, width = 720, height = 260)

        # Scroll bar making

        scrollx = ttk.Scrollbar (table_frame, orient = HORIZONTAL)
        scrolly = ttk.Scrollbar (table_frame, orient = VERTICAL)
        self.table = ttk.Treeview (table_frame, column = ("student", "name", "cls", "year", "board", "no", "guardian", "contact", "E-Mail", "DOB", "gender", "div", "add", "ac"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)

        scrollx.pack (side = BOTTOM, fill = X)
        scrolly.pack (side = RIGHT, fill = Y)

        scrollx.config (command = self.table.xview)
        scrolly.config (command = self.table.yview)
        
        # Table heading

        self.table.heading("student", text = "Student ID")
        self.table.heading("name", text = "Student Name")
        self.table.heading("cls", text = "Class")
        self.table.heading("year", text = "Year")
        self.table.heading("board", text = "Board")
        self.table.heading("no", text = "Roll No")
        self.table.heading("guardian", text = "Guardian Name")
        self.table.heading("contact", text = "Contact No")
        self.table.heading("E-Mail", text = "E-Mail ID")
        self.table.heading("DOB", text = "Date Of Birth")
        self.table.heading("gender", text = "Gender")
        self.table.heading("div", text = "Division")
        self.table.heading("add", text = "Address")
        self.table.heading("ac", text = "Academics")

        self.table["show"] = "headings"
        
        self.table.column("student", width = 100)
        self.table.column("name", width = 100)
        self.table.column("cls", width = 100)
        self.table.column("year", width = 100)
        self.table.column("board", width = 100)
        self.table.column("no", width = 100)
        self.table.column("guardian", width = 100)
        self.table.column("contact", width = 100)
        self.table.column("E-Mail", width = 150)
        self.table.column("DOB", width = 100)
        self.table.column("gender", width = 100)
        self.table.column("div", width = 100)
        self.table.column("add", width = 150)
        self.table.column("ac", width = 100)

        self.table.pack (fill = BOTH, expand = 1)
        self.table.bind ("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

# saving info into database function
    def save_info (self):
        if (self.nameVar.get() == "" or self.idVar.get() == "" or self.rollVar.get() == ""  or self.emailVar.get() == "" or self.guardianVar.get() == "") : 
            messagebox.showerror ("Error", "All fields are required")
        else:
             try:
                 connection = mysql.connector.connect (host = "127.0.0.1", username = "root", password = "pallab@123", database = "school")
                 my_cursor = connection.cursor ()
                 my_cursor.execute ("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.idVar.get (),
                                                                                                        self.nameVar.get(),
                                                                                                        self.clsVar.get(),
                                                                                                        self.yearVar.get(),
                                                                                                        self.boardVar.get(),
                                                                                                        self.rollVar.get(),
                                                                                                        self.guardianVar.get(),
                                                                                                        self.contactVar.get(),
                                                                                                        self.emailVar.get(),
                                                                                                        self.dobVar.get(),
                                                                                                        self.genderVar.get(),
                                                                                                        self.divisionVar.get(),
                                                                                                        self.addressVar.get(),
                                                                                                        self.academicsVar.get()) )
                 connection.commit()
                 self.fetch_data()
                 connection.close()
                 messagebox.showinfo ("Succesfull", "information has been added", parent = self.root)
             except Exception as es:
                 messagebox.showerror("Error", f"Due to :{str(es)}", parent = self.root)

# fetching data from database into gui
    def fetch_data (self):
         connection = mysql.connector.connect (host = "127.0.0.1", username = "root", password = "pallab@123", database = "school")
         my_cursor = connection.cursor ()
         my_cursor.execute("select* from student")
         data = my_cursor.fetchall()
         if len(data) != 0:
             self.table.delete(*self.table.get_children())
             for i in data:
                 self.table.insert("", END, values = i)
             connection.commit()
         connection.close()

# get cursor function
    def get_cursor (self, event = ""):
        cursor_row = self.table.focus()
        content = self.table.item (cursor_row)
        data = content ["values"]

        self.idVar.set(data [0])
        self.nameVar.set(data [1])
        self.clsVar.set(data [2])
        self.yearVar.set(data [3])
        self.boardVar.set(data [4])
        self.rollVar.set(data [5])
        self.guardianVar.set(data [6])
        self.contactVar.set(data [7])
        self.emailVar.set(data [8])
        self.dobVar.set(data [9])
        self.genderVar.set(data [10])
        self.divisionVar.set(data [11])
        self.addressVar.set(data [12])
        self.academicsVar.set(data [13])

# Delete data function
    def delete (self):
        if (self.nameVar.get() == "" or self.idVar.get() == "" or self.rollVar.get() == ""  or self.emailVar.get() == "" or self.guardianVar.get() == "") :
            messagebox.showerror ("Error", "All fields are required...", parent = self.root)
        else:
            try :
                Delete = messagebox.askyesno ("Query", "Are you sure you want to delete this information..", parent = self.root)
                if Delete > 0 :
                    connection = mysql.connector.connect (host = "127.0.0.1", username = "root", password = "pallab@123", database = "school")
                    my_cursor = connection.cursor ()
                    my_cursor.execute ("delete from student where id = %s", (self.idVar.get(),))
                else:
                    if not Delete :
                        return
                connection.commit()
                self.fetch_data ()
                connection.close()
                messagebox.showinfo ("Success", "Student information has been deleted..", parent = self.root)
            except Exception as es:
                 messagebox.showerror("Error", f"Due to :{str(es)}", parent = self.root)

    def update (self):
        if (self.nameVar.get() == "" or self.idVar.get() == "" or self.rollVar.get() == ""  or self.emailVar.get() == "" or self.guardianVar.get() == "") :
            messagebox.showerror ("Error", "All fields are required...", parent = self.root)
        else:
            try:
                Update = messagebox.askyesno ("update", "Are you sure you want to update this information..", parent = self.root)
                if Update > 0:
                    connection = mysql.connector.connect (host = "127.0.0.1", username = "root", password = "pallab@123", database = "school")
                    my_cursor = connection.cursor ()
                    my_cursor.execute ("update student set name = %s, class = %s, year = %s, board = %s, roll = %s, guard = %s, contact = %s, mail = %s, dob = %s, gender = %s, division = %s, address = %s, academics = %s where id = %s",(self.nameVar.get(),
                    self.clsVar.get(),
                    self.yearVar.get(),
                    self.boardVar.get(),
                    self.rollVar.get(),
                    self.guardianVar.get(),
                    self.contactVar.get(),
                    self.emailVar.get(),
                    self.dobVar.get(),
                    self.genderVar.get(),
                    self.divisionVar.get(),
                    self.addressVar.get(),
                    self.academicsVar.get(),
                    self.idVar.get()))
                else:
                    if not Update:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo ("Success", "Student information has been updated..", parent = self.root)
            except Exception as es:
                 messagebox.showerror("Error", f"Due to :{str(es)}", parent = self.root)

    def reset (self):
        self.idVar.set("")
        self.nameVar.set("")
        self.clsVar.set("Select Class")
        self.yearVar.set("Select Year")
        self.boardVar.set("Select Board")
        self.rollVar.set("")
        self.guardianVar.set("")
        self.contactVar.set("")
        self.emailVar.set("")
        self.dobVar.set("YYYY-MM-DD")
        self.genderVar.set("Select Gender")
        self.divisionVar.set("Select Division")
        self.addressVar.set("")
        self.academicsVar.set("Select Academics")

    def search (self):
        if self.searchcomboVar.get() == "" or self.searchVar.get() == "" :
            messagebox.showerror ("Error", "Please select a option..", parent = self.root)
        else :
            try :
                connection = mysql.connector.connect (host = "127.0.0.1", username = "root", password = "pallab@123", database = "school")
                my_cursor = connection.cursor()
                my_cursor.execute("select * from student where " + self.searchcomboVar.get() +" LIKE '%"+ self.searchVar.get()+ "%'")

                # query = "SELECT * FROM student WHERE " + self.searchcomboVar.get() + " LIKE %s"
                # value = ("%" + self.searchVar.get() + "%",)
                # my_cursor.execute(query, value)

                row = my_cursor.fetchall()

                if len(row) != 0:
                    self.table.delete (*self.table.get_children())
                    for i in row:
                        self.table.insert("", END, values = i)
                    connection.commit()
                connection.close()
            except Exception as es:
                 messagebox.showerror("Error", f"Due to :{str(es)}", parent = self.root)



    
    def scl(self):
        webbrowser.open ("https://schools.org.in/sibsagar/18160300308/auniatia-hemchandra-dev-hss.html")

    def map (self):
        webbrowser.open ("https://maps.app.goo.gl/Lf6vxyT7hWXe4gdQA")

    def openlink(self):
        webbrowser.open ("https://www.instagram.com/__about_.pallab/?__pwa=1")

root = Tk()
student = School (root)
root.mainloop ()