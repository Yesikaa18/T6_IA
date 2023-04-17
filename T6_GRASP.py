import numpy as np
import time
import matplotlib.pyplot as plt
from statsmodels.sandbox.distributions.examples.ex_mvelliptical import fig

inicio = time.time()

# Código a medir
time.sleep(1)

print("Algoritmo de GRASP con implementación de instancias del problema de la mochila")
def greedy(K, pesos, valores, capacidad):
    # Algoritmo goloso para construir una solución inicial
    solucion = []
    valor_total = 0
    peso_total = 0
    while peso_total < capacidad:
        candidatos = [(i, valores[i]/pesos[i]) for i in range(len(pesos)) if i not in solucion]
        candidatos_ordenados = sorted(candidatos, key=lambda x: x[1], reverse=True)
        mejor_candidato = candidatos_ordenados[0][0]
        if peso_total + pesos[mejor_candidato] <= capacidad:
            solucion.append(mejor_candidato)
            valor_total += valores[mejor_candidato]
            peso_total += pesos[mejor_candidato]
        else:
            break
    return solucion, valor_total

def busqueda_local(K, solucion, pesos, valores, capacidad):
    # Búsqueda local para mejorar la solución
    mejor_solucion = list(solucion)
    mejor_valor = sum([valores[i] for i in solucion])
    for i in range(len(solucion)):
        for j in range(i+1, len(solucion)):
            vecino = list(solucion)
            vecino[i], vecino[j] = vecino[j], vecino[i]
            valor_vecino = sum([valores[i] for i in vecino])
            peso_vecino = sum([pesos[i] for i in vecino])
            if peso_vecino <= capacidad and valor_vecino > mejor_valor:
                mejor_solucion = vecino
                mejor_valor = valor_vecino
    return mejor_solucion, mejor_valor

def grasp(K, pesos, valores, capacidad, max_iter):
    # Algoritmo GRASP
    mejor_solucion = None
    mejor_valor = float('-inf')
    for i in range(max_iter):
        solucion, valor = greedy(K, pesos, valores, capacidad)
        solucion, valor = busqueda_local(K, solucion, pesos, valores, capacidad)
        if valor > mejor_valor:
            mejor_solucion = solucion
            mejor_valor = valor
    return mejor_solucion, mejor_valor

# Ejemplo de uso
#pesos = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]     #ejemplo de la instancia f1_l-d_10_269
#valores = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
#capacidad = 269

#pesos = [92, 4, 43, 83, 84, 68, 92, 82, 6, 44, 32, 18, 56, 83, 25, 96, 70, 48, 14, 58]
#valores = [44, 46, 90, 72, 91, 40, 75, 35, 8, 54, 78, 40, 77, 15, 61, 17, 75, 29, 75, 63]
#capacidad = 878

pesos = [485,326,248,421,322,795,43 ,845,955,252,9  ,901,122,94 ,738,574,715,
            882,367,984,299,433,682,72 ,874,138,856,145,995,529,199,277,97 ,719,
            242,107,122,70 ,98 ,600,645,267,972,895,213,748,487,923,29 ,674,540,
            554,467,46 ,710,553,191,724,730,988,90 ,340,549,196,865,678,570,936,
            722,651,123,431,508,585,853,642,992,725,286,812,859,663,88 ,179,187,
            619,261,846,192,261,514,886,530,849,294,799,391,330,298,790]

valores = [94, 506, 416, 992, 649, 237, 457, 815, 446, 422, 791, 359, 667, 598, 7 ,
           544, 334, 766, 994, 893, 633, 131, 428, 700, 617, 874, 720, 419, 794, 196,
           997, 116, 908, 539, 707, 569, 537, 931, 726, 487, 772, 513, 81 , 943, 58 ,
           303, 764, 536, 724, 789, 479, 142, 339, 641, 196, 494, 66 , 824, 208, 711,
           800, 314, 289, 401, 466, 689, 833, 225, 244, 849, 113, 379, 361, 65 , 486,
           686, 286, 889, 24 , 491, 891, 90 , 181, 214, 17 , 472, 418, 419, 356, 682,
           306, 201, 385, 952, 500, 194, 737, 324, 992, 224]

capacidad = 995

max_iter = 100  #Máximo de iteraciones
solucion, valor = grasp(len(pesos), pesos, valores, capacidad, max_iter)
print('Su solución para el algoritmo es: ', solucion)
print('Valor total:', valor)


x = np.linspace(0, capacidad, 100)
y = x * (max(valores) / max(pesos))

plt.scatter(pesos, valores)
plt.plot(x, y, color='grey', label='Solución óptima')
plt.axvline(x=capacidad, color='r', linestyle='--', label='Capacidad máxima')
plt.xlabel('Peso')
plt.ylabel('Valor')
plt.title('Elementos')
plt.legend()
plt.show()

fin = time.time()
print("Tiempo de ejecución del programa: ", fin-inicio)
fig.savefig('grafica.png')

dato = fin-inicio