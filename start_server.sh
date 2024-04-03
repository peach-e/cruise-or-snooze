#!/usr/bin/env bash
PROJECT_DIR=$(cd $(dirname $0) && pwd)
export PYTHONPATH="$PYTHONPATH:$PROJECT_DIR/python"
jupyter notebook --ip=127.0.0.1 --NotebookApp.token= --NotebookApp.password=
