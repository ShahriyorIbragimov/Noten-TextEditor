from pathlib import Path
from customtkinter import CTk, CTkTextbox, END
from tkinter import Canvas, Button, PhotoImage
from tkinter.filedialog import askopenfilename, asksaveasfilename

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")
font_size = 20


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def plus():
    global font_size
    global entry_1
    value = entry_1.get('1.0', END)
    font_size += 2
    entry_1 = CTkTextbox(
        master=window,
        fg_color='#232323',
        text_color='snow',
        width=1899,
        height=973,
        font=('JetBrains Mono', font_size)
    )
    entry_1.place(
        x=0.0,
        y=42.0,
    )
    entry_1.insert('1.0', value)


def minus():
    global font_size
    global entry_1
    value = entry_1.get('1.0', END)
    font_size -= 2
    entry_1 = CTkTextbox(
        master=window,
        fg_color='#232323',
        text_color='snow',
        width=1899,
        height=973,
        font=('JetBrains Mono', font_size)
    )
    entry_1.place(
        x=0.0,
        y=42.0
    )
    entry_1.insert('1.0', value)


def saving():
    path = asksaveasfilename(filetypes=[('text files', '*.txt')])
    if path == '':
        pass
    else:
        with open(path, 'w', encoding='UTF-8') as doc:
            text = entry_1.get('1.0', 'end-1c')
            doc.write(text)


def opening():
    path = askopenfilename(filetypes=[('text files', '*.txt')])
    if path == '':
        pass
    else:
        with open(path, 'r', encoding='UTF-8') as doc:
            text = doc.read()
            entry_1.delete('1.0', END)
            entry_1.insert('1.0', text=text)


def cleaning():
    entry_1.delete('1.0', END)


window = CTk()
window.geometry("1700x850")
window.title("Note")
window.configure(bg="#2C2C2C")
window.minsize(1700, 850)

canvas = Canvas(
    window,
    bg="#2C2C2C",
    height=1017,
    width=1919,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    959.5,
    529.5,
    image=entry_image_1
)
entry_1 = CTkTextbox(
    master=window,
    fg_color='#232323',
    text_color='snow',
    font=('JetBrains Mono', 20),
    width=1919,
    height=973
)
entry_1.place(
    x=0.0,
    y=42.0,
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    959.0,
    21.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_1.place(
    x=20.0,
    y=17.0,
    width=28.014598846435547,
    height=8.137510299682617
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=saving,
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_2.place(
    x=279.0,
    y=7.0,
    width=28.01458740234375,
    height=28.029197692871094
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=opening,
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_3.place(
    x=425.0,
    y=7.0,
    width=28.01458740234375,
    height=28.029197692871094
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=cleaning,
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_4.place(
    x=138.0,
    y=7.0,
    width=28.014602661132812,
    height=28.029220581054688
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_5.place(
    x=567.0,
    y=6.0,
    width=32.0,
    height=31.438594818115234
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=window.quit,
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_6.place(
    x=1877.0,
    y=3.0,
    width=36.0,
    height=36.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_7.place(
    x=715.0,
    y=4.0,
    width=30.0,
    height=34.28571319580078
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_8.place(
    x=857.0,
    y=6.0,
    width=34.0,
    height=29.75
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=minus,
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_9.place(
    x=1069.0,
    y=2.0,
    width=38.0,
    height=38.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1054.0,
    21.0,
    image=image_image_2
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=plus,
    relief="flat",
    bg='#343434',
    activebackground='#343434'
)
button_10.place(
    x=1003.0,
    y=3.0,
    width=36.0,
    height=36.0
)

window.mainloop()
