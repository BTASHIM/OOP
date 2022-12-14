students = []
lecturers = []
class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def finish_course(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course_name, lecturer_grade):
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached and course_name \
                in self.finished_courses and 0 < lecturer_grade <= 10:
            if course_name in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course_name] += [lecturer_grade]
            else:
                lecturer.lecturer_grades[course_name] = [lecturer_grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for a in self.grades.values():
            for b in a:
                grades_list.append(b)
        if len(grades_list) > 0:
            avg = sum(grades_list) / len(grades_list)
            return avg
        else:
            return 'Оценок нет'

    def __str__(self):
        res = f'Студент \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: ' \
              f'{self.average_grade()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные ' \
              f'курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
        else:
            return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}
        self.courses_attached = []
        lecturers.append(self)

    def attach_course(self, course_name):
        if course_name in self.courses_attached:
            pass
        else:
            self.courses_attached.append(course_name)

    def average_grade(self):
        grades_list = []
        for a in self.lecturer_grades.values():
            for b in a:
                grades_list.append(b)
        if len(grades_list) > 0:
            avg = sum(grades_list)/len(grades_list)
            return avg
        else:
            return 'Оценок нет'

    def __str__(self):
        res = f'Лектор \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: ' \
              f'{str(self.average_grade())}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
        else:
            return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course_name, grade):
        if isinstance(student, Student) and course_name in student.finished_courses or student.courses_in_progress:
            if course_name in student.grades:
                student.grades[course_name] += [grade]
            else:
                student.grades[course_name] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


student1 = Student('Иван', 'Иванов', 'Мужской')
student2 = Student('Петр', 'Петров', 'Мужской')
lecturer1 = Lecturer('Сидор', 'Сидоров')
lecturer2 = Lecturer('Емельян', 'Емельянов')
reviewer1 = Reviewer('Михаил', 'Михаилов')
reviewer2 = Reviewer('Виктор', 'Викторов')

student1.add_courses('Математика')
student2.add_courses('Математика')
student1.add_courses('Физика')

student2.finish_course('Физика')
student1.finish_course('Химия')

reviewer1.rate_hw(student1, 'Химия', 10)
reviewer2.rate_hw(student1, 'Физика', 2)
reviewer1.rate_hw(student2, 'Химия', 8)
reviewer2.rate_hw(student2, 'Математика', 9)

lecturer1.attach_course('Химия')
lecturer2.attach_course('Физика')
student1.rate_lecturer(lecturer1, 'Химия', 10)
student2.rate_lecturer(lecturer2, 'Физика', 7)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(lecturer1.__lt__(lecturer2))
print(student1.__lt__(student2))

def average_stud_grade (course):
    stud_grades = []
    course_grades = []
    for k in students:
       if course in k.grades:
          stud_grades.append(k.grades[course])
    for grade in stud_grades:
       course_grades.extend(grade)
    if len(course_grades) > 0:
       avg = sum(course_grades)/len(course_grades)
    else:
        avg = f'Нет оценок по предмету {course}'
    return avg

def average_lecturer_grade (course):
    lect_grades = []
    course_grades = []
    for k in lecturers:
       if course in k.lecturer_grades:
          lect_grades.append(k.lecturer_grades[course])
    for grade in lect_grades:
       course_grades.extend(grade)
    if len(course_grades) > 0:
       avg = sum(course_grades)/len(course_grades)
    else:
        avg = f'Нет оценок по предмету {course}'
    return avg

print(average_stud_grade ('Физика'))
print(average_lecturer_grade('Физика'))