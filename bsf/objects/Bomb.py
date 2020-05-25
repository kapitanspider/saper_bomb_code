#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pygame.locals import *
import random



class Bomb:
    def __init__(self, time, type):

        self.time = time
        self.type = type
        self.code = []
        for i in range(3):
            self.code.append(random.randint(0, 1796))

    def tick(self):
        if self.time > 0:
            self.time = self.time - 1

    def priority(self):
        return self.time