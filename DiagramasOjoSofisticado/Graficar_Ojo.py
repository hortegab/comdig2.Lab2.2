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
f_rc_rc=scipy.fromfile(open("Senal_RC_RC"), dtype=scipy.float32) 
f_rrc_rrc=scipy.fromfile(open("Senal_RRC_RRC"), dtype=scipy.float32) 


#Escogemos una porcion de datos para graficar
fp_rc_rc=(f_rc_rc[0:Ndat])
fp_rrc_rrc=(f_rrc_rrc[0:Ndat])

#Grafica para RC*RC
#plt.subplot(221)
p1=eyediagram(fp_rc_rc, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
#eyediagram(fp_rc_rc, 2*Sps, offset=16)
plt.title("Caso: RC*RC")
plt.show(p1)

#Grafica para RRC*RRC
#plt.subplot(222)
#eyediagram(fp_rrc_rrc, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
#plt.title("Caso: RRC*RRC")
#plt.show()

#Grafica para RC*RC
#plt.subplot(223)
#eyediagram(fp_rc_rc, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
#eyediagram(fp_rc_rc, 2*Sps, offset=16)
#plt.title("Caso: RC*RC")
#plt.show()

#Grafica para RRC*RRC
#plt.subplot(224)
#eyediagram(fp_rrc_rrc, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
#plt.title("Caso: RRC*RRC")
#plt.show()

