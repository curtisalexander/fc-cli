#!/usr/bin/env python

# standard library
import os

# third party
import click
import requests

@click.command()
@click.option('--lookup', type=click.Choice(['email', 'phone', 'twitter']), help='lookup type')
@click.option('--lookup-value', help='lookup value: email, phone, twitter')
@click.option('--json', type=click.Path(), help='json file path')

# even though the cli option is 'lookup-value'
# it is passed in as lookup_value
def fc(lookup, lookup_value, json):
    """ Query the Full Contact Person API """
    API_KEY = get_api_key('fc_key')
    URL = 'https://api.fullcontact.com/v2/person.json'

    headers = {'X-FullContact-APIKey': API_KEY}

    parameters = {'prettyPrint': 'true'}
    if lookup == 'email':
        parameters['email'] = lookup_value
    elif lookup == 'phone':
        no_dash_paren = str.maketrans('', '', '()-')
        parameters['phone'] = '+1' + lookup_value.translate(no_dash_paren)
    elif lookup == 'twitter':
        parameters['twitter'] = lookup_value
    else:
        raise ValueError('--lookup should be one of email, phone, or twitter')

    r = requests.post(URL, headers=headers, params=parameters)

    print('Full Contact return status code: {_status}'.format(_status = r.status_code))
    print('Full Contact return datetime: {_dt}'.format(_dt = r.headers['Date']))
    print('Full Contact rate limit: {_ratelimit} calls / {_ratelimitreset} seconds'.format( \
        _ratelimit = r.headers['X-Rate-Limit-Limit'], \
        _ratelimitreset = r.headers['X-Rate-Limit-Reset']))
    print('Full Contact rate limit remaining: {_ratelimitremaining} calls / {_ratelimitreset} seconds'.format( \
        _ratelimitremaining = r.headers['X-Rate-Limit-Remaining'], \
        _ratelimitreset = r.headers['X-Rate-Limit-Reset']))

    with open(json, 'w') as j:
        j.write(r.text)


def get_api_key(api_file):
    """ Return an API key from the user's home directory """
    with open('{_home}/.{_api_file}'.format(_home = os.path.expanduser('~'),
                                            _api_file = api_file)) as f:
        return f.read().replace('\n', '')


if __name__ == '__main__':
    fc()
