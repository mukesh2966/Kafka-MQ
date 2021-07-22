#!/bin/bash

cd /mnt/c/mk1/uploads
python3 -m venv env
activate () {
 . ./env/bin/activate
}
activate

pip3 install sklearn
