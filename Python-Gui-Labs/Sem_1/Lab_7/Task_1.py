import os, pickle, shutil, shelve, re
from mypackage.func_module import dir_maker
from mypackage.Lab_5 import solar_system as ss
from mypackage.Lab_6 import planets_lst as planets
letter = str(input("Input a random letter: "))
while len(letter) != 1:
    letter = str(input("Input a random letter: "))
# task 1 & 2
dir_maker(r"C:\lab_7")
dir_maker(r"C:\lab_7\Herchuk")
try:
    shutil.move("8.txt", r"C:\lab_7\Herchuk")
    print("8.txt was successfully moved  to the directory\n")
except Exception:
    print("\nFile has been already moved!")
# task 3
with open(r"C:\lab_7\Herchuk\8.txt", "r") as main:
    full_text = main.read()
    data_sen = sorted(full_text.replace("\n", " ").split("."), key=lambda x: len(x.replace(" ", "")))
    with open("C:\lab_7\Herchuk\81.txt", 'w') as saver_sen:
        i = 1
        for sentence in data_sen:
            if len(sentence) > 2:
                saver_sen.write(f"{i}) {sentence.strip()}\n")
                i += 1
    with open("C:\lab_7\Herchuk\82.txt", 'w') as saver_words:
        data_words = re.findall((r"( {}[а-я]+ )".format(letter)), full_text, re.IGNORECASE)
        for word in data_words:
            word.replace(" ", "")
            saver_words.write(f"{word}\n")
# task 4
dir_maker(r"C:\lab_5")
with open(r"lab5.txt", "wb") as lab5:
    pickle.dump(ss, lab5)

try:
    shutil.move("lab5.txt", r"C:\lab_5")
    print("lab5.txt was successfully moved  to the directory)\n")
except Exception:
    print("\nFile has been already moved!")

try:
    os.rename("C:\lab_5\lab5.txt",r"C:\lab_5\updated_lab5.txt")
except Exception:
    print("already renamed")

with open(r"C:\lab_5\updated_lab5.txt", "rb") as lb5:
    lb5 = pickle.load(lb5).update({"Pluto": "ceased to be called a planet in 2006"})

    try:
        shutil.move("updated_lab5.txt", r"C:\lab_5")
        print("updated_lab5.txt was successfully updated\n")
    except Exception:
        print("File has been already moved\n")
# task 5
dir_maker(r"C:\lab6")
with shelve.open("C:\lab6\lab6.txt", flag="n") as lb6:
    i = 0
    for planet in planets:
        lb6[f"{i}"] = [planet.name]
        i += 1
    lb6.update({"Pluto": "ceased to be called a planet in 2006"})
    lb6.popitem()
    lb6.update({"Enthrum": "Never discovered"})
    for key in lb6:
        print(key, " - ", lb6[key])
