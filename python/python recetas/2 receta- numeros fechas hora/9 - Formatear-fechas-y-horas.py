# Formatear fechas

from datetime import datetime

fecha = datetime.now()

print(fecha)

print(fecha.strftime('%A, %d. %B %Y %I:%M:%S'))

#%A Dia ocn nombre completo
#%d Dia en numero
#%B Mes nombre completo
#%Y Año completo
#%I horas
#%M minutos
#%S segundo