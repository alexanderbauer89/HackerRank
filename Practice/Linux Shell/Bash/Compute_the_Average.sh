#!/bin/bash
read N
for _ in $(eval echo "{1..$N..1}")
do
    read number
    sum=$(($sum + $number))
done
printf "%.3f" $(echo $sum/$N | bc -l)
