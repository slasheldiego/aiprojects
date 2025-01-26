import re

def buscar_dni(texto):
    patron = r'\b\d{8}\b'
    coincidencias = re.findall(patron, texto)
    return coincidencias