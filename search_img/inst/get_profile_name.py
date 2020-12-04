import instaloader

def get_profile_name(ID):
    res = dict()
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_id(L.context, ID)
    res['name'] = profile.username
    return res

if __name__ == '__main__':
    print(get_profile_name(3170429672))