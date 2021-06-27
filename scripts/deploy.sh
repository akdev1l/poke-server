#!/bin/bash

./setup.py clean
./setup.py build
./setup.py bdist --format=rpm

scp dist/poke-server-1.0-1.noarch.rpm root@poke-back.hq.akdev.xyz:/tmp

ssh root@poke-back.hq.akdev.xyz dnf remove -y poke-server
ssh root@poke-back.hq.akdev.xyz dnf install -y /tmp/poke-server-1.0-1.noarch.rpm
