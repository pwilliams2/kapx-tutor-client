import os

base_path = os.path.dirname(__file__)
LOCAL_HANGOUT_APP_URL = 'https://localhost:8080/subjects'
DEV_HANGOUT_APP_URL = 'https://kx-tutor-hangout-app.appspot.com/subjects'
PROD_HANGOUT_APP_URL = 'https://kx-tutor-hangout-app.appspot.com/subjects'

#TODO: add some code to select the correct env url
ENVIRONMENT_URL = DEV_HANGOUT_APP_URL