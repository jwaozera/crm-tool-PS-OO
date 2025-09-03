from datetime import datetime
from .base import Serializavel

class EmailCampanha(Serializavel):
    def __init__(self, title, description, target_stage):
        self.title = title
        self.description = description
        self.target_stage = target_stage
        self.sent_to = []
        self.created_at = datetime.now().strftime("%d/%m/%Y")

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "target_stage": self.target_stage,
            "sent_to": self.sent_to,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        camp = cls(data["title"], data["description"], data["target_stage"])
        camp.sent_to = data.get("sent_to", [])
        camp.created_at = data.get("created_at", datetime.now().strftime("%d/%m/%Y"))
        return camp
