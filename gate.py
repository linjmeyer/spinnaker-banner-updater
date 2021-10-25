#   Foremast - Pipeline Tooling
#
#   Copyright 2019 Redbox Automated Retail, LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""Centralized Methods interacting with the Spinnaker Gate API."""
import logging
import requests
import json
import config

LOG = logging.getLogger(__name__)
OAUTH_ENABLED = False


def gate_request(uri=None, method="GET", headers={}, data={}, params={}):
    """Make a request to Gate's API via various auth methods

    Args:
        method (str): Method to request Gate API; GET or POST
        uri (str): URI path to gate API
    """
    response = None
    url = '{host}{uri}'.format(host=config.host, uri=uri)

    method = method.upper()
    if method == 'GET':
        response = requests.get(url, params=params, headers=headers, verify=config.verify, cert=config.cert)
    elif method == 'POST':
        response = requests.post(url, data=data, headers=headers, verify=config.verify, cert=config.cert)
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers, verify=config.verify, cert=config.cert)
    else:
        raise NotImplementedError

    response.raise_for_status()

    LOG.info(response.content)
    return response

def update_banners(app_name, banners):
    task = {
        "job": [
            {
                "type": "updateApplication",
                "application": {
                    "name": app_name,
                    "customBanners": banners
                }
            }
        ],
        "application": app_name,
        "description": "Update Application Banner: " + app_name
    }
    gate_request(uri="/tasks", method="POST", data=json.dumps(task), headers={"content-type": "application/json"})

def update_pipeline(pipeline):
    gate_request(uri="/pipelines", method="POST", data=json.dumps(pipeline), headers={"content-type": "application/json"})

