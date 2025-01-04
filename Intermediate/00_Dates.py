### Dates ###

from datetime import datetime  # Importamos módulo del Core

now = datetime.now() # Tenemos que instanciar un objeto
# Ahora imprimimos diferentes propiedades del objeto
print(now.year)
print(now.month)
print(now.day)  
print(now.hour)
print(now.minute)
print(now.second)
# Cada vez que imprimimos todo lo anterior, los datos cambian puesto que coge el now del momento

# Timestamp. Representación en float de un tiempo, momento, etc
# Se utiliza para que podamos propagarla sin depender de los sistemas ni lenguajes
# Es un número de segundos desde 00:00:00 del 1 enero de 1970
timestamp = now.timestamp()
print(timestamp)