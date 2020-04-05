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
    
    def __init__(self, api_key):
        self.api_key = api_key

    def get_all_projects(self, offset=0, limit=2, include_options=0):
        params = {
            'api_key': self.api_key,
            'offset': offset,
            'limit': limit,
            'include_options': include_options
        }
        r = requests.get('https://www.parsehub.com/api/v2/projects', params=params)
        return r
