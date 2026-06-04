class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        if all_grades:
            average = sum(all_grades)/len(all_grades)
            return average
        return 0

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average() == other.average()
        return 'Введите двух студентов'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average() < other.average()
        return 'Введите двух студентов'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average() > other.average()
        return 'Введите двух студентов'

    def __str__(self):
       return (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.average()}\n'
               f'Курсы в процессе изучения: {self.courses_in_progress}\n'
               f'Завершенные курсы: {self.finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        if all_grades:
            average = sum(all_grades)/len(all_grades)
            return average
        return 0

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average()}')

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average() == other.average()
        return 'Введите двух лекторов'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average() < other.average()
        return 'Введите двух лекторов'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average() > other.average()
        return 'Введите двух лекторов'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        self.courses_attached += [course]
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Семен', 'Семенев')
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Игорь', 'Игорев')
student_1 = Student('Ольга', 'Алёхина', 'Ж')
student_2 = Student('Кирилл', 'Кириллов', 'М')

student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Python', 'Физкультура']
student_1.finished_courses += ['OOP', 'AI']
student_2.finished_courses += ['OOP', 'Python']
student_1.add_courses('Программирование')
student_2.add_courses('SQL')

lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Python', 'Java']
reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Python', 2)

student_1.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_1, 'Java', 8)
student_1.rate_lecture(lecturer_1, 'С++', 8)
student_1.rate_lecture(lecturer_1, 'Python', 5)
student_2.rate_lecture(lecturer_1, 'Python', 5)
student_1.rate_lecture(lecturer_2, 'Python', 5)
student_1.rate_lecture(lecturer_2, 'Java', 4)
student_1.rate_lecture(lecturer_2, 'С++', 3)
student_1.rate_lecture(lecturer_2, 'Python', 3)
student_2.rate_lecture(lecturer_2, 'Python', 3)

print(student_2.average())
print(student_1.average())
print(student_1==student_2)
print(student_1>student_2)
print(student_1<student_2)
print(student_1>lecturer_2)
print(lecturer_1==lecturer_2)
print(lecturer_1>lecturer_2)
print(lecturer_1<lecturer_2)
print(lecturer_1>student_1)
print(student_1.average())
print(student_2.average())
print('='*30)
print(student_1)
print('='*30)
print(student_2)
print('='*30)
print(reviewer_1)
print('='*30)
print(reviewer_2)

def average_student_grade(students, course_name):
    all_grades = []
    for student in students:
        if course_name in student.grades:
            all_grades += student.grades[course_name]
    if all_grades:
        return sum(all_grades)/len(all_grades)
    else:
        return 0

def average_lecture_grade(lecturers, course_name):
    all_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            all_grades += lecturer.grades[course_name]
    if all_grades:
        return sum(all_grades)/len(all_grades)
    else:
        return 0

print(average_student_grade([student_1, student_2], 'Python'))
print(average_lecture_grade([lecturer_1, lecturer_2], 'Python'))

