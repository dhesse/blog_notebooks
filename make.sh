#!/usr/bin/env bash

pyenv exec python -m jupyter nbconvert $1 --to markdown
pyenv exec python blogify.py $1


