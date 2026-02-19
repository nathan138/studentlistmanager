from dataclasses import dataclass

@dataclass
class Student:
    id: int
    nom: str

students = []

def printList():
    for s in students:
        print(f"{s.id} - {s.nom}")

def addStudent(id, nom):
    students.append(Student(id, nom))
    print(f"Student {nom} ajouté.")

def removeStudent(id):
    global students
    students = [s for s in students if s.id != id]
    print(f"Student avec id {id} supprimé.")

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python Main.py [list|add|remove] args...")
        return

    cmd = sys.argv[1]

    if cmd == "list":
        printList()
    elif cmd == "add" and len(sys.argv) == 4:
        addStudent(int(sys.argv[2]), sys.argv[3])
    elif cmd == "remove" and len(sys.argv) == 3:
        removeStudent(int(sys.argv[2]))
    elif cmd == "export" and len(sys.argv) == 4:
        if sys.argv[2] == "json":
            exportJSON(sys.argv[3])
        else:
            print("Format d'export invalide.")
    else:
        print("Commande invalide ou arguments manquants.")

if __name__ == "__main__":
    main()

import json
def exportJSON(file_path):
    data = [{"id": s.id, "nom": s.nom} for s in students]

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print("Export JSON terminé.")
