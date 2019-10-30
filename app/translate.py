import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, source_language, dest_language):
    if "MS_TRANSLATOR_KEY" not in current_app.config or not current_app.config["MS_TRANSLATOR_KEY"]:
        return _("Error: the translation service is not configured")
    auth = {"Ocp-Apim-Subscription-Key": current_app.config["MS_TRANSLATOR_KEY"]}
    params = {"api-version": "3.0", "from": source_language, "to": dest_language}
    r = requests.post(
        "https://api.cognitive.microsofttranslator.com/translate",
        headers=auth,
        params=params,
        json=[{"Text": text}],
    )
    if r.status_code != requests.codes.ok:
        return _("Error: the translation service failed (status=%(status)d", status=r.status_code)

    return json.loads(r.content.decode("utf-8-sig"))[0]["translations"][0]["text"]
