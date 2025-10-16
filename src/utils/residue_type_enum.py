from enum import Enum

class ResidueTypeEnum(Enum):
    PAPER = 0
    PLASTIC = 1
    GLASS = 2
    METAL = 3

    @staticmethod
    def is_valid(tipo):
        return tipo in [item.value for item in ResidueTypeEnum]