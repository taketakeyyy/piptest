# -*- coding: utf-8 -*-

class Dog():
    def __init__(self, _name):
        self._name = _name

    @property
    def name(self):
        return self._name

    def bark(self):
        print(f"Bow! Bow name is {self.name}!")