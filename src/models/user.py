from typing import TypedDict

from ..remote.protobuf.common import User_pb2

__all__ = ("User",)


class User:
    __slots__ = ("id", "name", "name_show", "portrait", "level_id")

    def __init__(
        self, *, id: int, name: str, name_show: str, portrait: str, level_id: int
    ):
        self.id = id
        self.name = name
        self.name_show = name_show
        self.portrait = portrait
        self.level_id = level_id

    @classmethod
    def from_protobuf(cls, pb: User_pb2.User):
        return cls(
            id=pb.id,
            name=pb.name,
            name_show=pb.name_show,
            portrait=pb.portrait,
            level_id=pb.level_id,
        )

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __repr__(self):
        return f"User({self.id}:{self.name_show}[Lv.{self.level_id}])"
