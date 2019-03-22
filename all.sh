#!/bin/bash

set -e

cd /tmp/test

# expect pass
./run.sh 57d8b68d9594d4e23d5f4960073a1cac78bc72e3~1

# expect fail
./run.sh master
