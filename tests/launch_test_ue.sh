#!/bin/bash
/home/ue4/UnrealEngine/Engine/Binaries/Linux/UE4Editor-Cmd "$1" \
  -stdout \
  -nullrhi \
  -run=pythonscript \
  -script="$2" \
  -ExecCmds="Quit" || exit 1