from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt
import scipy 
import numpy as np

# Configuracion del Diagrama de Ojo
# Ndat: Es el numero de datos a graficar
# Sps: El numero de muestras por simbolo del archivo generado en gnuradio
Ndat=10000 
Sps = 8

# Leemos el archivo producido por gnuradio
y1=scipy.fromfile(open("Senal_Nyq"), dtype=scipy.float32) 
y2=scipy.fromfile(open("Senal_RC"), dtype=scipy.float32) 
y3=scipy.fromfile(open("Senal_Rect"), dtype=scipy.float32) 
y4=scipy.fromfile(open("Senal_RRC"), dtype=scipy.float32) 

#Escogemos una porcion de datos para graficar
y1=(y1[0:Ndat])
y2=(y2[0:Ndat])
y3=(y3[0:Ndat])
y4=(y4[0:Ndat])

#Grafica1
eyediagram(y1, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Filtro: Nyquist")
plt.show()

#Grafica2
eyediagram(y2, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Filtro: Coseno Alzado")
plt.show()

#Grafica3
eyediagram(y3, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Filtro: Rectangular")
plt.show()

#Grafica4
eyediagram(y4, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Filtro: Raiz Coseno Alzado")
plt.show()

