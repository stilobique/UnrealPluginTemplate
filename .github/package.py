import glob
import os


def get_folder_name():
    addon = glob.glob(os.getcwd() + "/*/*.uplugin", recursive=True)

    return os.path.basename(os.path.dirname(addon[0]))


if __name__ == "__main__":
    name = get_folder_name()
    print(name)
