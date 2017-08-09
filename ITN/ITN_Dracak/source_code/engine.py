#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import config

def scene( dialogue ):
    for i, elem in enumerate( dialogue ):
        print(elem)

        if (len(elem)/10) > 5:
            sleep_time = 5
        else:
            sleep_time = len(elem)/10
            
        time.sleep( sleep_time )

def options( question, options, callback ):
    for i, elem in enumerate( options ):
        print('%d - %s' % (i+1, elem))

    health = True
    
    while health:
        choise = input( question )
        
        if (not choise.isdigit()) or (int(choise) > int(len(options)) or (int(choise) < 1)):
            print(config.illegal_choice)
        else:
            health = False
            callback[ int(choise) - 1 ]()

def get( question ):
    data = input( question )
    return data
