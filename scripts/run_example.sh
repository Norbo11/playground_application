#!/bin/bash
python threaded_example.py $1 $2 &
PID=$!
echo "Running pyflame-bleeding -p $PID ${@:3} > output_$1_$2.txt"
pyflame-bleeding -p $PID ${@:3} > output_$1_$2.txt
cat output_$1_$2.txt | flamegraph.pl > diagram_$1_$2.svg
wait $PID

