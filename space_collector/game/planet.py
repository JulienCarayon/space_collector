from dataclasses import dataclass


@dataclass
class Planet:
    x: int
    y: int
    size: int
    id: int
    collected_by: int = -1

    def state(self) -> dict:
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "collected_by": self.collected_by,
        }
