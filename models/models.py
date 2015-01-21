__author__ = 'admin'

from google.appengine.ext import ndb

class HangoutSubjects(ndb.Model):
    subjects = ndb.StringProperty()
    isAvailable = ndb.BooleanProperty(indexed=False)
