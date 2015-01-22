#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import os
import pprint
from apiclient import discovery

from google.appengine.ext import ndb
import jinja2

import webapp2
from models.models import HangoutSubjects

# Jinja environment instance necessary to use Jinja views.
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                               autoescape=True)

PARENT_KEY = ndb.Key("Entity", 'hangoutsubjects_root')

def load(self):
        logging.info("loading...")
        HangoutSubjects(parent=PARENT_KEY,
                        subject="Business",
                        isAvailable=False).put()

        HangoutSubjects(parent=PARENT_KEY,
                        subject="Technology",
                        isAvailable=False).put()

        HangoutSubjects(parent=PARENT_KEY,
                        subject="General Math",
                        isAvailable=False).put()

        HangoutSubjects(parent=PARENT_KEY,
                        subject="Calculus",
                        isAvailable=False).put()
        HangoutSubjects(parent=PARENT_KEY,
                        subject="Science",
                        isAvailable=False).put()

        HangoutSubjects(parent=PARENT_KEY,
                        subject="Writing",
                        isAvailable=True).put()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        subjects = HangoutSubjects.query().order(HangoutSubjects.subject).fetch()

        if not subjects:
            logging.info("no subjects")
            load(self)
            subjects = HangoutSubjects.query().order(HangoutSubjects.subject).fetch()

        template = jinja_env.get_template("views/index.html")
        self.response.out.write(template.render({'subjects_query' : subjects}))
        main()

class DataHandler(webapp2.RequestHandler):
    def get(self):
        subjects_query = HangoutSubjects.query(ancestor=PARENT_KEY)

        self.redirect(self.request.referer)




app = webapp2.WSGIApplication([
                                  ('/', MainHandler),
                                  ('/data', DataHandler)
                              ], debug=True)

def main():
    # Build a service object for interacting with the API.
    api_root = 'https://kx-tutor-hangout-app.appspot.com/_ah/api'
    api = 'tutorhangouts'
    version = 'v1'
    discovery_url = '%s/discovery/v1/apis/%s/%s/rest' % (api_root, api, version)
    service = discovery.build(api, version, discoveryServiceUrl=discovery_url)

    # Fetch all subjects and print them out.
    response = service.subjects().list().execute()
    subjects = response.get('items', [])
    for row in subjects:
        print row['subject']

    # TODO: convert dict to json to be sent to jinja
    pprint.pprint(response)


if __name__ == '__main__':
  main()