# Programmer: Chris Bunch (chris@appscale.com)


from google.appengine.ext import ndb
import webapp2


class OneTimeFile(ndb.Model):
  """A OneTimeFile represents a file that can be downloaded one time.

  Fields:
    name: The user-provided name of the file. This is the key of the item, to
      avoid having to manually index it.
    contents: A binary blob that holds the actual file the user uploaded.
  """
  contents = ndb.BlobProperty()


class MainPage(webapp2.RequestHandler):
  """MainPage defines one route for downloading (GET) and uploading (POST).

  Callers can upload or download to any URL, with no authentication.
  """


  def get(self, name):
    """Downloads the item indexed by the given name, if it exists.

    Note that since the item is deleted after the download is started, if the
    caller fails to download the item, there is no way to download it again.

    Args:
      name: A str that names the item that should be downloaded.

    Returns:
      If the item exists, its contents are printed as the response. Otherwise,
      a 404 is returned to the user.
    """
    one_time_file = OneTimeFile.get_by_id(name)
    if one_time_file:
      self.response.out.write(one_time_file.contents)
      one_time_file.key.delete()
    else:
      self.error(404)


  def post(self, name):
    """Uploads a new item with the specified name.

    This method doesn't do any validation on the name, so if another item is
    stored with the same name, it will be overwritten.

    Args:
      name: A str that names the item that should be uploaded.
      body: The request body, which will be stored for later retrieval.
    """
    one_time_file = OneTimeFile(id = name)
    one_time_file.contents = self.request.body
    one_time_file.put()


# Start up our app
app = webapp2.WSGIApplication([
  ('/(.+)', MainPage),
], debug=True)
