# utils/formatting.py
from typing import Union

def format_currency(
    value: Union[int, float, str],
    currency: str = "€",
    decimal_places: int = 2,
    thousand_sep: str = " "
) -> str:
    
    try:
        num = float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Impossible de convertir {value} en nombre.")

    # Formate avec décimales et séparateur de milliers
    formatted_value = f"{num:,.{decimal_places}f}".replace(",", "X").replace(".", ",").replace("X", thousand_sep)
    return f"{formatted_value} {currency}"
