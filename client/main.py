from password_manager_client.cryptography.aes_cipher import AESCipher
import argparse
import requests
import pprint
import json

def get_arguments() -> argparse.ArgumentParser.parse_args:
    parser = argparse.ArgumentParser(description='Client for password managert')

    parser.add_argument('--key', dest='key', required=True,
                        help='Key to read/write databse')

    parser.add_argument('--action', dest='action', required=True,
                        help='Action to perform ;')


    args = parser.parse_args()
    return args
def add_password(key: str, data: dict):
    aes_cipher = AESCipher(key)
def get_passwords(key) -> requests.Response:
    response = requests.get('http://0.0.0.0:8000/passwords/?skip=0&limit=100')
    return json.loads(response.text)

if __name__ == '__main__':
    args = get_arguments()
    if args.action == 'add_password':
        add_password(args)
    elif args.action == 'get_passwords':
        responses = get_passwords(args.key)
    for response in responses:
        pprint.pprint(response)
    # cipher_text = aes_cipher.encrypt('hello world!')
    # text = aes_cipher.decrypt(cipher_text)
    # print(cipher_text)
    # print(text)
