import webapp2

import controllers.account.account_index
import controllers.account.company
import controllers.account.location
import controllers.account.caucus

app = webapp2.WSGIApplication(
    [('/account/caucus_create/?', controllers.account.caucus.CaucusCreateHandler),
     ('/account/caucus_edit/(\d+)', controllers.account.caucus.CaucusEditHandler),
     ('/account/caucus/(\d+)', controllers.account.caucus.CaucusInfoHandler),
     ('/account/company_create/?', controllers.account.company.CompanyCreateHandler),
     ('/account/company_edit/(\d+)', controllers.account.company.CompanyEditHandler),
     ('/account/company/(\d+)', controllers.account.company.CompanyInfoHandler),
     ('/account/location_create/?', controllers.account.location.LocationCreateHandler),
     ('/account/?', controllers.account.account_index.IndexBaseHandler),
     ], debug=True)
