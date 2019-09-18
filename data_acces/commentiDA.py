from models.commentiModel import Commento

def getAllCommenti():
    Commenti = Commento().query().fetch()
    return Commenti