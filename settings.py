from environs import Env
from pathlib import Path

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent

CODA_API_TOKEN = env.str('CODA_API_TOKEN')
