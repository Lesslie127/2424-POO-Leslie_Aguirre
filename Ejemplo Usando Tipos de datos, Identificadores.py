# Este programa gestiona un registro de estudiantes utilizando listas, diccionarios y cadenas de texto en Python.

def add_student(students, student_id, name, age, course):

    # Se agrega un estudiante al registro.

    student = {
        'id': student_id,
        'name': name,
        'age': age,
        'course': course
    }
    students.append(student)
    print(f"Estudiante {name} agregado al registro.")

def list_students(students):

    #Muestra la lista de estudiantes en el registro.
    if students:
        print("Registro de Estudiantes:")
        for student in students:
            print(f"ID: {student['id']}, Nombre: {student['name']}, Edad: {student['age']}, Curso: {student['course']}")
    else:
        print("No hay estudiantes en el registro.")

def find_student_by_id(students, student_id):

#Busca un estudiante por su número de identificación.
    for student in students:
        if student['id'] == student_id:
            print(f"Estudiante encontrado - Nombre: {student['name']}, Edad: {student['age']}, Curso: {student['course']}")
            return
    print(f"No se encontró ningún estudiante con el ID {student_id}.")

def main():
    # Declaración de variables
    students = []  # Lista de estudiantes

    # Agregar estudiantes al registro
    add_student(students, 101, "Nelly Perez", 20, "Ingeniería")
    add_student(students, 102, "Tammy García", 22, "Medicina")
    add_student(students, 103, "Carlos López", 21, "Economía")

    # Se muestra la lista de estudiantes
    list_students(students)

    # Buscar estudiante por ID
    find_student_by_id(students, 102)

if __name__ == "__main__":
    main()
