import requests
import json

TOKEN = 'EAAE9cVrwZAH8BAC3NYK5BZBkF9NfijOeDSSbUawJRZBVczEiGx0zFpEN7Vi9SQW7ZBUUZAYghl1ZC7X29UQs6zRWskLjL6PiC0BuW7hb0DIZAZBGSchk5ZBUQ9kwK2dTznTNlGVyZAuqzBeMAVPh09etC89vGri8BPuCAAV9GevaemvhZB3CSf9YXYZA4HjLxsiLCT3YwRQLb1yRxZAgSIIbHcDLj9xS6DZAhDeTd4ZC0V6DPshKwZDZD'

def getCreds():
    """ Get creds required for use in the applications

    Returns:
        dictonary: credentials needed globally
    """

    creds = dict()  # dictionary to hold everything
    creds['access_token'] = TOKEN
    creds['client_id'] = '349032043013247'  # client id from facebook app IG Graph API Test
    creds['client_secret'] = '4d033b0901f58883b26519bf771ffefc'  # client secret from facebook app
    creds['graph_domain'] = 'https://graph.facebook.com/'  # base domain for api calls
    creds['graph_version'] = 'v6.0'  # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'  # base endpoint with domain and version
    creds['page_id'] = '105388414686910'
    creds['instagram_account_id'] = '17841403290166303'

    return creds


def makeApiCall(url, endpointParams):
    """ Request data from endpoint with params

    Args:
        url: string of the url endpoint to make request from
        endpointParams: dictionary keyed by the names of the url parameters
    Returns:
        object: data from the endpoint
    """

    data = requests.get(url, endpointParams)# make get request
    response = dict()
    # hold response info
    response['json_data'] = json.loads(data.content)  # response data from the api
    return response['json_data'] # get and return content


if __name__ == '__main__':
    print(getCreds())