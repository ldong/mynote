#!/bin/bash

cd $(dirname $0)

python server/main.py --static-file-path=./static --template-file-path=./template --notes-file-path=../notes

