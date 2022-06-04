import os
import subprocess

from flask import request

import config
from loader import app


@app.route('/projects')
def projects():
    walker = os.walk(config.PROJECTS_DIR)
    items = next(walker)
    return {'ok': True, 'projects': items[1]}


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
    export_handlers(project)
    subprocess.run('. scripts/deploy.sh &', shell=True, cwd=config.BOTS_DIR / project)
    return {'ok': True}


@app.route('/stop/<project>')
def stop(project: str):
    subprocess.run('. scripts/stop.sh &', shell=True, cwd=config.BOTS_DIR / project)
    return {'ok': True}


@app.route('/export/handlers/<project>')
def export_handlers(project: str):
    source_file = config.PROJECTS_DIR / project / 'handlers'
    target_file = config.BOTS_DIR / project / 'app/handlers/misc.py'

    try:
        with open(source_file, encoding='utf-8') as file:
            text = file.read()
        with open(target_file, encoding='utf-8', mode='w') as file:
            file.write(text)
        return {'ok': True}
    except Exception as e:
        return {'ok': False, 'error': e}
