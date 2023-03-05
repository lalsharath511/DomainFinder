import whois
from googlesearch import search


def dict_update(data):
    for key in data.keys():
        if "date" in key:
            data.update({key: str(data[key])})
    return data


def getURL(companyName):
    try:
        for url in search(companyName, num_results=1):
            return url
    except:
        return ''


def domain_info_fun(url):
    try:
        domain_info = whois.whois(url)
        return domain_info
    except:
        return
