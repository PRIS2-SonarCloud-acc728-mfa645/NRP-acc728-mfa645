class Requisito:

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.peso = 1
        self.relRequisitos = [] #Implicacion, combinacion y exclusion con requisitos
        self.stakeholders = []
        self.valor = 0 #Iterar los stakeholders y sumar la importancia de cada uno


class Stakeholder:

    def __init__(self, nombre):
        self.nombre = nombre
        self.recomendaciones = []
        self.recomendadoPor = []
        self.importancia = len(self.recomendadoPor)

    def recomendar(self, stakeholder):
        if not self.recomendaciones.__contains__(stakeholder):
            self.recomendaciones.append(stakeholder)
            stakeholder.importancia += 1