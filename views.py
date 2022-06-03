import os

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
        return {'ok': True, 'type': 'dir', 'files': items[1] + items[2]}

    try:
        with open(path, encoding='utf-8') as file:
            return {'ok': True, 'type': 'file', 'text': file.read()}
    except Exception as e:
        return {'ok': False, 'error': e}


# elif text := request.json['text']:
#     with open(file_path, encoding='utf-8', mode='w') as file:
#         file.write(text.replace('\r\n', '\n'))
#
#     return {'ok': True}


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
