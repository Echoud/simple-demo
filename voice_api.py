import hashlib
import hmac
import sys

def get_signature(channel_uuid, service_uuid, user_uuid, time, client_secret):
    content = '{}{}{}{}'.format(channel_uuid, service_uuid or '', user_uuid, time)
    digester = hmac.new(client_secret, content, hashlib.sha256)
    print digester.hexdigest()


if __name__ == "__main__":
    get_signature(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
