# Exercise: Student Marks Calculator

## Objective

To create a Python program that calculates the average marks of a student and assigns a grade based on the average. The program is also tested using pytest.

## Files

* `calculator.py` – Contains the `average()` and `grade()` functions.
* `test_calculator.py` – Contains test cases for the functions.
* `README.md` – Contains the project description and instructions.

## Functions

### average()

The `average()` function calculates the average of the given marks.

It raises a `ValueError` if the marks list is empty.

### grade()

The `grade()` function assigns a grade based on the average mark:

* 90 and above → A
* 75 to 89 → B
* 60 to 74 → C
* 50 to 59 → D
* Below 50 → F

## Testing

The project uses `pytest` for testing.

The following cases are tested:

* Average of `[80, 90, 70]` is `80`.
* Grade for `80` is `B`.
* Empty marks list raises a `ValueError`.

## Installation

Install pytest using:

```bash
pip install pytest
```

## Run the Program

Run:

```bash
python calculator.py
```

Expected output:

```text
Marks: [80, 90, 70]
Average: 80.0
Grade: B
```

## Run Tests

Run:

```bash
pytest
```

All test cases should pass successfully.

## Conclusion

The student marks calculator was successfully implemented using Python. The program calculates the average, assigns the appropriate grade, handles empty input, and verifies the functions using pytest.
