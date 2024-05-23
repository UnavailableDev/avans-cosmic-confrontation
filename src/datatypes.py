# from typing import NamedTuple
from dataclasses import dataclass

@dataclass
class Position:
   x: int
   y: int
   horizontal: bool = True
