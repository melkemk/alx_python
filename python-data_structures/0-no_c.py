#!/usr/bin/env python3
def no_c(my_string):
    i=0
    newstring=''
    for i in  range(len(my_string)):
        if(my_string[i]!='c' and my_string[i]!='C'):
            newstring+=my_string[i]
    return newstring
