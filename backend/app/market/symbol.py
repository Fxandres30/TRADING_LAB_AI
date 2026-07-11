from dataclasses import dataclass


@dataclass(slots=True)
class Symbol:

    # Broker
    broker: str

    # Nombre interno
    name: str

    # Nombre que usa el broker
    broker_symbol: str

    # Nombre visible
    display_name: str

    # Tipo
    market: str
    category: str

    # Precio
    digits: int
    pip: float

    # Estado
    tradable: bool = True

    # Sesión
    exchange_open: bool = True