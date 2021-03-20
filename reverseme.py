#!/usr/bin/env python

with open('coords.txt','r') as input:
        with open('output.txt','w') as output:
                for line in input:
                        line = line.strip()
                        data = line.split(',')
                        if len(data)>1:
                                output.write("%s,%s,0 "%(data[1],data[0]))
