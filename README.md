# fc_cli
Command line script to query Full Contact's RESTful [Person API](https://www.fullcontact.com/developer/docs/person).  Able to query using
* email
* phone
* Twitter username
* Facebook username

## Usage
```
fc.py [OPTIONS]

Options:
  --lookup [email|phone|twitter|facebook] lookup type
  --lookup-value TEXT             lookup value: email, phone, twitter, facebook
  --json PATH                     json file path
  --help                          Show this message and exit.
```

## Example
```
fc_cli.py --lookup=email --lookup-value=myaddress@gmail.com --json=results.json

fc_cli.py --lookup=phone --lookup-value=7737654321 --json=results.json
```

## Requirements
Full Contact API key is required.  Place the key in the following location.

`~/.fc_key`

## Software Requirements
* [click](http://click.pocoo.org/6) - Python package for creating beautiful command line interfaces 

```
pip install click
```
or
```
conda install click
```
* [requests](http://docs.python-requests.org/en/latest) - HTTP for Humans

```
pip install requests
```
or
```
conda install requests
```

## Related
[fullcontact.py](https://github.com/garbados/fullcontact.py) - Python implmentation referenced by the Full Contact docs
