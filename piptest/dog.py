# -*- coding: utf-8 -*-

class Dog():
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    def bark(self):
        print(f"Bow! Bow name is {self.name}!")