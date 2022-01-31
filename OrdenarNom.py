import llista

def ordenar_per_nom(alumnes):
    def nom (element):
        return element['alumne']
        llista.sort(key=nom)
        return llista

print(ordenar_per_nom(llista.alumnes))
