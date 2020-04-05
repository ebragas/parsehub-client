import requests

# What's this client going to be able to do?
# Get projects
# Get runs
# Get data from run

# classes:
# Client
# Project
# Run


class ParseHubClient(object):
    
    def __init__(self, api_key=None):
        self.api_key = api_key

    def authenticate(self, api_key):
        self.api_key = api_key

    def get_project(self, project_token, offset=0, include_options=0):
        
        project_endpoint = f'https://www.parsehub.com/api/v2/projects/{project_token}'
        
        params = {
            "api_key": self.api_key,
            "offset": offset,
            "include_options": include_options
        }
        response = requests.get(project_endpoint, params=params)
        project = ParseHubProject(**response.json())
        return project 

    def get_all_projects(self, offset=0, limit=2, include_options=0):
        params = {
            'api_key': self.api_key,
            'offset': offset,
            'limit': limit,
            'include_options': include_options
        }
        r = requests.get('https://www.parsehub.com/api/v2/projects', params=params)
        return r


class ParseHubProject(object):
    '''A single ParseHub Project'''
    def __init__(self, *initial_data, **kwargs):

        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    self.last_ready_run = ParseHubRun(**self.last_ready_run)


class ParseHubRun(object):
    '''A signle ParseHub Run'''
    def __init__(self, *initial_data, **kwargs):
        
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
