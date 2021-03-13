from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import random
A, B, C, D = set(), set(), set(), set()

# deleting output
def deleter():
    global outputA, outputB, outputC
    outputA.set(""), outputC.set(""), outputB.set("")


# randomly set creating
def generate_array():
    deleter()
    global A, B, C
    size_A = int(entry_A.get())
    size_B = int(entry_B.get())
    size_C = int(entry_C.get())
    arr_size = [size_A, size_B, size_C]
    start_rand = int(range_array1.get())
    end_rand = int(range_array2.get())
    # перевірка для правильного працювання алгоритму.
    for el in arr_size:
        if el > abs(end_rand - start_rand):
            outputA.set("Range is too low!")
            outputB.set("Range is too low!")
            outputC.set("Range is too low!")
            return 0

    A = {random.randint(start_rand, end_rand) for i in range(size_A)}
    while (len(A)< size_A):
        A.add(random.randint(start_rand,end_rand))
    B = {random.randint(start_rand, end_rand) for i in range(size_B)}
    while (len(B) < size_B):
        B.add(random.randint(start_rand,end_rand))
    C = {random.randint(start_rand, end_rand) for i in range(size_C)}
    while (len(C) < size_C):
        C.add(random.randint(start_rand,end_rand))
    outputA.set(A)
    outputB.set(B)
    outputC.set(C)


def manual_input():
    deleter()
    global A, B, C
    # arrayA_man = entry_A1.get()
    # arrayB_man = entry_B1.get()
    # arrayC_man = entry_C1.get()
    A = {int(i) for i in entry_A1.get().split(',')}
    B = {int(i) for i in entry_B1.get().split(',')}
    C = {int(i) for i in entry_C1.get().split(',')}
    outputA.set(A)
    outputB.set(B)
    outputC.set(C)


def chooser():
    open_calc()
    if radio_var.get() == 0:
        generate_array()
    else:
        manual_input()

# toplevel windows opening
# Calculations window for A B C D
def open_calc():
    global imD
    calc = Toplevel(master)
    calc.title("Calculations")
    calc.resizable(0, 0)
    calc.grab_set()
    def count():
        global A, B, C, D
        print(f"{A}\n{B}\n{C}")
        U = set()
        U.update(A | B | C)
        D = (((A & (U - B)) | (B & (U - A))) & (C | B) & C)
        outputD.set(D)
        first.config(text=f"{A & (U - B)}")
        sec.config(text=f"{B & (U - A)}")
        thrd.config(text=f"{(A & (U - B)) | (B & (U - A))}")
        four.config(text=f"{(C | B)}")
        five.config(text=f"{((A & (U - B)) | (B & (U - A))) & (C | B)}")
        six.config(text=f"{D}")

    # saving D
    def save():
        file_name = filedialog.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                    ("HTML files", "*.html;*.htm"),
                                                    ("All files", "*.*")))
        f = open(file_name, 'w')
        s = outputD.get()
        f.write(s)
        f.close()


    Label(calc, width=40, height=2, bg="#d6d4d3", text="Результати: ", relief="ridge")\
        .grid(row=0, column=1, pady=5)
    Label(calc, width=20, height=2, bg="#d6d4d3", text="Множина А:", relief="solid")\
        .grid(row=1, column=0, pady=5)
    Label(calc, width=50, height=2, bg="#ffffff", textvariable=outputA, relief="solid")\
        .grid(row=2, column=0, pady=5, padx=(5, 5))
    Label(calc, width=20, height=2, bg="#d6d4d3", text="Множина B:", relief="solid")\
        .grid(row=1, column=1, pady=5)
    Label(calc, width=50, height=2, bg="#ffffff", textvariable=outputB, relief="solid")\
        .grid(row=2, column=1, pady=5, padx=(5, 5))
    Label(calc, width=20, height=2, bg="#d6d4d3", text="Множина C:", relief="solid")\
        .grid(row=1, column=2, pady=5)
    Label(calc, width=50, height=2, bg="#ffffff", textvariable=outputC, relief="solid")\
        .grid(row=2, column=2, pady=5, padx=(5, 5))

    Label(calc, width=40, height=2, bg="#d6d4d3", text="Множина D:", relief="ridge")\
        .grid(row=3, column=0, pady=5)
    imD = ImageTk.PhotoImage(Image.open("formula.png"))
    Label(calc, image=imD, relief="ridge", compound=TOP)\
        .grid(row=4, column=0, pady=5)
    Button(calc, text="Згенерувати множину D", width=40, height=2, bg="#d6d4d3", relief="raised", command=count)\
        .grid(row=5, column=0, pady=5)

    Label(calc, width=30, height=2, bg="#ffffff", textvariable=outputD, relief="solid")\
        .grid(row=6, column=0, pady=5, ipady=2)
    Button(calc, text="Зберегти множину D", width=40, height=2, bg="#d6d4d3", relief="raised", command=save)\
        .grid(row=7, column=0, pady=5)

    Label(calc, width=40, height=2, bg="#d6d4d3", text="Послідовні дії:", relief="solid")\
        .grid(row=3, column=1, pady=5, columnspan=2)

    # six actions
    Label(calc, width=20, height=2, bg="#d6d4d3", text="A ∪ not(B) = G", relief="solid")\
        .grid(row=4, column=1, pady=5)
    Label(calc, width=20, height=2, bg="#d6d4d3", text="B ∩ not(A) = G2", relief="solid")\
        .grid(row=5, column=1, pady=5)
    Label(calc, width=20, height=2, bg="#d6d4d3", text="G ∪ G2 = Z", relief="solid")\
        .grid(row=6, column=1, pady=5)
    Label(calc, width=20, height=2, bg="#d6d4d3", text="C ∪ B = Y", relief="solid")\
        .grid(row=7, column=1, pady=5)
    Label(calc, width=20, height=2, bg="#d6d4d3", text="Z ∩ Y = R", relief="solid")\
        .grid(row=8, column=1, pady=5)
    Label(calc, width=20, height=2, bg="#d6d4d3", text="R ∩ C", relief="solid")\
        .grid(row=9, column=1, pady=5)
    # output results
    first = Label(calc, width=40, height=2, bg="#ffffff", text="", relief="solid")
    first.grid(row=4, column=2, pady=5)
    sec = Label(calc, width=40, height=2, bg="#ffffff", text="", relief="solid")
    sec.grid(row=5, column=2, pady=5)
    thrd = Label(calc, width=40, height=2, bg="#ffffff", text="", relief="solid")
    thrd.grid(row=6, column=2, pady=5)
    four = Label(calc, width=40, height=2, bg="#ffffff", text="", relief="solid")
    four.grid(row=7, column=2, pady=5)
    five = Label(calc, width=40, height=2, bg="#ffffff", text="", relief="solid")
    five.grid(row=8, column=2, pady=5)
    six = Label(calc, width=40, height=2, bg="#ffffff", text="", relief="solid")
    six.grid(row=9, column=2, pady=5)

def open_last():
    global imF
    last = Toplevel(master)
    last.title("Calculations")
    last.resizable(0, 0)
    last.grab_set()
    def generate_last():
        outputF.delete(0, END)
        rangeF = len(D)
        minD = min(D)
        maxD = max(D)
        arrayF = {random.randint(minD, maxD) for i in range(rangeF)}
        while (len(arrayF) < len(D)):
            arrayF.add(random.randint(minD, maxD))
        print(arrayF)
        arrayF.remove(min(arrayF))
        arrayF.remove(max(arrayF))
        arrayF.add(minD)
        arrayF.add(maxD)
        print(arrayF)
        outputF.insert(0, arrayF)

    def calc_x():
        U = set()
        F = {int(i) for i in outputF.get().replace("{", "").replace("}", "").split(', ')}
        U.update(F | D)
        print(U)
        print(U - F)
        X = (U - F) | (U - D)
        outputX.insert(0, X)

    Label(last, width=40, height=2, bg="#d6d4d3", text="Множина D:", relief="ridge")\
        .grid(row=0, column=0, pady=5, padx=5)
    Label(last, width=30, height=2, bg="#ffffff", textvariable=outputD, relief="solid")\
        .grid(row=1, column=0, pady=5, ipady=2)
    Button(last, text="Згенерувати множину F", width=40, height=2, bg="#d6d4d3", relief="raised", command=generate_last)\
        .grid(row=0, column=2, pady=5, columnspan=2, padx=5)
    outputF = Entry(last, width=30, relief="solid")
    outputF.grid(row=1, column=2, pady=5, ipady=2, columnspan=2)
    # set X
    Label(last, width=40, height=2, bg="#d6d4d3", text="Множина X:", relief="ridge")\
        .grid(row=3, column=0, pady=5, padx=5, columnspan=2)
    imF = ImageTk.PhotoImage(Image.open("formula_2.png"))
    Label(last, image=imF, relief="ridge", compound=TOP)\
        .grid(row=4, column=0, pady=5, columnspan=2)
    Button(last, text="Згенерувати множину X", width=40, height=2, bg="#d6d4d3", relief="raised", command=calc_x)\
        .grid(row=5, column=0, pady=5, columnspan=2, padx=5)
    outputX = Entry(last, width=30, relief="solid")
    outputX.grid(row=6, column=0, pady=5, ipady=2, columnspan=2)


# info opening
def open_info(top):
    info = Toplevel(top)
    info.title("Information")
    info.grab_set()
    Label(info, width=15, height=2, bg="#ffffff", text="П. І. Б: ", relief="solid")\
        .grid(row=0, column=4, pady=5, padx=(10, 10))
    Label(info, width=30, height=2, bg="#ffffff", text="Герчук Володимир Дмитрович", relief="groove")\
        .grid(row=0, column=5, pady=5, padx=(10, 10))
    Label(info, width=15, height=2, bg="#ffffff", text="Номер групи:", relief="solid")\
        .grid(row=1, column=4, pady=5, padx=(10, 10))
    Label(info, width=20, height=2, bg="#ffffff", text="ІО-02", relief="groove")\
        .grid(row=1, column=5, pady=5, padx=(10, 10))
    Label(info, width=15, height=2, bg="#ffffff", text="Номер у списку:", relief="solid")\
        .grid(row=2, column=4, pady=5, padx=(10, 10))
    Label(info, width=20, height=2, bg="#ffffff", text="08", relief="groove")\
        .grid(row=2, column=5, pady=5, padx=(10, 10))


# main
master = Tk()
master.title("Set Counter")
master.configure(bg="#F8F8FF")
master.resizable(0, 0)

# result A B C D
outputD = StringVar()
outputA = StringVar()
outputB = StringVar()
outputC = StringVar()
# Info button
btn = Button(master, text="Info", height=2, bg="#d6d4d3", command=open_info)\
    .grid(row=0, column=6, pady=5, padx=5)
# A B C input for randomly generation
Label(master, width=20, height=2, bg="#d6d4d3", text="Множина А:", relief="solid")\
    .grid(row=1, column=2, pady=5)
entry_A = Entry(master, width=30, relief="groove")
entry_A.grid(row=1, column=3, pady=5, ipady=2, padx=(2, 50))
Label(master, width=20, height=2, bg="#d6d4d3", text="Множина B:", relief="solid")\
    .grid(row=2, column=2, pady=5)
entry_B = Entry(master, width=30, relief="groove")
entry_B.grid(row=2, column=3, pady=5, ipady=2, padx=(2, 50))
Label(master, width=20, height=2, bg="#d6d4d3", text="Множина C:", relief="solid")\
    .grid(row=3, column=2, pady=5)
entry_C = Entry(master, width=30, relief="groove")
entry_C.grid(row=3, column=3, pady=5, ipady=2, padx=(2, 50))
Label(master, width=20, height=2, bg="#d6d4d3", text="Діапазон чисел ВІД:", relief="solid")\
    .grid(row=4, column=2, pady=5)
range_array1 = Entry(master, width=30, relief="groove")
range_array1.grid(row=4, column=3, pady=5, ipady=2, padx=(2, 50))
Label(master, width=20, height=2, bg="#d6d4d3", text="ДО:", relief="solid")\
    .grid(row=5, column=2, pady=5)
range_array2 = Entry(master, width=30, relief="groove")
range_array2.grid(row=5, column=3, pady=5, ipady=2, padx=(2, 50))
# A B C input
Label(master, width=20, height=2, bg="#d6d4d3", text="Множина А:", relief="solid")\
    .grid(row=1, column=0, pady=5)
entry_A1 = Entry(master, width=30, relief="groove")
entry_A1.grid(row=1, column=1, pady=5, ipady=2, padx=(2, 50))
Label(master, width=20, height=2, bg="#d6d4d3", text="Множина B:", relief="solid")\
    .grid(row=2, column=0, pady=5)
entry_B1 = Entry(master, width=30, relief="groove")
entry_B1.grid(row=2, column=1, pady=2, ipady=2, padx=(2, 50))
Label(master, width=20, height=2, bg="#d6d4d3", text="Множина C:", relief="solid")\
    .grid(row=3, column=0, pady=5)
entry_C1 = Entry(master, width=30, relief="groove")
entry_C1.grid(row=3, column=1, pady=5, ipady=2, padx=(2, 50))
# Radio-buttons
radio_var = BooleanVar()
radio_var.set(0)
r1 = Radiobutton(text="Генерація випадкових множин", variable=radio_var, value=0, relief="ridge", width=40, height=2, bg="#d6d4d3")\
    .grid(row=0, column=2, pady=5, columnspan=2)
r2 = Radiobutton(text="Ввести множини", variable=radio_var, value=1, relief="ridge", width=40, height=2, bg="#d6d4d3")\
    .grid(row=0, column=0, pady=5, columnspan=2)


# creating sets - A B C
b_generate = Button(text="Згенерувати множини", width=40, height=2, bg="#d6d4d3", relief="raised", command=chooser)\
    .grid(row=6, column=1, pady=5)
# F - generating
b_last = Button(text="Згенерувати множину F", width=40, height=2, bg="#d6d4d3", relief="raised", command=open_last)\
    .grid(row=6, column=2, pady=5, columnspan=2)



master.mainloop()
