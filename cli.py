from datetime import time
from subman import SubjectManager

manager = SubjectManager()


def read_time(value):
    hour, minute = map(int, value.split(":"))
    return time(hour, minute)


def add_subject():
    name = input("name: ")
    entrance_time = read_time(input("entrance HH:MM: "))
    ending_time = read_time(input("ending HH:MM: "))
    days = [day.strip() for day in input("days comma-separated: ").split(",") if day.strip()]
    summer_subject = input("summer (y/n): ").strip().lower() == "y"

    try:
        subject = manager.add_subject(name, entrance_time, ending_time, days, summer_subject)
        print("added:", subject)
    except Exception as error:
        print("error:", error)


def list_subjects():
    for subject in manager.subjects:
        print(subject)


def main():
    while True:
        command = input("add/list/exit: ").strip().lower()

        if command == "add":
            add_subject()
        elif command == "list":
            list_subjects()
        elif command == "exit":
            break
        else:
            print("unknown command")


if __name__ == "__main__":
    main()
