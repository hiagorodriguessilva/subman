from datetime import time
import pytest
from subman import SubjectManager, Subject


def test_add_subject():
    manager = SubjectManager()
    subject = manager.add_subject(
        "Math",
        time(8, 0),
        time(9, 30),
        ["monday", "wednesday"],
        False,
    )

    assert subject.name == "Math"
    assert subject.entrance_time == time(8, 0)
    assert subject.class_ending_time == time(9, 30)
    assert subject.days_of_week == ("monday", "wednesday")
    assert subject.summer_subject is False
    assert len(manager.subjects) == 1


def test_blank_name():
    manager = SubjectManager()
    with pytest.raises(ValueError):
        manager.add_subject(" ", time(8, 0), time(9, 0), ["monday"])


def test_invalid_times():
    manager = SubjectManager()
    with pytest.raises(ValueError):
        manager.add_subject("Math", time(10, 0), time(9, 0), ["monday"])


def test_empty_days():
    manager = SubjectManager()
    with pytest.raises(ValueError):
        manager.add_subject("Math", time(8, 0), time(9, 0), [])


def test_invalid_day():
    manager = SubjectManager()
    with pytest.raises(ValueError):
        manager.add_subject("Math", time(8, 0), time(9, 0), ["funday"])


def test_summer_subject_true():
    manager = SubjectManager()
    subject = manager.add_subject("Summer Math", time(8, 0), time(9, 0), ["tuesday"], True)

    assert subject.summer_subject is True


def test_subject_immutable():
    subject = Subject("Math", time(8, 0), time(9, 0), ("monday",))
    with pytest.raises(Exception):
        subject.name = "New"
