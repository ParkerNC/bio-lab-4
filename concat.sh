#!/bin/bash

for i in $(find ./dat -type f)
do
    cat $i >> "data_booth.csv"
done