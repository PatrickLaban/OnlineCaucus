import json

from google.appengine.ext import ndb

from controllers.account.account_base import AccountBaseHandler
from models.Caucus import Caucus


class CaucusInfoHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self, caucus_id):
        caucus = Caucus.get_by_id(int(caucus_id))
        self.template_values['caucus'] = caucus
        self.render_template('account/caucus/caucus_details.html')


class CaucusCreateHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self):
        self.render_template('account/caucus/caucus_new_edit.html')

    @ndb.toplevel
    def post(self):
        name = self.request.get('name')
        if Caucus.query(Caucus.name == name).count() > 0:
            response = {'success': False, 'error_message': "A caucus already exists with the name {0}".format(name)}
            self.response.write(json.dumps(response))
            return
        new_caucus = Caucus.create_caucus(name=name, user_account=self.user_account)
        response = {'success': True, 'goto_url': '/account/caucus/{0}'.format(new_caucus.key.id())}
        self.response.write(json.dumps(response))


class CaucusEditHandler(AccountBaseHandler):
    @ndb.toplevel
    def get(self, caucus_id):
        caucus = Caucus.get_by_id(int(caucus_id))
        self.template_values['caucus'] = caucus
        self.render_template('account/caucus/caucus_new_edit.html')

    @ndb.toplevel
    def put(self, caucus_id):
        caucus = Caucus.get_by_id(int(caucus_id))
        name = self.request.get('name')
        if Caucus.query(Caucus.name == name).count() > 0:
            response = {'success': False, 'error_message': "A caucus already exists with the name {0}".format(name)}
            self.response.write(json.dumps(response))
            return
        caucus.edit_caucus(name=name)
        response = {'success': True, 'goto_url': '/account/caucus/{0}'.format(caucus.key.id())}
        self.response.write(json.dumps(response))


class CaucusJoinHandler(AccountBaseHandler):
    @ndb.toplevel
    def post(self, caucus_id):
        caucus = Caucus.get_by_id(int(caucus_id))
        caucus.add_participant(self.user_account)
        response = {'success': True}
        self.response.write(json.dumps(response))
