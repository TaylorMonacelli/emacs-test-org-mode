#!/bin/bash

[[ -x /usr/local/bin/bats ]] && exit

git clone --depth 1 https://github.com/sstephenson/bats.git /usr/local/src/bats
cd /usr/local/src/bats
./install.sh /usr/local
