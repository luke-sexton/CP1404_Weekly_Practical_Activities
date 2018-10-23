import os
import shutil


def main():
    os.chdir('FilesToSort')
    directories = {}

    for filename in os.listdir('.'):
        list = filename.split('.')
        end_list = list[-1].lower()

        if end_list not in directories:
            directory = input("What category would you like to sort {} files into?".format(end_list)).title()
            directories[end_list] = directory

        try:
            os.mkdir(directories[end_list])
        except FileExistsError:
            pass

        shutil.move(filename, os.path.join(directories[end_list], filename))


main()
