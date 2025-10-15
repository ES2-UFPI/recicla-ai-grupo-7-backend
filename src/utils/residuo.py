from enum import Enum

class Residuo(Enum):
    PAPEL = 0
    PLASTICO = 1
    VIDRO = 2
    METAL = 3

    @staticmethod
    def is_valid(tipo):
        return tipo in [item.value for item in Residuo]