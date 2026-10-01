from typing import List


def average(marks: List[int]) -> float:
    if not marks:
        raise ValueError("Marks cannot be empty")

    return sum(marks) / len(marks)


def grade(mark: float) -> str:
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


marks = [80, 90, 70]

avg = average(marks)

print("Marks:", marks)
print("Average:", avg)
print("Grade:", grade(avg))
