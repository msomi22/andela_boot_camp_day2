#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Car class that instantiate various vehicles
"""


class Car(object):

    """
    Attributes:
    name: Name representing the name of a Vehicle
    model: Model representing the model of a Vehicle
    car_type: Type representing the type of a Vehicle 
    """

    num_of_wheels = 0
    num_of_doors = 0
    speed = 0

    def __init__(self, name='General', model='GM', car_type=''):
        self.name = name
        self.model = model
        self.car_type = car_type
        if self.name == 'Opel':
            self.num_of_doors = 4
        elif self.name == 'Porshe':
            self.num_of_doors = 2
        elif self.name == 'Koenigsegg':
            self.num_of_doors = 2
            self.num_of_wheels = 4
        elif self.name == 'MAN':
            self.num_of_wheels = 8
            self.speed = 0

    def is_saloon(self):
        if self.car_type == 'trailer':
            return True 
        else:
            return 'The car type should be saloon if it is not a trailer'

    def drive(self, arg):
        if self.name == 'MAN':
            self.speed = arg * 11
            return self
        elif self.name == 'Mercedes':
            self.speed = int(1000 * arg / 3)
            return self


