estudiantes = []

def registrar_estudiante(nombre):
	estudiantes.append(nombre);
	print("Estudiante Registrado:", nombre);

registrar_estudiante("Juan Perez")
registrar_estudiante("Maria Lopez");
print("Lista estudiantes: ")

for estudiante in estudiantes:
	print(estudiante)
