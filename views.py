import os
import subprocess

from flask import request

import api
import config
from loader import app


@app.route('/get/<path:path>')
def get(path: str):
    path = config.PROJECTS_DIR / path

    if not os.path.exists(path):
        return {'ok': False, 'error': 'Not found'}

    if os.path.isdir(path):
        walker = os.walk(path)
        items = next(walker)
        return {'ok': True, 'type': 'dir', 'items': items[1] + items[2]}

    try:
        with open(path, encoding='utf-8') as file:
            return {'ok': True, 'type': 'file', 'text': file.read()}
    except Exception as e:
        return {'ok': False, 'error': e}


@app.route('/edit/<path:path>', methods=['POST'])
def edit(path: str):
    path = config.PROJECTS_DIR / path

    if not os.path.exists(path):
        return {'ok': False, 'error': 'Not found'}

    if os.path.isdir(path):
        return {'ok': False, 'error': 'Not a file'}

    text = request.json.get('text')

    if text is None:
        return {'ok': False, 'error': 'Invalid text'}

    try:
        with open(path, encoding='utf-8', mode='w') as file:
            file.write(text.replace('\r\n', '\n'))
            return {'ok': True}
    except Exception as e:
        return {'ok': False, 'error': e}


@app.route('/deploy/<project>')
def deploy(project: str):
    subprocess.run('. scripts/deploy.sh &', shell=True, cwd=config.PROJECTS_DIR / project)
    return {'ok': True}


@app.route('/stop/<project>')
def stop(project: str):
    subprocess.run('. scripts/stop.sh &', shell=True, cwd=config.PROJECTS_DIR / project)
    return {'ok': True}
