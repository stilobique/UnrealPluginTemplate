![Static Badge](https://img.shields.io/badge/3.9.7-brightgreen?style=flat-square&logo=python&labelColor=yellow&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-397%2F)
![Static Badge](https://img.shields.io/badge/5.0.3-brightgreen?style=flat-square&logo=unrealengine&labelColor=black&link=https%3A%2F%2Fwww.unrealengine.com)

# Unreal Plugin Template
This repository is a template to make a new Unreal Engine plugin (blueprint/python only, but can be easily converted to be a C++).

Any official Epic plugins are request to work:

|           Plugins             |
|:-----------------------------:|
| Editor Scripting Utilities    |
| Python Editor Script Plugin   |
| PythonAutomationTest          |


# Improvement
More improvement are in the pipe, a real support and documentation with the Unit Test, maybe the C++ version and easily package setup... and more.


# How to start
Quickly change this file and folder:
- `unreal_plugin_folder`: your plugin folder name
- `unreal_plugin_folder\unreal_plugin_name.uplugin`. your unreal plugin, and edit this content. It's a json and can be edit with notepad.
- `unreal_plugin_folder\Resources\Icon128.png` a small thumbnail draw inside unreal editor.
