from typing import List
from enum import Enum

class Requisito:

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.stakeholders:List[Stakeholder] = []
        self.rel_requisitos:List[(Requisito,Relacion)] = []
        self.peso = 1
    
    def relacionar(self, requisito: "Requisito", relacion: "Relacion"):
        if not self.rel_requisitos.__contains__((requisito)):
            self.rel_requisitos.append((requisito,relacion))

    def obtener_valor(self) -> int:
        valor = 0
        for st in self.stakeholders:
            valor += len(st.recomendado_por)
        return valor

class Stakeholder:

    def __init__(self, nombre):
        self.nombre = nombre
        self.recomendaciones:List[Stakeholder] = []
        self.recomendado_por:List[Stakeholder] = []
        self.req_recomendados:List[Requisito] = []

    def recomendar_stakeholder(self, stakeholder: "Stakeholder"):
        if not self.recomendaciones.__contains__(stakeholder):
            self.recomendaciones.append(stakeholder)
            stakeholder.recomendado_por.append(self)

    def recomendar_requisito(self, requisito: "Requisito"):
        if not self.req_recomendados.__contains__(requisito):
            self.req_recomendados.append(requisito)
            requisito.stakeholders.append(self)

class Relacion(Enum):
    IMPLICACION = "Implicacion"
    COMBINACION = "Combinacion"
    EXCLUSION = "Exclusion"

class Mochila:

    def __init__(self, requisitos:List[Requisito]):
        self.requisitos:List[Requisito] = requisitos
        
    def NRPKnapsack(self, W):
        self.requisitos.sort(key=lambda x: (x.obtener_valor/req.peso), reverse=True) 
        finalvalue = 0.0
        num_reqs = 0
    
        for req in self.requisitos:
            if req.peso <= W:
                W -= req.peso
                finalvalue += req.obtener_valor
                num_reqs+=1
                
        return self.requisitos[0:num_reqs]

