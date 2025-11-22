import yaml
from typing import Dict

def load_projects() -> Dict[str, Dict[str, str]]:
    with open('config/projects.yml', 'r') as f:
        data = yaml.full_load(f)
        return data