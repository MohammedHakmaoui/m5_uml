class Client:
    def __init__(self, nom: str, adreca: str, telefon: str, email: str):
        # Inicialitzem els atributs de la classe Client
        self.nom = nom  # Nom del client
        self.adreca = adreca  # Adreça del client
        self.telefon = telefon  # Número de telèfon del client
        self.email = email  # Correu electrònic del client

class UsuariWeb:
    def __init__(self, login: str, password: str, estat: str):
        # Inicialitzem els atributs de la classe UsuariWeb
        self.login = login  # Nom d'usuari per iniciar sessió
        self.password = password  # Contrasenya per iniciar sessió
        self.estat = estat  # Estat de l'usuari (per exemple: actiu, inactiu)

class CarroCompra:
    def __init__(self, client: Client, factura: 'Factura'):
        # Inicialitzem els atributs de la classe CarroCompra
        self.client = client  # Client que realitza la compra
        self.factura = factura  # Factura associada al carro de compra
        self.linies_comanda = []  # Llista de línies de comanda d'aquest carro de compra

class Producte:
    def __init__(self, codi_identificatiu: str, nom: str, proveidor: str):
        # Inicialitzem els atributs de la classe Producte
        self.codi_identificatiu = codi_identificatiu  # Codi identificatiu del producte
        self.nom = nom  # Nom del producte
        self.proveidor = proveidor  # Proveïdor del producte

class Factura:
    def __init__(self, codi_factura: str, adreca_facturacio: str, data_emissio: str, data_tancament: str, pagament: str):
        # Inicialitzem els atributs de la classe Factura
        self.codi_factura = codi_factura  # Codi de la factura
        self.adreca_facturacio = adreca_facturacio  # Adreça de facturació
        self.data_emissio = data_emissio  # Data d'emissió de la factura
        self.data_tancament = data_tancament  # Data de tancament de la factura
        self.pagament = pagament  # Mètode de pagament de la factura

class LiniaComanda:
    def __init__(self, producte: Producte, quantitat: int, preu: float):
        # Inicialitzem els atributs de la classe LiniaComanda
        self.producte = producte  # Producte associat a la línia de comanda
        self.quantitat = quantitat  # Quantitat del producte
        self.preu = preu  # Preu unitari del producte

class OrdreEnviament:
    def __init__(self, codi_identificatiu: str, data_comanda: str, data_enviament: str, destinacio: str, import_: float, estat: str):
        # Inicialitzem els atributs de la classe OrdreEnviament
        self.codi_identificatiu = codi_identificatiu  # Codi identificatiu de l'ordre d'enviament
        self.data_comanda = data_comanda  # Data de la comanda
        self.data_enviament = data_enviament  # Data d'enviament
        self.destinacio = destinacio  # Destinació de l'enviament
        self.import_ = import_  # Import de l'enviament
        self.estat = estat  # Estat de l'ordre d'enviament (per exemple: pendent, enviat)


