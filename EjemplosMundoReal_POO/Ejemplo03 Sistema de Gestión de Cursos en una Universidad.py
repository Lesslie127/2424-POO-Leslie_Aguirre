class Curso:
    def __init__(self, nombre_curso, profesor, creditos):
        #Se inicializa un nuevo objeto Curso con nombre del curso, profesor y créditos.
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.creditos = creditos
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        #El estudiante se inscribe al curso
        self.estudiantes.append(estudiante)
        print(f'{estudiante} ha sido inscrito en el curso {self.nombre_curso}')

    def mostrar_estudiantes(self):
        #Se muestra la lista de los estudiantes inscritos en el curso
        print(f' Estudintes inscritos en {self.nombre_curso}:')
        for estudiante in self.estudiantes:
            print(f'{estudiante}')

# Ejemplo de creación y uso de un objeto Curso
curso1 = Curso('Geometria', 'Dr. Jeong', 6)
curso1.inscribir_estudiante('Jey Hyeong')  # Jey Hyeong ha sido inscrita en el curso Geometria.
curso1.inscribir_estudiante('Daniel Im')  # Daniel Im ha sido inscrito en el curso Geometria.
curso1.mostrar_estudiantes()  # Muestra la lista de estudiantes inscritos.