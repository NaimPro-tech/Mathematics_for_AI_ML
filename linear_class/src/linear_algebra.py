from abc import ABC, abstractmethod

class LinearAlgebra(ABC):

    @property
    @abstractmethod
    def shape(self):
        pass
