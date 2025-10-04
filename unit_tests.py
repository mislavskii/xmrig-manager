# Perplexity-generated

import unittest
import os
from pathlib import Path
from rig_manager import RigManager  # Adjust import if needed


class TestRigManager(unittest.TestCase):

    def setUp(self):
        # Prepare environment variable for DEFAULT_DIR
        os.environ['DEFAULT_DIR'] = '/tmp/test_rig_dir'
        # Prepare a dummy config.json in that directory
        test_dir = Path(os.environ['DEFAULT_DIR'])
        test_dir.mkdir(parents=True, exist_ok=True)
        config_path = test_dir / 'config.json'

        # Write sample config content with cpu.rx and cpu.rx/wow keys
        sample_config = {
            "cpu": {
                "rx": [0, 1, 2, 3],
                "rx/wow": [0, 1, 2, 3, 4]
            },
            "pools": [
                {"user": "wallet1"},
                {"user": "wallet2"}
            ]
        }
        with open(config_path, 'w') as f:
            import json
            json.dump(sample_config, f)

    def test_get_cwd_returns_env_value(self):
        rig_manager = RigManager()
        cwd = rig_manager.get_cwd()
        self.assertEqual(cwd, os.environ['DEFAULT_DIR'])

    def test_get_cores_returns_correct_list(self):
        rig_manager = RigManager()
        cores = rig_manager.get_cores()
        self.assertEqual(cores, [0, 1, 2, 3])

    def tearDown(self):
        # Clean up test files and folders if needed
        test_dir = Path(os.environ['DEFAULT_DIR'])
        config_path = test_dir / 'config.json'
        if config_path.exists():
            config_path.unlink()
        if test_dir.exists():
            try:
                test_dir.rmdir()
            except OSError:
                pass  # Directory not empty or in use


if __name__ == '__main__':
    unittest.main()
