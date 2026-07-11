from enum import IntEnum


class TimeFrame(IntEnum):

    M1 = 60
    M5 = 300
    M15 = 900
    M30 = 1800

    H1 = 3600
    H4 = 14400

    D1 = 86400

    @classmethod
    def from_string(cls, value: str):

        return cls[value.upper()]