#!/usr/bin/bash

a=$(echo 100 | ./root.py)
[ "$a" = "Not Prime" ]
echo $?

a=$(echo 71 | ./root.py)
[ "$a" = "Prime" ]
echo $?

a=$(echo 10 | ./root.py)
[ "$a" = "Not Prime" ]
echo $?

a=$(echo 17 | ./root.py)
[ "$a" = "Prime" ]
echo $?
