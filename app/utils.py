from enum import IntEnum


class InstrumentTypes(IntEnum):
    GUITAR = 1
    DRUMS = 2
    BASS = 3
    KEYBOARDS = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class PlayingLevelTypes(IntEnum):
    MASTER = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
