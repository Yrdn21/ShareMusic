from enum import Enum

class Edition(str, Enum):
    STANDARD = "Standard"
    SPECIAL = "Special"
    DELUXE = "Deluxe"
    REMASTER = "Remaster"
    LIVE = "Live"