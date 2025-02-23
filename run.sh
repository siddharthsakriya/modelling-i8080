#!/usr/bin/env bash

if [ "$1" == "i" ]; then
    python3 runner_interactive.py "$2" > out.txt
    python3 helper.py out.txt result.txt
elif [ "$1" == "b" ]; then
    python3 runner_binary.py "$2" "$3" > out.txt
    if [ "$3" == "e" ]; then
        python3 helper.py out.txt result.txt
    fi
fi
