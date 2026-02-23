# core/ui.py
from utils.formatting import euro, km, litre

class UI:
    @staticmethod
    def format_value(value, unit=None):
        if unit == "€":
            return euro(value)
        elif unit == "L":
            return litre(value)
        elif unit == "km":
            return km(value)
        else:
            return str(value)