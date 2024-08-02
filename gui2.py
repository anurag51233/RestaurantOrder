
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Label,LEFT,WORD,BOTH,HORIZONTAL,VERTICAL,BOTTOM,RIGHT,Scrollbar,X,Y,END


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\anura\Desktop\Programming\programs\DBMS project\ResV1\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

custom_font = ("Helvetica", 12, "bold italic") 

window = Tk()

window.geometry("788x538")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 538,
    width = 788,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)



canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    394.0,
    269.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    393.0,
    43.0,
    image=image_image_2
)

# image_image_2 = PhotoImage(
#     file=relative_to_assets("Text.png"))
# image_2 = canvas.create_image(
#     390.5,
#     365.0,
#     image=image_image_2
# )

canvas.create_rectangle(
    31.0,
    188.0,
    753.0,
    494.0,
    fill="#BCACC5",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=0.0,
    y=0.0,
    width=90.0,
    height=89.0
)



entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    301.5,
    153.0,
    image=entry_image_1
    
)
entry_1 = Entry(
    bd=0,
    font=custom_font,
    bg="#D7C5CA",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=131.0,
    y=139.0,
    width=341.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    301.5,
    104.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    font=custom_font,
    bg="#D7C5CA",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=131.0,
    y=89.0,
    width=341.0,
    height=28.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    75.0,
    151.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    60.0,
    107.0,
    image=image_image_4
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=611.0,
    y=139.0,
    
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=496.0,
    y=143.0,
    
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=543.0,
    y=134.0,
    
)

text_widget = Text(window, wrap=WORD, height=18, width=80,font=custom_font, background="#D7C5CA")
text_widget.place(x=30,y=180)

# Create a vertical scrollbar linked to the Text widget
v_scroll = Scrollbar(window, orient=VERTICAL, command=text_widget.yview)
v_scroll.pack(side=RIGHT, fill=Y)

# Create a horizontal scrollbar linked to the Text widget
h_scroll = Scrollbar(window, orient=HORIZONTAL, command=text_widget.xview)
h_scroll.pack(side=BOTTOM, fill=X)

# Configure the Text widget to use the scrollbars
text_widget.config(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

example_text = ("This is an example of a scrollable Text widget in Tkinter.\n"
                "You can add a lot of text here to see how the scrollbars work.\n"
                "This widget supports both vertical and horizontal scrolling.\n"
                "Feel free to add more content to test scrolling functionality.\n\n\n\n\n\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed justo et nunc gravida efficitur. "
                "Sed varius tincidunt nisl, a placerat nulla cursus sit amet. Quisque sit amet lacinia lorem. Maecenas "
                "rhoncus, ipsum nec ultrices consequat, augue odio facilisis nulla, at gravida nisl erat a sapien. "
                "Praesent hendrerit, elit at varius aliquet, lacus sapien pharetra turpis, in tempus metus nisi nec mi. "
                "Suspendisse potenti.")
text_widget.insert(END, example_text)


window.resizable(False, False)
window.mainloop()
