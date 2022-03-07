import os
import json

from pathlib import Path
from .forge import get_release_file


class ErrorTest(Exception):
    """ Failed to generate the test """


def get_unreal_plugins_dependency(addon: list):
    """From Github, get all Unreal plugins request to make Unit Test and install-it"""
    dependency = Path(os.getcwd(), "tests", "dependency.json")
    with open(dependency) as f:
        data = json.load(f)

    unreal_plugins = data['unreal']
    for key, value in unreal_plugins.items():
        get_release_file(value[0], value[1])
        addon.append(value[0])
