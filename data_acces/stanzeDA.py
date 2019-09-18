from google.appengine.ext import ndb

from models.stanzeModel import Stanza

def getAllStanze():
    stanze = Stanza().query().fetch()
    return stanze