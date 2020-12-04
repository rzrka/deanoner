from defines import getCreds, makeApiCall


def getAccountInfo(params):
    """ Get info on a users account

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}
    Returns:
        object: data from the endpoint
    """

    endpointParams = dict()
    endpointParams['fields'] = 'business_discovery.username('+ 'rzrka5555' +'){username,website,name,ig_id,profile_picture_url,media_count,media}'

    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['instagram_account_id']

    return makeApiCall(url, endpointParams)

params = getCreds()
response = getAccountInfo(params)
print(response)