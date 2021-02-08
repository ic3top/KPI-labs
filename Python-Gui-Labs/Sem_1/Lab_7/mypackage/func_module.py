import os


def dir_maker(way, mess="WARN: catalog already exists!"):
    try:
        os.mkdir(way)
        print(f"was created: {way}")
    except FileExistsError:
        print(mess)