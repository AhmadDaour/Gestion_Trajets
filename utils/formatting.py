from typing import Union

def number(value: Union[int, float, str], decimals: int = 2, thousand_sep: str = " ") -> str:
    """Format français : espace pour milliers, virgule pour décimales"""
    try:
        num = round(float(value), decimals)
    except (ValueError, TypeError):
        return str(value)
    formatted = f"{num:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", thousand_sep)
    return formatted

def euro(value: Union[int, float, str]) -> str:
    return number(value, 2) + " €"

def km(value: Union[int, float, str]) -> str:
    return number(value, 0) + " km"

def litre(value: Union[int, float, str]) -> str:
    return number(value, 2) + " L"