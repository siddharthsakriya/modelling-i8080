#!/usr/bin/env bash

if [ "$1" == "interactive" ]; then
    python3 runner_interactive.py $2 > out.txt
    python3 helper.py out.txt result.txt
else
    python3 runner_binary.py $2 > out.txt
    python3 helper.py out.txt result.txt
fi


