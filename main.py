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
import os

import jinja2
import webapp2

from apiclient import discovery
from utils import autolog


# Jinja environment instance necessary to use Jinja views.
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                               autoescape=True)
API_ROOT = 'https://kx-tutor-hangout-app.appspot.com/_ah/api'
API_NAME = 'tutorhangouts'
VERSION = 'v1'


class MainHandler(webapp2.RequestHandler):
    def get(self):
        subjects = self.get_subjects()
        template = jinja_env.get_template("views/index.html")
        self.response.out.write(template.render({'subjects_query': subjects}))

    def get_subjects(self):
        # Build a service object for interacting with the API.
        discovery_url = '%s/discovery/v1/apis/%s/%s/rest' % (API_ROOT, API_NAME, VERSION)
        service = discovery.build(API_NAME, VERSION, discoveryServiceUrl=discovery_url)

        response = service.subjects().list(order='subject').execute()
        if response:
            return response.get('items', [])
        else:
            autolog("no subjects found")
            return [{}]

app = webapp2.WSGIApplication([
                              ('/', MainHandler)
                              ], debug=True)




#   for row in items:
#       print row['subject']
#
#
#
#