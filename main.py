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
        
    def __str__(self) -> str:
        return self.descripcion

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
            
    def __str__(self) -> str:
        return self.nombre
class Relacion(Enum):
    IMPLICACION = "Implicacion"
    COMBINACION = "Combinacion"
    EXCLUSION = "Exclusion"

class Mochila:

    def __init__(self, requisitos:List[Requisito]):
        self.requisitos:List[Requisito] = requisitos
        
    def nrp_knapsack(self, weight):
        self.requisitos.sort(key=lambda x: (x.obtener_valor()/x.peso), reverse=True) 
        num_reqs = 0
    
        for req in self.requisitos:
            if req.peso <= weight:
                weight -= req.peso
                num_reqs+=1
                
        return self.requisitos[0:num_reqs]
    



#Stakeholder creation
st1 = Stakeholder("St1")
st2 = Stakeholder("St2")
st3 = Stakeholder("St3")
st4 = Stakeholder("St4")

#Stakeholder recomendations
st2.recomendar_stakeholder(st1)

st1.recomendar_stakeholder(st2)

st1.recomendar_stakeholder(st3)

st1.recomendar_stakeholder(st4)
st2.recomendar_stakeholder(st4)
st3.recomendar_stakeholder(st4)

#Requisitos creation
req1 = Requisito("Requisito numero 1")
req2 = Requisito("Requisito numero 2")
req3 = Requisito("Requisito numero 3")
req4 = Requisito("Requisito numero 4")
req5 = Requisito("Requisito numero 5")

#Requisitos recomendation by Stakeholders
st1.recomendar_requisito(req2)

st1.recomendar_requisito(req5)
st2.recomendar_requisito(req5)

st1.recomendar_requisito(req4)
st2.recomendar_requisito(req4)
st3.recomendar_requisito(req4)

st1.recomendar_requisito(req3)
st2.recomendar_requisito(req3)
st3.recomendar_requisito(req3)
st4.recomendar_requisito(req3)


#Requisitos relations
req1.relacionar(req2, "Combinacion")
req2.relacionar(req1, "Combinacion")
req2.relacionar(req3, "Implicacion")
req4.relacionar(req5, "Exclusion")
req5.relacionar(req4, "Exclusion")

#List creation and req addition
requisitos: List[Requisito] = []
requisitos.append(req1)
requisitos.append(req2)
requisitos.append(req3)
requisitos.append(req4)
requisitos.append(req5)

#Mochila creation and print knapsack method
mochila = Mochila(requisitos)
print("Mochila resultado : ")
print(*mochila.nrp_knapsack(3))
