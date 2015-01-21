__author__ = 'admin'

from google.appengine.ext import ndb

class HangoutSubjects(ndb.Model):
    subject = ndb.StringProperty()
    isAvailable = ndb.BooleanProperty(indexed=False)
