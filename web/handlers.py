import jinja2
from apiclient import discovery
from lib.base import BaseHandler


from utils import autolog

API_ROOT = 'https://kx-tutor-hangout-app.appspot.com/_ah/api'
API_NAME = 'tutorhangouts'
VERSION = 'v1'

class MainPage(BaseHandler):
    def get(self):
        subjects = self.get_subjects()
        # template = jinja_env.get_template("views/student.html")

        template_data = {'subjects_query': subjects}
        self.render_template('views/student.html', **template_data)
        # self.response.out.write(template.render({'subjects_query': subjects}))


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