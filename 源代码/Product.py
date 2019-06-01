<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class product:
    def __init__(self, name, price, number, index):
        self.name = name
        self.price = price
        self.number = number
        self.index = index

    def __str__(self):
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class product:
    def __init__(self, name, price, number, index):
        self.name = name
        self.price = price
        self.number = number
        self.index = index

    def __str__(self):
>>>>>>> 5fe40353c98a751d8986a82087b7b574f0221770
        return 'name:%s,price:%s,numde:%s,index:%s' % (self.name, self.price, self.number, self.index)