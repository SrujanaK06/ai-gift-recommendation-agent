from typing import TypedDict


class GiftState(TypedDict):
    recipient: str
    age: int
    occasion: str
    interests: str
    budget: int
    relationship: str
    preferences: str
    delivery: str
    recommendations: str
