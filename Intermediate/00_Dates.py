### Dates ###

from datetime import datetime  # Importamos módulo del Core

now = datetime.now() # Tenemos que instanciar un objeto
# Ahora imprimimos diferentes propiedades del objeto

def print_date(date):
    print("Year", date.year)
    print("Month", date.month)
    print("Day", date.day)  
    print("Hour", date.hour)
    print("Minutes", date.minute)
    print("seconds", date.second)
    print("timestamp", date.timestamp())

print("Los datos de ahora son:")
print_date(now) # Utilizamos la funcion para imprimir datos

# Cada vez que imprimimos todo lo anterior, los datos cambian puesto que coge el now del momento

# Timestamp. Representación en float de un tiempo, momento, etc
# Se utiliza para que podamos propagarla sin depender de los sistemas ni lenguajes
# Es un número de segundos desde 00:00:00 del 1 enero de 1970
#timestamp = now.timestamp()
#print(timestamp)

# Forma de crear una fecha concreta
year_2023 = datetime(2023, 1, 1, 0, 3, 58) # Como mínimo es obligatorio los 3 primeros datos
print("##################")
print("La fecha que he creado es:")
print_date(year_2023)


############  TIME ###########
from datetime import time
current_time = time()
print(current_time.hour)
print(current_time.min)
print(current_time.second)