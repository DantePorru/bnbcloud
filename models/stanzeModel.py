from google.appengine.ext import ndb

class Stanza(ndb.model):
    stanza_id = ndb.StringProperty(required=True)
    nome_stanza = ndb.StringProperty(required=True)
    numero = ndb.IntegerProperty()
    piano = ndb.StringProperty()
    tipologia = ndb.StringProperty()
    prezzo = ndb.FloatProperty()
    immagine = ndb.BlobKeyProperty()
    immagine mimetype = ndb.StringProperty()