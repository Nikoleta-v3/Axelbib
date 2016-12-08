import json
from tqdm import tqdm
import requests

from password import password
from arcas import *


def post_to_axelbib(post):
    """A function for posting to Axelbib
    """
    url = 'http://127.0.0.1:8000/article/'
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json.dumps(post), auth=('nikoleta', password), headers=headers)
    return r.status_code


def get_arguments(api, year, word, start, count):
    if api == 'springer':
        arguments = [{'-a': None, '-t': wr, '-s': start,
                      '-r': count, '-y': yr, '-b': None}]
    else:
        arguments = [{'-a': None, '-t': wr, '-s': start,
                      '-r': count, '-y': yr, '-b': None},
                     {'-a': None, '-b': wr, '-s': start,
                      '-r': count, '-y': yr, '-t': None}]
    return arguments


def main_program(arguments):
    parameters = pp.parameters_fix(arguments=arguments)
    url = pp.create_url_search(parameters=parameters)
    response = pp.make_request(url)
    root = pp.get_root(response)
    article = pp.parse(root)
    return article, url


years = list(range(1996, 2016))
words = ["prisoner's dilemma"]
apis = {"ieee": Ieee, "nature": Nature, "arxiv": Arxiv, "springer": Springer}
list_apis = ['ieee', 'arxiv', 'nature', 'springer']
count = 10
validate = True
val = False

pbar = tqdm(total=(len(years)*len(words)*len(apis)))
for yr in years:
    for wr in words:
        for p in list_apis:
            pp = apis[p]()
            start = 1
            article = True
            while article is not False:
                arguments = get_arguments(p, yr, wr, start, count)
                for arg in arguments:
                    article, url = main_program(arg)

                    if not article:
                        article = False
                    else:
                        for record in article:
                            try:
                                post = pp.to_json(record)
                            except:
                                KeyError()
                            if validate is True:
                                val = pp.validate_post(arg, post)
                            if val is True or validate is False:
                                make_post = post_to_axelbib(post)
                                with open('report', 'a') as textfile:
                                    textfile.write(
                                        '{}--{}--{}--({})\n'.format(
                                            make_post, post['key'], url,
                                            post['unique_key']))

                            else:
                                with open('failed_validation', 'a') as textfile:
                                    textfile.write('{}--{}--({})\n'.format(
                                                        post['key'], url,
                                                        post['unique_key']))
                            start += 10
                pbar.update(1)









