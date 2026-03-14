from pydantic import BaseModel


class MazeConfig(BaseModel):
    width: int
    height: int
    entry: int
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int | None = None
