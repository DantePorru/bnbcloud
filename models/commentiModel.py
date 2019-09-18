from google.appengine.ext import ndb

class Commento(ndb.Model):
    commento_id = ndb.StringProperty(required=True)
    guest_name = ndb.StringProperty()
    guest_email = ndb.StringProperty(required=True)
    guest_picture = ndb.StringProperty()
    testo =ndb.StringProperty()
    datetime = ndb.TimeProperty(auto_now=True)