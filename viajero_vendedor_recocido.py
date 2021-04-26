import numpy as np
import random 

class ViajeroVendedor():
    
    def __init__(self, mat_Dist, initial_City, num_Iter):
        self.mat_Dist = mat_Dist
        self.initial_City = initial_City
        self.num_Iter = num_Iter
        
    def camino_Inicio(self):
      copy_mat_Dist = self.mat_Dist.copy() # matriz a seguir
      ruta_Inicial = [self.initial_City]
      sig_Ciudad = self.initial_City
      while len(ruta_Inicial) < len(self.mat_Dist[0,:]):
        copy_mat_Dist[sig_Ciudad,:] = 0
        r = np.where(copy_mat_Dist[:,sig_Ciudad]>0) #busca ciudades disponibles
        sig_Ciudad = random.choice(r[0])
        ruta_Inicial.append(sig_Ciudad)
      ruta_Inicial.append(self.initial_City)
      return ruta_Inicial
  
    def random_neighbour(self,solution):
      cambio_solution = solution.copy()
      elemento1 = random.randint(1,len(cambio_solution)-2)
      r = list(range(1,elemento1)) + list(range(elemento1+1,len(cambio_solution)-1))
      elemento2 = random.choice(r)
      random_index = [elemento1,elemento2]
      cambio_solution[random_index[0]], cambio_solution[random_index[1]] = cambio_solution[random_index[1]], cambio_solution[random_index[0]]
      return cambio_solution
    
    def recocido_simulado(self):
      solucion = self.camino_Inicio()
      solucion_eval = self.evalua(solucion)
      temperatura = solucion_eval*0.4
      print('Temperatura: ',temperatura)
      while temperatura >= 0.1:
        for _ in range(self.num_Iter):
          candidato = self.random_neighbour(solucion.copy())
          candidato_eval = self.evalua(candidato)
          delta = candidato_eval-solucion_eval
          print(delta)
          print('Solución: ',solucion)
          print('Candidato: ',candidato)
          if delta <= 0 or np.random.uniform(low=0.0, high=1.0, size=None) < np.power(np.e,(-delta/(20*temperatura))):
              solucion, solucion_eval = candidato, candidato_eval
              if delta <= 0:
                  print('Se acepta la nueva solución') 
              else:
                  print('Se acepta la nueva solución sin mejora')
          else:
              print('No se acepta la nueva solución sin mejora')              
        temperatura = temperatura * np.random.uniform(low=0.8, high=0.99, size=None)
        print('Temperatura',temperatura)
      return temperatura
        
    def evalua(self,Ruta):
      suma_Ractual = 0
      for i in range(len(Ruta)-1):
        suma_Ractual += self.mat_Dist[Ruta[i],Ruta[i+1]]
      return suma_Ractual

#h=ViajeroVendedor(np.array([[0,8,4,15],[8,0,7,9],[4,7,0,10],[15,9,10,0]]),0,3)
h=ViajeroVendedor(np.array([[0,54,146,180,27],[54,0,43,110,120],[146,43,0,31,135],[180,110,31,0,86],[27,120,135,86,0]]),0,3)
print(h.recocido_simulado())