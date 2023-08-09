


"""
Para la siguiente problemática presentada, use programacioón orientada a objedos 
y herencias, uSando como clase principal (  quiniela).
"""
import random
import datetime


# CLASE PRINCIPAL,
class Quiniela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.apuestas = []
        self.recaudacion_total = 0

        #Cada apuesta se irán incrementando de 500.
    def apostar(self, dni, cifra):
        fecha_hora = datetime.datetime.now()
        comprobante = random.randint(1000, 9999)
        self.apuestas.append((dni, cifra))
        self.recaudacion_total += 500

        # CABECERA DEL TICKET IMPRESO DE LA JUGADA
        print("🟢🟢------------------------------------------------🟢🟢")
        print("Agencia💲💲===========💸|🔝LA SUERTE🔝|💸==========💲💲")
        print("🟩🟩_______________________________________________🟩🟩\n ")

        print("-----------------TICKET DE SU JUGADA---------------------- \n")
        print("USTED JUGO!:                    ---------------|", self.nombre)
        print("FECHA Y HORA:                   ---------------|", fecha_hora)
        print("COMPROBANTE N°:                 ---------------|", comprobante)
        print("SU DNI ES:                      ---------------|", dni)
        print("SUS NUMEROS APOSTADOS ES:   -------------------|", cifra)

        #FUNCIÓN QUE CALCULA LA RECAUDACIÓN DIARIA
    def calcular_recaudacion_diaria(self):
        retencion = self.recaudacion_total * 0.47
        ganancia_neta = self.recaudacion_total - retencion
        print("Su recaudación es: ", self.recaudacion_total)
        print("La retención fue de: ", retencion)
        print("Su ganancia neta fue: ", ganancia_neta)
        #FUNCION QUE CALCULA EL TOTAL DE RECAUDACION DE LAS JUGADAS
    def total_recaudacion(self, quini6):
        recaudacion_total = self.recaudacion_total + quini6.recaudacion_total
        retencion = recaudacion_total * 0.47
        ganancia_neta = recaudacion_total - retencion
        print("Recaudación diaria total es:", recaudacion_total)
        print("La retención fue de:", retencion)
        print("La ganancia neta fue de:", ganancia_neta)


        #CLASE HEREDADA DE LA SUPER CLASE MADRE (QUINIELA)
class Quini6(Quiniela):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def apostar(self, dni, cifras):
        self.apuestas.append((dni, cifras))
        self.recaudacion_total += 500

    def comprobar_ganador(self, numeros_ganadores):
        for _, cifras in self.apuestas:
            if cifras == numeros_ganadores:
                print("¡Felicidades! Ha ganado en el Quini 6.")
                return True
        print("No ha ganado en el Quini 6.")
        return False
    
    #FUNCIÓN QUE CALCULA LA RECAUDACION TOTAL DEL DIA, RETENCIONES Y GANANCIAS NETAS
def calcular_recaudacion_total(quiniela, quini6):
    recaudacion_total = quiniela.recaudacion_total + quini6.recaudacion_total
    retencion = recaudacion_total * 0.47
    ganancia_neta = recaudacion_total - retencion
    return recaudacion_total, retencion, ganancia_neta

    #MENÚ PRINCIPAL
if __name__ == "__main__":
    quiniela = Quiniela("Quiniela")
    quini6 = Quini6("Quini 6 tradicional")

    while True:
        print("------------------BIENVENIDO | ELIJA LA OPCIÓN QUE DESEAS REALIZAR--------------\n")
        print("1- Apostar en Quiniela")
        print("2- Apostar en Quini 6 tradicional")
        print("3- Comprobar si ha ganado en Quini 6")
        print("4- Arqueo de caja")
        print("5- Salir del sistema\n")

        #PARA LAS OPCIONES QUE ELIJA EL USUARIO, ELEGI UN IF ANIDADO PROPIO DE PYTHON, QUE ES EL (ELIF)
        opcion = int(input("Dijite su opción: \n"))

        if opcion == 1:
            print("Usted eligio jugar quiniela: \n")
            dni = input("-> Ingrese su DNI: ")
            cifra = input("-> Ingrese el número de 2, 3 o 4 cifras a apostar:\n ")               
            quiniela.apostar(dni, cifra)
            

        elif opcion == 2:
            print("Usted eligio jugar quini6: \n")
            dni = input("-> Ingrese su DNI: \n")
            cifras = input("-> Ingrese seis números entre 00 y 45: \n")
            cifras = [int(num) for num in cifras.split()]
            quini6.apostar(dni, cifras)
            
        elif opcion == 3:
            numeros_ganadores = input("-> Ingrese los números ganadores del Quini 6: \n")
                
            print("...............................................................")
            numeros_ganadores = [int(num) for num in numeros_ganadores.split()]
            quini6.comprobar_ganador(numeros_ganadores)

            #ESTA OPCIÓN MUESTRA POR PANTALLA LA SUMA TOTAL DE LO RECAUDADO, RETENCIONES Y EL NETO DE GANANCIAS
        elif opcion == 4:
            print("Recaudación diaria en apuestas: \n")
            recaudacion_total, retencion, ganancia_neta = calcular_recaudacion_total(quiniela, quini6)
            print("Recaudación diaria total es:", recaudacion_total)
            print("La retención fue de:", retencion)
            print("La ganancia neta fue de:", ganancia_neta)
                 
        elif opcion == 5:
            print("Nos da pena que se valla..Vuelva pronto😞 \n")
            break
        else:
            print("La opción alegida no existe. Elija otro número!.")
