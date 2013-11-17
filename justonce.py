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


class DownloadPage(webapp2.RequestHandler):


  def get(self, app_id):
    one_time_file = OneTimeFile.get_by_id(app_id)
    if one_time_file:
      self.response.out.write(one_time_file.contents)
      one_time_file.key.delete()
    else:
      self.error(404)


class UploadPage(webapp2.RequestHandler):


  def post(self, app_id):
    one_time_file = OneTimeFile.get_by_id(app_id)
    one_time_file.contents = XXX
    one_time_file.put()


# Start up our app
app = webapp2.WSGIApplication([
  ('/download/(.+)', DownloadPage),
  ('/upload/(.+)', UploadPage),
], debug=True)
