'''
Created on Sep 5, 2014

@author: gerard
'''

import urllib

def website_is_ok (url):
    """
    Return TRUE if the HTTP GET operation to the website URL returs the OK code 200. FALSE otherwise.
    """
    code = urllib.urlopen(url).getcode()
    if code == 200:
        return 1
    else:
        return 0