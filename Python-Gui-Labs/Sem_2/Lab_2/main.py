import eel
from tkinter import *
from tkinter import filedialog
import json

eel.init('web')

A_set = set()
B_set = set()
relative_dict = {}

@eel.expose
def get_A():
    return [list(enumerate(A_set, start=1)), 'Множина А']


@eel.expose
def get_B():
    return [list(enumerate(B_set, start=1)), 'Множина В']


def writeIn(data):
    root = Tk()
    path = filedialog.asksaveasfilename(filetypes=[("Json", '*.json'), ("All files", "*.*")])
    if path is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        root.destroy()
        return False
    try:
        with open(path, 'w') as f:
            f.write(json.dumps(list(data)))
        root.destroy()
    except FileNotFoundError:
        root.destroy()
        return False

    return path


def readOut():
    root = Tk()
    path = filedialog.askopenfilename(initialdir="/",
                                      title="Select a File",
                                      filetypes=(("Text files",
                                                  "*.txt*"),
                                                 ("all files",
                                                  "*.*")))
    if path is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        root.destroy()
        return False

    with open(path) as f:
        data = json.load(f)
    root.destroy()

    return data


@eel.expose
def readA():
    data = readOut()
    if data:
        clear('A')
        A_set.update(set(data))
        return f'Зчитано А: {A_set}'
    return 'Error while reading A from file'


@eel.expose
def readB():
    data = readOut()
    if data:
        clear('B')
        B_set.update(set(data))
        return f'Зчитано B: {B_set}'
    return 'Error while reading B from file'


@eel.expose
def writeA():
    path = writeIn(A_set)
    if path:
        return f'Множину А збережено в {path}'

    return 'Множину А НЕ збережено'


@eel.expose
def writeB():
    path = writeIn(B_set)
    if path:
        return f'Множину B збережено в {path}'

    return 'Множину В НЕ збережено'


@eel.expose
def memorizeA(A):
    A_set.update(A)

    return f'A: {A_set}'


@eel.expose
def memorizeB(B):
    B_set.update(B)

    return f'B: {B_set}'


@eel.expose
def clear(some_set):
    if some_set == 'A':
        A_set.clear()

        return 'Множина А тепер не містить елементів'
    if some_set == 'B':
        B_set.clear()

        return 'Множина В тепер не містить елементів'


def is_women(name):
    if name[-1] == 'а' or name[-1] == 'я':
        return True
    return False


def split_gender(some_set):
    woman_arr, man_arr = [], []
    for name in some_set:
        if is_women(name):
            woman_arr.append(name)
            continue
        man_arr.append(name)
    return woman_arr, man_arr


def createR(A = A_set, B = B_set):
    woman_arr, man_arr = split_gender(A)
    woman_arr2, man_arr2 = split_gender(B)
    R = []

    for women in woman_arr:
        relative_dict[women] = []
        if len(man_arr2):
            man = man_arr2.pop()
            R.append((women, man))
            relative_dict[women].append(man)
        else:
            relative_dict[women].append('')

    relative_dict['B'] = list(B)
    relative_dict['A'] = list(A)
    relative_dict['R'] = R


def createS():
    B = relative_dict['B'].copy()
    S = []

    for women in relative_dict.keys():
        if not len(B):
            break

        if is_women(women):
            for name in B:
                if name in relative_dict[women]:
                    continue
                relative_dict[women].append(name)
                S.append((women, name))
                B.remove(name)
                break

    relative_dict['S'] = S
    return relative_dict


@eel.expose
def createRelative():
    global relative_dict
    relative_dict = {}

    createR()
    return createS()


@eel.expose
def getRelative():
    return relative_dict


@eel.expose
def union():
    return relative_dict["S"] + relative_dict["R"]


@eel.expose
def cross():
    result = []
    for arr in relative_dict["R"]:
        if arr in relative_dict["S"]:
            result.append(arr)

    return result


@eel.expose
def difference():
    R = relative_dict["R"]
    for arr in R:
        if arr in relative_dict["S"]:
            R.remove(arr)

    return R


@eel.expose
def inverse():
    S = relative_dict["S"]
    result = []
    for arr in S:
        new_arr = list(arr)
        new_arr.reverse()
        result.append(new_arr)
    return result


@eel.expose
def addition():
    U = relative_dict["R"] + relative_dict["S"]
    for arr in relative_dict["R"]:
        if arr in U:
            U.remove(arr)

    return U


eel.start('index.html')
