import json
from pprint import pprint
import random
from pathlib import Path
import signal
import subprocess
import requests as rq

from dotenv import load_dotenv
import os

load_dotenv()


class RigManager:
    STAT_URL = f'https://api.moneroocean.stream/miner/{os.getenv('WALLET')}/stats'

    def __init__(self, working_dir=''):
        self.working_dir = Path(working_dir if working_dir else os.getenv('DEFAULT_DIR', ''))
        self.config_path = self.working_dir / 'config.json'
        with open(self.config_path, 'r') as file:
            self.config_dict = json.load(file)

    def launch(self):
        print('Launching the rig...')
        rig_path = self.working_dir / "xmrig"
        self.xmrig_process = subprocess.Popen([
            "gnome-terminal", "--",
            rig_path
        ])

    def set_ncores(self, n):
        all_cores = self._prepare_core_list()
        cores_to_use = sorted(random.sample(all_cores, n))
        print(cores_to_use)
        self.config_dict['cpu']['rx'] = cores_to_use
        try:
            with open(self.config_path, 'w') as file:
                json.dump(self.config_dict, file)
        except OSError as e:
            print(e)

    def get_stats(self):
        resp = rq.get(self.STAT_URL, timeout=30)
        pprint(resp.json())

    def stop(self):
        print('Stopping the rig...')
        subprocess.run(["pkill", "-2", "xmrig"])

    def _prepare_core_list(self) -> list[int]:
        return self.config_dict['cpu']['rx/wow']
