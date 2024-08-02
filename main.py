from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, Label, Text, LEFT,WORD,BOTH,HORIZONTAL,VERTICAL,BOTTOM,RIGHT,Scrollbar,X,Y, END
import sql1

class GUI:
    def __init__(self, root):
        self.root = root
        self.custom_font = ("Helvetica", 15, "bold italic")
        self.name = ""
        self.setup_window()
        self.first_screen()
    
    
    def setup_window(self):
        self.root.geometry("775x494")
        self.root.configure(bg="#FFFFFF")

    def first_screen(self):
        self.clear_window()
        self.root.geometry("775x494")
        self.canvas1 = Canvas(
            self.root,
            bg="#FFFFFF",
            height=494,
            width=775,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas1.place(x=0, y=0)

        self.image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas1.create_image(387.0, 247.0, image=self.image_1)

        self.image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas1.create_image(580.0, 70.0, image=self.image_2)

        self.image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.canvas1.create_image(430.0, 243.0, image=self.image_4)

        self.image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.canvas1.create_image(187.0, 247.0, image=self.image_5)

        
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas1.create_image(614.0, 240.0, image=self.entry_image_1)
        self.entry_1 = Entry(
            bd=0,
            bg="#85433D",
            fg="white",
            font=self.custom_font,
            highlightthickness=0
        )
        self.entry_1.place(x=496.0, y=223.0, width=236.0, height=32.0)

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.nameandscreen_change,
            relief="flat"
        )
        self.button_1.place(x=546.0, y=300.0, width=122.0, height=40.1588134765625)

    def nameandscreen_change(self):
        self.name = self.entry_1.get()
        
        self.second_screen()

    def second_screen(self):
        self.clear_window()

        self.root.geometry("763x500")
        
        self.canvas2 = Canvas(
            self.root,
            bg="#FFFFFF",
            height=500,
            width=763,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas2.place(x=0, y=0)

        self.image_1 = PhotoImage(file=self.relative_to_assets_second_screen("image_1.png"))
        self.canvas2.create_image(381.0, 250.0, image=self.image_1)

        self.button_image_1 = PhotoImage(file=self.relative_to_assets_second_screen("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.third_screen,
            relief="flat"
        )
        self.button_1.place(x=492.0, y=340.0, width=203.0, height=41.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets_second_screen("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.fourth_screen,
            relief="flat"
        )
        self.button_2.place(x=492.0, y=283.0, width=203.0, height=41.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets_second_screen("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(x=492.0, y=402.0, width=203.0, height=41.0)

        self.image_2 = PhotoImage(file=self.relative_to_assets_second_screen("image_2.png"))
        self.canvas2.create_image(219.0, 250.0, image=self.image_2)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets_second_screen("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.first_screen,
            relief="flat"
        )
        self.button_4.place(x=0.0, y=0.0, width=90.0, height=89.0)

    def third_screen(self):
        self.clear_window()
        
        self.root.geometry("763x596")
        
        self.root.geometry("763x596")
        self.canvas3 = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 596,
            width = 763,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas3.place(x=0,y=0)
        
        self.label1 = Label(self.root, text="", font=self.custom_font,background="#330000",foreground="white", justify="left")
        self.label1.place(x=480,y=120)


        def display_text_of_selectefood(stringref):
            chgdtext = self.label1.cget("text") + "\n" + stringref
            self.label1.config(text=chgdtext)
            
        def clear_display_selected_food():
            self.label1.config(text="")
            

        self.canvas3.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets_third_screen("image_1.png"))
        self.image_1 = self.canvas3.create_image(
            381.0,
            300.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets_third_screen("image_2.png"))
        self.image_2 = self.canvas3.create_image(
            209.0,
            300.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.queryPlaceOrder(self.label1.cget('text')),
            relief="flat"
        )
        self.button_1.place(
            x=454.0,
            y=534.0,
            width=280.0,
            height=41.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Cheeseburger"),
            relief="flat"
        )
        self.button_2.place(
            x=32.0,
            y=140.0,
            width=168.0,
            height=17.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Cheese Sandwich"),
            relief="flat"
        )
        self.button_3.place(
            x=32.0,
            y=157.0,
            width=168.0,
            height=17.0
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Cheese Sandwich"),
            relief="flat"
        )
        self.button_4.place(
            x=32.0,
            y=174.0,
            width=168.0,
            height=17.0
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Spicy Chicken"),
            relief="flat"
        )
        self.button_5.place(
            x=32.0,
            y=191.0,
            width=168.0,
            height=17.0
        )

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Hot dog"),
            relief="flat"
        )
        self.button_6.place(
            x=32.0,
            y=208.0,
            width=168.0,
            height=17.0
        )

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Fruit Salad"),
            relief="flat"
        )
        self.button_7.place(
            x=223.0,
            y=304.0,
            width=168.0,
            height=17.0
        )

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Cocktail"),
            relief="flat"
        )
        self.button_8.place(
            x=223.0,
            y=321.0,
            width=168.0,
            height=17.0
        )

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Nuggets"),
            relief="flat"
        )
        self.button_9.place(
            x=223.0,
            y=338.0,
            width=168.0,
            height=17.0
        )

        self.button_image_10 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Sandwich"),
            relief="flat"
        )
        self.button_10.place(
            x=223.0,
            y=355.0,
            width=168.0,
            height=17.0
        )

        self.button_image_11 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("French Fries"),
            relief="flat"
        )
        self.button_11.place(
            x=223.0,
            y=372.0,
            width=168.0,
            height=17.0
        )

        self.button_image_12 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Milk Shake"),
            relief="flat"
        )
        self.button_12.place(
            x=31.0,
            y=467.0,
            width=168.0,
            height=17.0
        )

        self.button_image_13 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_13.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Iced Tea"),
            relief="flat"
        )
        self.button_13.place(
            x=31.0,
            y=484.0,
            width=168.0,
            height=17.0
        )

        self.button_image_14 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_14.png"))
        self.button_14 = Button(
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Orange juice"),
            relief="flat"
        )
        self.button_14.place(
            x=31.0,
            y=501.0,
            width=168.0,
            height=17.0
        )

        self.button_image_15 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_15.png"))
        self.button_15 = Button(
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Lemon Tea"),
            relief="flat"
        )
        self.button_15.place(
            x=31.0,
            y=518.0,
            width=168.0,
            height=17.0
        )

        self.button_image_16 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_16.png"))
        self.button_16 = Button(
            image=self.button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: display_text_of_selectefood("Coffees"),
            relief="flat"
        )
        self.button_16.place(
            x=31.0,
            y=535.0,
            width=168.0,
            height=17.0
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets_third_screen("image_3.png"))
        self.image_3 = self.canvas3.create_image(
            594.0,
            291.0,
            image=self.image_image_3
        )

        self.button_image_17 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_17.png"))
        self.button_17 = Button(
            image=self.button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=clear_display_selected_food,
            relief="flat"
        )
        self.button_17.place(
            x=454.0,
            y=18.0,
            width=280.0,
            height=38.0
        )

        self.canvas3.create_rectangle(
            472.0,
            109.0,
            716.0,
            484.0,
            fill="#320000",
            outline="")

        self.button_image_18 = PhotoImage(
            file=self.relative_to_assets_third_screen("button_18.png"))
        self.button_18 = Button(
            image=self.button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=self.second_screen,
            relief="flat"
        )
        self.button_18.place(
            x=0.0,
            y=4.0,
            width=90.0,
            height=89.0
        )

    
    def fourth_screen(self):
        self.clear_window()
        
        self.root.geometry("798x548")
        
        self.canvas4 = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 538,
            width = 788,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )



        self.canvas4.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("image_1.png"))
        self.image_1 = self.canvas4.create_image(
            394.0,
            269.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("image_2.png"))
        self.image_2 = self.canvas4.create_image(
            393.0,
            43.0,
            image=self.image_image_2
        )

        # image_image_2 = PhotoImage(
        #     file=relative_to_assets_fourth_screen("Text.png"))
        # image_2 = canvas4.create_image(
        #     390.5,
        #     365.0,
        #     image=image_image_2
        # )

        self.canvas4.create_rectangle(
            31.0,
            188.0,
            753.0,
            494.0,
            fill="#BCACC5",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.second_screen,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=90.0,
            height=89.0
        )



        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("entry_1.png"))
        self.entry_bg_1 = self.canvas4.create_image(
            301.5,
            153.0,
            image=self.entry_image_1
            
        )
        self.entry_1 = Entry(
            bd=0,
            font=self.custom_font,
            bg="#D7C5CA",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=131.0,
            y=139.0,
            width=341.0,
            height=26.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("entry_2.png"))
        self.entry_bg_2 = self.canvas4.create_image(
            301.5,
            104.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            font=self.custom_font,
            bg="#D7C5CA",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=131.0,
            y=89.0,
            width=341.0,
            height=28.0
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("image_3.png"))
        self.image_3 = self.canvas4.create_image(
            75.0,
            151.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("image_4.png"))
        self.image_4 = self.canvas4.create_image(
            60.0,
            107.0,
            image=self.image_image_4
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.querysearch,
            relief="flat"
        )
        self.button_2.place(
            x=611.0,
            y=139.0,
            
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=496.0,
            y=143.0,
            
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets_fourth_screen("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=543.0,
            y=134.0,
            
        )

        self.text_widget = Text(self.root, wrap=WORD, height=13, width=66,font=self.custom_font, background="#D7C5CA")
        self.text_widget.place(x=30,y=180)

        # Create a vertical scrollbar linked to the Text widget
        self.v_scroll = Scrollbar(self.root, orient=VERTICAL, command=self.text_widget.yview)
        self.v_scroll.pack(side=RIGHT, fill=Y)

        # Create a horizontal scrollbar linked to the Text widget
        self.h_scroll = Scrollbar(self.root, orient=HORIZONTAL, command=self.text_widget.xview)
        self.h_scroll.pack(side=BOTTOM, fill=X)

        # Configure the Text widget to use the scrollbars
        self.text_widget.config(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        self.example_text = ("...")
        self.text_widget.insert(END, self.example_text)

    def querysearch(self):
        self.text_widget.delete("1.0", END)
        
        if len(self.entry_2.get()) == 0 and len(self.entry_1.get()) == 0:
            self.text_widget.insert(END,sql1.run_sql_command_for_showing_result(str("select * from Customers ")))
        elif(len(self.entry_2.get()) > 0 and len(self.entry_1.get()) > 0):
            self.text_widget.insert(END,sql1.run_sql_command_for_showing_result(str("SELECT itemname FROM OrderDetail WHERE orderid IN (SELECT orderid FROM Orders WHERE customerid=" + self.entry_1.get() + ")")))
        elif(len(self.entry_2.get()) > 0):
            self.text_widget.insert(END,sql1.run_sql_command_for_showing_result(str("select * from Customers where name="+'\"'+ self.entry_2.get() + '\"')))
    
    
    def queryPlaceOrder(self,original_string):
        list_of_strings = original_string.split('\n')
        sql1.run_sql_command(str("insert into Customers(name) values (" + '\''+self.name+"\')"))
        currentCustomerid = sql1.run_sql_command(str("SELECT MAX(personid) FROM Customers"))
        print(currentCustomerid)
        sql1.run_sql_command(str("insert into Orders(customerid) values ("+currentCustomerid+")"))
        
        currentorderid = sql1.run_sql_command(str("SELECT MAX(orderid) FROM Orders"))
        print(currentorderid)
        
        if len(self.name) > 0 and len(original_string)>0:
            
            for s in list_of_strings:
                sql1.run_sql_command(str("insert into OrderDetail(orderid,itemname) values ("+ currentorderid +"," + '\''+s+"\')"))
        
        self.first_screen()   
            
            
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def relative_to_assets(self, path: str) -> Path:
        output_path = Path(__file__).parent
        assets_path = output_path / Path(r"C:\Users\anura\Desktop\Programming\programs\DBMS project\RestaurantOrder\assets\frame3")
        return assets_path / Path(path)
    #order + search
    def relative_to_assets_second_screen(self, path: str) -> Path:
        output_path = Path(__file__).parent
        assets_path = output_path / Path(r"C:\Users\anura\Desktop\Programming\programs\DBMS project\RestaurantOrder\assets\frame0")
        return assets_path / Path(path)
    #order canvas 
    def relative_to_assets_third_screen(self, path: str) -> Path:
        output_path = Path(__file__).parent
        assets_path = output_path / Path(r"C:\Users\anura\Desktop\Programming\programs\DBMS project\RestaurantOrder\assets\frame1")
        return assets_path / Path(path)
    #search canvas
    def relative_to_assets_fourth_screen(self, path: str) -> Path:
        output_path = Path(__file__).parent
        assets_path = output_path / Path(r"C:\Users\anura\Desktop\Programming\programs\DBMS project\RestaurantOrder\assets\frame2")
        return assets_path / Path(path)

    
if __name__ == "__main__":
    root = Tk()
    root.title("Restaurant APP")
    gui = GUI(root)
    root.resizable(False, False)
    root.mainloop()
