from datetime import date

class Categoria:
    def __init__(self, definicio):
        self.definicio = definicio

class Autor:
    def __init__(self, nom, data_naixement):
        self.nom = nom
        self.data_naixement = data_naixement

class Editorial:
    def __init__(self, nom, nacionalitat):
        self.nom = nom
        self.nacionalitat = nacionalitat

class Llibre:
    def __init__(self, titol, any, categoria, autor, editorial):
        self.titol = titol
        self.any = any
        self.categoria = categoria
        self.autor = autor
        self.editorial = editorial

class Copia:
    def __init__(self, codi, ubicacio):
        self.codi = codi
        self.ubicacio = ubicacio

class Lector:
    def __init__(self, nom, cognoms, dni, adreca):
        self.nom = nom
        self.cognoms = cognoms
        self.dni = dni
        self.adreca = adreca

class Prestec:
    def __init__(self, data_inici, data_final, llibre, lector):
        self.data_inici = data_inici
        self.data_final = data_final
        self.llibre = llibre
        self.lector = lector

class UsuariMulta:
    def __init__(self, data_inici, data_final, lector):
        self.data_inici = data_inici
        self.data_final = data_final
        self.lector = lector

# Relacions
llibre = Llibre("Titol del llibre", 2022, Categoria("Definicio de categoria"), Autor("Nom de l'autor", date(1990, 1, 1)), Editorial("Nom de l'editorial", "Nacionalitat"))
copia1 = Copia("codi1", "ubicacio1")
copia2 = Copia("codi2", "ubicacio2")
lector = Lector("Nom del lector", "Cognoms del lector", "DNI del lector", "Adreca del lector")
prestec1 = Prestec(date(2024, 3, 18), date(2024, 4, 18), llibre, llector)
prestec2 = Prestec(date(2024, 3, 20), date(2024, 4, 20), llibre, llector)
usuari_multa = UsuariMulta(date(2024, 3, 18), date(2024, 3, 25), llector)
