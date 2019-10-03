#EDGAR ALDAIR RANGEL GARCIA         MATRICULA: 1741207      SALON 835
#FECHA DE CREACIOM: 22/09/2019

def ObtenerTiempo (Distancia, Velocidad):
    TiempoEstimado = Distancia / Velocidad
    return TiempoEstimado

DistanciaEstimada = int(input("Favor de ingresar la distancia \n"))
VelocidadEstimada = int(input("Favor de ingresar la velocidad \n"))
TiempoEstimado = ObtenerTiempo (DistanciaEstimada, VelocidadEstimada)

print("El tiempo estimado es de: {}"  .format(TiempoEstimado))