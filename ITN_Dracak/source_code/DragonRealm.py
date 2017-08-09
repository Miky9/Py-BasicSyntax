#!/usr/bin/python
# -*- coding: utf-8 -*-
import scenes
import config

running = True

while running:
    scenes.intro()

    again = input( config.try_again + ' (Y/N):');
    if again.lower() == 'y':
        running = True
    if again.lower() == 'n':
        running = False

print( config.thanks )
input('Press enter to exit...')
