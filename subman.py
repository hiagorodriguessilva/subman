from dataclasses import dataclass
from datetime import time

VALID_DAYS = {
    "monday", "tuesday", "wednesday", "thursday",
    "friday", "saturday", "sunday",
}


@dataclass(frozen=True)
class Subject:
    name: str
    entrance_time: time
    class_ending_time: time
    days_of_week: tuple[str, ...]
    summer_subject: bool = False

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("name is required")
        if self.class_ending_time <= self.entrance_time:
            raise ValueError("class_ending_time must be after entrance_time")
        if not self.days_of_week:
            raise ValueError("days_of_week is required")

        normalized_days = []
        for day in self.days_of_week:
            normalized_day = day.strip().lower()
            if normalized_day not in VALID_DAYS:
                raise ValueError(f"invalid day: {day}")
            if normalized_day in normalized_days:
                raise ValueError(f"duplicate day: {day}")
            normalized_days.append(normalized_day)

        object.__setattr__(self, "days_of_week", tuple(normalized_days))


class SubjectManager:
    def __init__(self):
        self.subjects = []

    def add_subject(self, name, entrance_time, class_ending_time, days_of_week, summer_subject=False):
        subject = Subject(name, entrance_time, class_ending_time, tuple(days_of_week), summer_subject)
        self.subjects.append(subject)
        return subject
