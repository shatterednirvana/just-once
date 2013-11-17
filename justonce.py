# Programmer: Chris Bunch (chris@appscale.com)


# General purpose library imports
import jinja2
import os
import re
import urllib
import webapp2


# Google App Engine Datastore-related imports
from google.appengine.ext import ndb


# Set up Jinja to read template files for our app
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class OneTimeFile(ndb.Model):
  """A OneTimeFile represents a file that can be downloaded one time.

  Fields:
    name: The user-provided name of the file. This is the key of the item, to
      avoid having to manually index it.
    contents: A binary blob that holds the actual file the user uploaded.
  """
  contents = ndb.BlobProperty()


class MainPage(webapp2.RequestHandler):


  def get(self, name):
    one_time_file = OneTimeFile.get_by_id(name)
    if one_time_file:
      self.response.out.write(one_time_file.contents)
      one_time_file.key.delete()
    else:
      self.error(404)


  def post(self, name):
    one_time_file = OneTimeFile(id = name)
    one_time_file.contents = self.request.body
    one_time_file.put()


# Start up our app
app = webapp2.WSGIApplication([
  ('/(.+)', MainPage),
], debug=True)
