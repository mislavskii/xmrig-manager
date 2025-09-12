import json
import random

from dotenv import load_dotenv
import os

load_dotenv()


class RigManager:

    def __init__(self, config_path=''):
        self.config_path = config_path if config_path else os.getenv('DEFAULT_CONFIG_PATH', '')
        with open(self.config_path, 'r') as file:
            self.config_dict = json.load(file)

    def launch(self):
        print('Launching the rig...')

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

    def stop(self):
        print('Stopping the rig...')

    def _prepare_core_list(self) -> list[int]:
        return self.config_dict['cpu']['rx/wow']
    

if __name__ == '__main__':
    mgr = RigManager()
    mgr.set_ncores(6)