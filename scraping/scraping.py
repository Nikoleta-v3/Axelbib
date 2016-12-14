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


def get_arguments(api, word, start, count):
    if api == 'springer':
        arguments = [{'-a': None, '-t': word, '-s': start,
                      '-r': count, '-y': None, '-b': None}]
    else:
        arguments = [{'-a': None, '-b': word, '-s': start,
                      '-r': count, '-y': None, '-t': None},
                     {'-a': None, '-t': word, '-s': start,
                      '-r': count, '-y': None, '-b': None}]
    return arguments


def main_program(arguments):
    parameters = pp.parameters_fix(arguments=arguments)
    url = pp.create_url_search(parameters=parameters)
    response = pp.make_request(url)
    root = pp.get_root(response)
    article = pp.parse(root)
    return article, url

words = ["prisoner's dilemma", "prisoners evolution", "prisoner dilemma",
         "prisoner game theory", "Axelrod", "memory one strategy", "TFT",
         "tit for tat", "tit-for-tat", "zero determinant"]
apis = {"ieee": Ieee, "nature": Nature, "arxiv": Arxiv, "springer": Springer,
        "plos": Plos}
list_apis = ['nature', 'ieee', 'arxiv', 'springer', 'plos']
count = 10
validate = True
val = False

pbar = tqdm(total=(len(words)*len(apis)))

for wr in words:
    for p in list_apis:
        pp = apis[p]()
        start = 1
        article = True
        while article is not False:
            arguments = get_arguments(p, wr, start, count)
            for arg in arguments:
                article, url = main_program(arg)
                print(url)
                if not article:
                    article = False
                else:
                    for record in article:
                        try:

                            post = pp.to_json(record)
                            post['labels'], post['list_strategies'] = [], []
                            post['score'] = post.get('score', 'none')

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
                                    textfile.write('{},{},({})\n'.format(
                                                        post['key'], url,
                                                        post['unique_key']))
                        except ValueError:
                            ValueError()

                            with open('raised_key_error', 'a') as textfile:
                                textfile.write('{}'.format(url))

            start += 10
        pbar.update(1)









