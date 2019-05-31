#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class product:
    def __init__(self, name, price, number, index):
        self.name = name
        self.price = price
        self.number = number
        self.index = index

    def __str__(self):
        return 'name:%s,price:%s,numde:%s,index:%s' % (self.name, self.price, self.number, self.index)