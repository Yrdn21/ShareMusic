from enum import Enum, auto


class ActiveStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"