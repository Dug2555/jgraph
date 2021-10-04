#!/bin/bash

python Main.py

for file in ./Moves/*
	do
		./jgraph -P $file | ps2pdf - | convert -density 300 - -quality 100 $file.jpg 
	done

convert -delay 100 -loop 0   Moves/*.jpg out.gif  
