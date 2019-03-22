#!/bin/bash

cd ~/org
git clean -dfx
git checkout "$1"
make autoloads

cd /tmp/test
rm -f /tmp/test/scratch*.sh

bats *.bats
