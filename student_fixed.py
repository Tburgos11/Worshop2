class Student:
    def __init__(self, student_id: str, name: str):
        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty.")
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor_roll = False

    def add_grade(self, grade: float):
        if not isinstance(grade, (int, float)):
            print("Error: grade must be numeric.")
            return
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Error: grade must be between 0 and 100.")

    def calc_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self) -> str:
        avg = self.calc_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        return "F"

    def evaluate(self):
        avg = self.calc_average()
        self.is_passed = avg >= 60
        self.honor_roll = avg >= 90

    def remove_grade(self, index: int):
        try:
            self.grades.pop(index)
        except IndexError:
            print("Error: index out of range.")

    def report(self):
        self.evaluate()
        print("---- Student Report ----")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.calc_average():.2f}")
        print(f"Letter Grade: {self.letter_grade()}")
        print(f"Passed: {'Yes' if self.is_passed else 'No'}")
        print(f"Honor Roll: {'Yes' if self.honor_roll else 'No'}")


def start_run():
    s = Student("001", "Thomas")
    s.add_grade(95)
    s.add_grade(87)
    s.add_grade(91)
    s.report()


if __name__ == "__main__":
    start_run()
