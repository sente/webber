# -*- coding: utf-8 -*-

import sys
import lxml.html
import requests
from operator import itemgetter



def get_anchors(root):
    res = []
    for a in root.xpath('//a'):
        href = a.get('href')
        if href:
            res.append((a.sourceline, href))
    return res

def get_images(root):
    res = []
    for a in root.xpath('//img'):
        src = a.get('src')
        if src:
            res.append((a.sourceline, src))
    return res

def get_scripts(root):
    res = []
    for a in root.xpath('//script'):
        src = a.get('src')
        if src:
            res.append((a.sourceline, src))
    return res

def get_stylesheets(root):
    res = []
    for a in root.xpath('//style'):
        src = a.get('src')
        if src:
            res.append((a.sourceline, src))
    return res

def get_iframes(root):
    res = []
    for a in root.xpath('//iframe'):
        src = a.get('src')
        if src:
            res.append((a.sourceline, src))
    return res



def getall(root):

    assets = {}
    assets['A'] = get_anchors(root)
    assets['IMG'] = get_images(root)
    assets['STYLESHEET'] = get_stylesheets(root)
    assets['SCRIPT'] = get_scripts(root)
    assets['IFRAME'] = get_scripts(root)
    return assets


def get_page(url):

    root = lxml.html.parse(url).getroot()
    root.make_links_absolute()
    return root

def main():

    try:
        url = sys.argv[1]
    except:
        url = 'http://www.nytimes.com/'

    root = get_page(url)
    assets = getall(root)

    res = []
    for tag, lst in assets.items():
        for asset in lst:
            res.append((tag,asset[0],asset[1]))

    for r in sorted(res, key=itemgetter(1)):
        sys.stdout.write('%s\t%s\t%s\n' % (r[0],r[1],r[2]))


if __name__ == "__main__":
    main()

