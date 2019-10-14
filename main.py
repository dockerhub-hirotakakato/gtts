#!/usr/bin/python3

import os

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ja')

from flask import Flask, request, Response
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

@app.route('/<path:text>.mp3')
def mp3(text):
    lang = request.args.get('lang', DEFAULT_LANG)
    fp   = BytesIO()

    gTTS(text, lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
