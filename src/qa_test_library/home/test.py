from dataclasses import dataclass, field


@dataclass
class HomeTest:
    name: str
    label: str = ""
    isbn: str = ""
    tags: list[str] = field(default_factory=list)
