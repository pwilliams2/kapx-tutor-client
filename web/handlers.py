import json
import httplib2
from apiclient import discovery

import config
from lib.base import BaseHandler
from utils import autolog, JSONEncoder


API_ROOT = 'https://kx-tutor-hangout-app.appspot.com/_ah/api'
API_NAME = 'tutorhangouts'
VERSION = 'v1'

class MainPage(BaseHandler):
    def get(self):
        template_data = {'subjects_query': self.get_subjects()}
        self.render_template('views/student.html', **template_data)



    def get_subjects(self):
        """ Retrieve available subjects        """
        resp, content = httplib2.Http().request(config.DEV_HANGOUT_APP_URL)

        if content:
            return json.loads(content)
        else:
            autolog("no subjects found")
            return [{}]