import os
import pathlib
import sys
import zipfile
import shutil

from pathlib import Path


def read_token(file: str = 'token.txt') -> str:
    """From tests folder, return a token string, in a dedicated file"""
    token_file = Path(os.getcwd(), 'tests', file)
    with open(token_file, 'r') as f:
        token = f.read()

    return token


def generate_test_list():
    test_list = None
    if sys.argv:
        for arg in sys.argv:
            if '--test=' in arg:
                test_list = []
                items = arg.replace('--test=', '').split(',')
                for item in items:
                    test_list.append(item)

                return {'unreal': test_list}
            else:
                return ordering_test_file()
    else:
        return ordering_test_file()


def install_all_plugins(plugin: str, archives: [str]):
    """Config a folder with all plugins request"""
    clean_plugin_folder()
    shutil.copytree(Path(os.getcwd(), plugin), Path(os.getcwd(), 'tests', 'plugins', plugin))

    for archive in archives:
        with zipfile.ZipFile(archive) as f:
            f.extractall(Path(os.getcwd(), 'tests', 'plugins'))

    # TODO Add plugin in hard code, write an automatised way
    distant = Path(os.getcwd(), 'tests', 'unreal_sample', 'empty_project', 'Plugins')
    if distant.exists():
        shutil.rmtree(distant)
    shutil.copytree(Path(os.getcwd(), 'tests', 'plugins'), distant)


def ordering_test_file():
    unit_test_folder = pathlib.Path(os.getcwd(), "tests", "unit_tests")
    unit_test = os.listdir(unit_test_folder)
    unit_test_ue = []

    for test in unit_test:
        unit_test_ue.append(test)

    return {'unreal': unit_test_ue}


def clean_folders_and_archives(archives: list):
    """Removes all folders present in the plugins folder"""
    clean_plugin_folder()

    # TODO Remove with an hardcode way the plugin with the Unreal sample
    shutil.rmtree(Path(os.getcwd(), 'tests', 'unreal_sample', 'empty_project', 'Plugins'))
    for archive in archives:
        if Path(Path(os.getcwd(), archive)).exists():
            os.remove(Path(os.getcwd(), archive))


def clean_plugin_folder():
    for root, dirs, files in os.walk(Path(os.getcwd(), 'tests', 'plugins')):
        for folder in dirs:
            shutil.rmtree(Path(root, folder))
