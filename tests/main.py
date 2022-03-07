import enum

from utils.unreal import get_unreal_plugins_dependency
from utils.container import VirtualMachine
from utils.misc import generate_test_list, install_all_plugins, clean_folders_and_archives
from utils.properties import ContainerObject


class Container(enum.Enum):
    """Enumerate about the Geometry node"""
    UNREAL = ContainerObject(name='Unreal', image='ghcr.io/epicgames/unreal-engine')


def launch_unit_test(test: [str] = None):
    """Start all Unit Test, Blender and Unreal if needed"""
    vm_ue = VirtualMachine(Container.UNREAL.value)
    vm_ue.launch_unit_test(tests=test['unreal'])


if __name__ == '__main__':
    # Initialize Variable and module request
    archives = []

    # Prepare Blender and Unreal dependency
    get_unreal_plugins_dependency(archives)
    install_all_plugins(plugin='unreal_pipeline', archives=archives)

    # Launch Unit Test
    launch_unit_test(test=generate_test_list())

    # Clear archive file and folder generated
    clean_folders_and_archives(archives=archives)
