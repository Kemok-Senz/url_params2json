from urllib.parse import urlparse, parse_qs
from argparse import ArgumentParser
import json


parser = ArgumentParser()
parser.add_argument('-u', '--url', default=None, help='Typesense URL to parse')
parser.add_argument('-j', '--json', default=None, dest='json_file', help="The name of the JSON file to write to")


def run(url: str = None, json_file: str = None):
    query = {
        'group_by': 'nog',
        'page': '1',
        'per_page': '250'
    }

    # Parse the URL
    parsed_url = urlparse(url)
    # Get the query string from the parsed URL
    query_string = parsed_url.query
    # Parse the query string into a dictionary
    query_params = parse_qs(query_string)
    # Decode the values
    for key, values in query_params.items():
        query[key] = values[0]

    if json_file:
        print('creando el archivo json...')
        with open(json_file, 'w') as f:
            json.dump(query, f, indent=4)

    print('El query para Typesense es:')
    print(json.dumps(query, indent=4))


if __name__ == '__main__':
    try:
        args = parser.parse_args()
        if not args.url:
            raise Exception('URL no recibido, por favor ingrese un URL')
        print('params recibidos:', args)
        run(**vars(args))
    except Exception as e:
        print('Ocurrió un error:', e)
