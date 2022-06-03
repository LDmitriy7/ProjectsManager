import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECTS_DIR = Path(os.environ['PROJECTS_DIR'])
APP_HOST = os.environ['APP_HOST']
APP_PORT = int(os.environ['APP_PORT'])
