import webapp2
import jinja2
import os
import json

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        api_key = "AIzaSyC_VbSfueAdlwCkD2Mnr-cXzuCeN59FKA8"
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render())

class AboutMePage(webapp2.RequestHandler):
    def get(self):
        aboutme_template = the_jinja_env.get_template('templates/aboutme.html')
        self.response.write(aboutme_template.render())

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/aboutme',AboutMePage),
], debug=True)
