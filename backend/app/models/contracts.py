from enum import Enum


class ContractType(str, Enum):

    CALL = "CALL"

    PUT = "PUT"

    DIGITOVER = "DIGITOVER"

    DIGITUNDER = "DIGITUNDER"

    DIGITODD = "DIGITODD"

    DIGITEVEN = "DIGITEVEN"

    DIGITMATCH = "DIGITMATCH"

    DIGITDIFF = "DIGITDIFF"

    RISE = "CALL"

    FALL = "PUT"