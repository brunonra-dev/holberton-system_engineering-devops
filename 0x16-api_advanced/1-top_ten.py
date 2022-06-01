#!/usr/bin/python3
'''
Queries the Reddit API and prints the titles of
the first 10 hot posts
'''
import requests


def top_ten(subreddit):
    '''Function'''
    url = 'http://reddit.com/r/{}/hot.json'
    header = {'User-agent': 'Prueba:1-top_ten:v1'}
    res = requests.get(url.format(subreddit), headers=header)
    inf = res.json().get('data', {}).get('children', {})
    if res.status_code != 200:
        return print('None')
    for x in inf[0:10]:
        print(x.get('data', {}).get('title'))
