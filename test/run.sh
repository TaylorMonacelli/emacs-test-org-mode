#!/bin/bash

find . -maxdepth 1 -type f -name 'test*.sh' |
    grep -v test.sh |
    while read script; do
        bash $script
    done

find . -maxdepth 1 -name 'test*' -type d |
    while read test_dir; do
        cat <<'__eot__' >$test_dir.bats
@test "$test_dir" {
	result="$(find $test_dir -type f -name '*.sh' | wc -l)"
	[ "$result" -eq 2 ]
}
__eot__
        perl -i'' -pe 's{\$test_dir}{'$test_dir'}' $test_dir.bats
    done
