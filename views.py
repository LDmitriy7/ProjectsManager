import os
from pathlib import Path

from flask import request

import api
from loader import app
import config


@app.route('/edit/<path:file_path>', methods=['GET', 'POST'])
def edit(file_path: str):
    file_path = config.PROJECTS_DIR / file_path

    if request.method == 'GET':
        with open(file_path, encoding='utf-8') as file:
            return {'text': file.read()}
    elif text := request.json['text']:
        with open(file_path, encoding='utf-8', mode='w') as file:
            file.write(text.replace('\r\n', '\n'))

        return {'ok': True}


@app.route('/deploy/<project>')
def deploy(project: str):
    with api.ChangeDir(config.PROJECTS_DIR / project):
        os.system('. scripts/deploy.sh')

    return {'ok': True}


@app.route('/stop/<project>')
def stop(project: str):
    with api.ChangeDir(config.PROJECTS_DIR / project):
        os.system('. scripts/stop.sh')

    return {'ok': True}
