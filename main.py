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

from google.appengine.ext import ndb
import jinja2

import webapp2
from models.models import HangoutSubjects

# Jinja environment instance necessary to use Jinja templates.
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
        subjects_query = HangoutSubjects.query().order(HangoutSubjects.subject).fetch()

        if not subjects_query:
            logging.info("no subjects")
            load(self)
            subjects_query = HangoutSubjects.query().order(HangoutSubjects.subject).fetch()

        template = jinja_env.get_template("templates/index.html")
        self.response.out.write(template.render({'subjects_query' : subjects_query}))


class DataHandler(webapp2.RequestHandler):
    def get(self):
        subjects_query = HangoutSubjects.query(ancestor=PARENT_KEY)

        self.redirect(self.request.referer)




app = webapp2.WSGIApplication([
                                  ('/', MainHandler),
                                  ('/data', DataHandler)
                              ], debug=True)
