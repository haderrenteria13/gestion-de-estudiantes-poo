class Estudiantes: 
    # Constructor
    def __init__(self, estudiante, nombre, apellido, id_estudiante):
        # Atributos de instancia
        self.__estudiante = estudiante
        self.__nombre = nombre
        self.__apellido = apellido
        self.__id_estudiante = id_estudiante
    
    def get_estudiante(self):
        return self.__estudiante
        
    def get_nombre(self):
        return self.__nombre
            
    def get_apellido(self):
        return self.__apellido
            
    def get_id_estudiante(self):
        return self.__id_estudiante
    
    # Metodos de instancia
    