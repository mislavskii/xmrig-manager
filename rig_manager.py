import json
from pprint import pprint
import random
from pathlib import Path
import signal
import subprocess
import requests as rq

from dotenv import load_dotenv, set_key
import os

load_dotenv()


class RigManager:

    def __init__(self, working_dir=''):
        if working_dir and Path(working_dir).exists():
            set_key('.env', 'DEFAULT_DIR', working_dir)
            self.working_dir = Path(working_dir)
        else:
            self.working_dir = Path(os.getenv('DEFAULT_DIR', ''))
            print(f'No valid new dir provided. Defaulting to "{self.working_dir}"')
        self.config_path = self.working_dir / 'config.json'
        with open(self.config_path, 'r') as file:
            self.config_dict = json.load(file)
        self.wallets = [pool['user'] for pool in self.config_dict['pools']]

    def launch(self):
        print('Launching the rig...')
        rig_path = self.working_dir / "xmrig"
        try:
            self.xmrig_process = subprocess.Popen([
                "gnome-terminal", "--",
                rig_path
            ])
        except Exception as e:
            print(e)

    def set_ncores(self, n):
        all_cores = self._prepare_core_list()
        if n > len(all_cores):
            n = len(all_cores)
            print('Desired number of cores exceeds available. Set to max available.')
        if n < 1:
            n = 1
            print('Invalid value below min. Set to 1')
        cores_to_use = sorted(random.sample(all_cores, n))
        print(cores_to_use)
        self.config_dict['cpu']['rx'] = cores_to_use
        try:
            with open(self.config_path, 'w') as file:
                json.dump(self.config_dict, file, indent=2)
        except OSError as e:
            print(e)

    def get_stats(self):
        for wallet in self.wallets:
            print(f'Getting stats for {wallet}...')
            stat_url = f'https://api.moneroocean.stream/miner/{wallet}/stats'
            resp = rq.get(stat_url, timeout=30)
            pprint(resp.json())

    def get_cwd(self):
        return os.getenv('DEFAULT_DIR', '')  # TODO: test
    
    def get_cores(self):  # TODO: test
        return self.config_dict['cpu']['rx']
    
    def stop(self):
        print('Stopping the rig...')
        subprocess.run(["pkill", "-2", "xmrig"])

    def _prepare_core_list(self) -> list[int]:
        return self.config_dict['cpu']['rx/wow']
