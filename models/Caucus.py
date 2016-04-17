from google.appengine.ext import ndb

from ModelBase import ModelBase
#from UserAccount import UserAccount


class Caucus(ModelBase):
    name = ndb.StringProperty(required=True)
    participants = ndb.KeyProperty(kind='UserAccount', repeated=True)
    created_by = ndb.KeyProperty(kind='UserAccount', required=True)


    @classmethod
    def create_caucus(cls, name, user_account):
        new_caucus = cls(name=name, created_by=user_account.key)
        new_caucus.put()
        return new_caucus

    def add_participant(self, user_account):
        self.participants.append = user_account.key
        self.put()
