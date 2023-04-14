class Requisito:

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.peso = 1
        self.stakeholders = []
        #Iterar los stakeholders y sumar la importancia de cada uno
        self.valor = 0
        #Implicacion, combinacion y exclusion con requisitos (self será un requisito)
        self.rel_requisitos = [(self, "Implicacion"), (self, "Exclusion"), (self, "Combinacion")] 

class Stakeholder:

    def __init__(self, nombre):
        self.nombre = nombre
        self.recomendaciones = []
        self.recomendado_por = []
        self.importancia = len(self.recomendado_por)

    def recomendar(self, stakeholder):
        if not self.recomendaciones.__contains__(stakeholder):
            self.recomendaciones.append(stakeholder)
            stakeholder.importancia += 1