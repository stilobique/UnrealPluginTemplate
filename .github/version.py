import os
import re
import sys
import glob

from pathlib import Path


class SetupVersion:
    def __init__(self, version: str):
        self.addon_file = Path(self.get_plugin_file())
        self.tag = version.replace('--tag=', '')
        self.update_addon_init()

    def update_addon_init(self):
        """Simple function to update the bl_info to set the Git tag release"""
        regex, update = r'[0-9]{1,2}\.[0-9]{1,2}\.[0-9{1,2}]', ''

        try:
            with open(self.addon_file, "r") as f:
                i = 0
                lines = f.readlines()
                for line in lines:
                    if '\t"VersionName":' in line:
                        print('Actual set : ', line)
                        line = re.sub(regex, self.tag, line)
                        lines[i] = line
                        update = lines
                        print('Update version : ', line)
                        break
                    i += 1

            with open(self.addon_file, 'w') as f:
                f.writelines(update)

        except FileNotFoundError as exception:
            print(f'Can\'t find a file :\n\t{exception}')

    @staticmethod
    def get_plugin_file():
        file = glob.glob(os.getcwd() + "/*/*.uplugin", recursive=True)
        return file[0]


class SetupError(Exception):
    """No tag or folder name valid"""
    pass


if __name__ == "__main__":
    tag: str = ''

    for value in sys.argv:
        if '--tag' in value:
            tag = value.replace('--tag=v', '')

    try:
        if not tag:
            raise SetupError
        else:
            print(f'[UpdateVersion] Set the tag "{tag}".')
            bump = SetupVersion(version=tag)

    except SetupError:
        print(SetupError.__doc__)
        sys.exit(1)
