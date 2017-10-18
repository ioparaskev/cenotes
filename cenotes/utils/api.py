import json
from cenotes.utils import CENParams


def craft_json_response(
        success=True, error="", enote=None, plaintext="", key="", payload=""):

    return json.dumps(
        {"success": success if not error else False,
         "error": error,
         "key": key,
         "plaintext": plaintext,
         "payload": payload,
         "expiration_date": enote.iso_expiration_date if enote else "",
         "max_visits": enote.max_visits if enote else ""})


def get_request_params(request_params):
    return CENParams(**request_params)
