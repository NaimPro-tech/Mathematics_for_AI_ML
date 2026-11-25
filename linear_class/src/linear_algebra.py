from abc import ABC, abstractmethod
import copy

class LinearAlgebra(ABC):

    @property
    @abstractmethod
    def shape(self):
        pass

class Vector(LinearAlgebra):

    def __init__(self, vector):
        self.vector = copy.deepcopy()

