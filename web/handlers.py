import json

import httplib2
from google.appengine import runtime

import config
from lib.base import BaseHandler
from utils import autolog


API_ROOT = 'https://kx-tutor-hangout-app.appspot.com/_ah/api'
API_NAME = 'tutorhangouts'
VERSION = 'v1'


class MainPage(BaseHandler):
    def get(self):

        subjects = self.get_subjects()
        if subjects:
            template_data = {'subjects_query': subjects}
            self.render_template('views/student.html', **template_data)
        else:
            self.render_template('views/unavailable.html')


    def get_subjects(self):
        """ Retrieve available subjects        """
        try:
            resp, content = httplib2.Http().request(config.ENVIRONMENT_URL)
            if content:
                return json.loads(content)
            else:
                autolog("no subjects found")
        except runtime.DeadlineExceededError:
            autolog('Deadline exceed error on url: %s' % config.ENVIRONMENT_URL)
        return [{}]