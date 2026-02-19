class StudentService:

    def printList(self) -> None:
        """Affiche la liste des étudiants"""
        pass

    def addStudent(self, student: 'Student') -> None:
        """Ajoute un étudiant à la liste"""
        pass

    def removeStudent(self, student_id: int) -> None:
        """Supprime un étudiant par son id"""
        pass

class StudentService:
    
    def __init__(self):
        self.students = {}

    def printList(self):
        if not self.students:
            print("No students.")
        for id, name in self.students.items():
            print(f"{id}: {name}")

    def addStudent(self, student_id, name):
        self.students[student_id] = name
        print(f"Student '{name}' added.")

    def removeStudent(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with id '{student_id}' removed.")
        else:
            print("Student not found.")
