from datetime import datetime
from random import randint, choice
from faker.providers import BaseProvider
import faker
import sqlite3

COUNT_STUDENTS = randint(30, 50)
COUNT_GROUPS = 3
COUNT_SUBJECTS = randint(5, 8)
COUNT_TEACHERS = randint(3, 5)
MAX_COUNT_POINTS = 20

class CollegeSubjectProvider(BaseProvider):
    def college_subject(self):
        subjects_list = [ "Mathematics", "English", "Science", "History", "Geography",
            "Physics", "Chemistry", "Biology", "Computer Science", "Art",
            "Music", "Physical Education", "Literature", "Social Studies",
            "Spanish", "French", "German", "Economics", "Psychology",
            "Sociology", "Astronomy", "Philosophy", "Political Science",
            "Environmental Science", "Health Education", "Business Studies",
            "Information Technology", "Drama", "Dance", "Nutrition",
            "Ethics", "Anthropology", "Linguistics", "Graphic Design",
            "Robotics", "Statistics", "Media Studies", "Geology",
            "Home Economics", "Industrial Arts", "Mythology", "Meteorology",
            "Criminology", "Mythology", "Oceanography", "Archaeology",
            "Ethics", "Cultural Studies", "Logic", "Women's Studies"
        ]
        return self.random_element(subjects_list)

def generate_fake_data(count_students: int, count_groups: int, count_subjects: int, count_teachers: int, max_count_points: int):
    fake_students = []
    fake_groups = []
    fake_subjects = []
    fake_teachers = []
    fake_journal = []
    
    fake_data = faker.Faker()
    fake_data.add_provider(CollegeSubjectProvider)

    for _ in range(count_students):
        fake_students.append(fake_data.name())
    
    for _ in range(count_groups):
        fake_groups.append(fake_data.bothify(text='??-##').upper())
        
    for _ in range(count_subjects):
        fake_subjects.append(fake_data.college_subject())
        
    for _ in range(count_teachers):
        fake_teachers.append(fake_data.name())
        
    for _ in range(count_students):
        fake_points = []
        for _ in range(randint(0, max_count_points)):
            fake_points.append(randint(1, 12))
        fake_journal.append(fake_points)
        
    return fake_students, fake_groups, fake_subjects, fake_teachers, fake_journal

if __name__ == "__main__":
    result = generate_fake_data(COUNT_STUDENTS, COUNT_GROUPS, COUNT_SUBJECTS, COUNT_TEACHERS, MAX_COUNT_POINTS)
    print(result)