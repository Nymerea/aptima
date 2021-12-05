#!bin/bash

echo "will compile $1"
cmd="cp $1 $1x"
echo $cmd
$cmd
cmd="cython $1x --embed"
echo $cmd
$cmd
cmd="gcc -Os -I /usr/include/python3.8 -o ${1:0:${#1}-3} ${1:0:${#1}-3}.c -lpython3.8 -lpthread -lm -lutil -ldl"
echo $cmd
$cmd
