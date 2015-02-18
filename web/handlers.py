import json

import httplib2
from google.appengine import runtime

import config
from lib.base import BaseHandler
from utils import autolog



class MainPage(BaseHandler):
    def get(self):

        subjects = self.get_subjects()
        print subjects
        if subjects:
            template_data = {'subjects_query': subjects}
            self.render_template('views/student.html', **template_data)
        else:
            self.render_template('views/unavailable.html')


    def get_subjects(self):
        """ Retrieve available subjects        """
        try:
            resp, content = httplib2.Http().request(config.ENVIRONMENT_URL)
            if resp.status == 200 and content:
                return json.loads(content)
            else:
                print 'tutor-client: no subjects found'
                autolog("no subjects found")
        except runtime.DeadlineExceededError:
            autolog('Deadline exceed error on url: %s' % config.ENVIRONMENT_URL)
        return [{}]