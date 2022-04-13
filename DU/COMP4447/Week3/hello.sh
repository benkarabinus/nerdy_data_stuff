#!/bin/bash shell to use to tun this file
# first postional parameter
first_name=$1
# second postional parameter
last_name=$2
echo "Hello, $first_name, $last_name"
echo "Thank you for running $0"
echo "Now lets count a little with a for loop"
for i in $(seq 5)
do
echo $first_name
echo $iteration $i
done