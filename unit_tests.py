# Perplexity-generated

import unittest
import os
from pathlib import Path
from dotenv import load_dotenv
from rig_manager import RigManager  # Adjust import as needed


class TestRigManagerWithEnvConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load environment variables from actual .env file in project root
        load_dotenv()  # loads .env from current working directory by default

    def setUp(self):
        # Retrieve DEFAULT_DIR from loaded environment variables
        self.default_dir = os.getenv('DEFAULT_DIR')
        self.assertIsNotNone(self.default_dir, "DEFAULT_DIR must be set in .env")

        # Verify config.json exists in DEFAULT_DIR
        config_path = Path(self.default_dir) / 'config.json'
        self.assertTrue(config_path.exists(), f"Config file not found at {config_path}")

        # Instantiate RigManager with no arguments so it uses DEFAULT_DIR from environment
        self.rig_manager = RigManager()

    def test_get_cwd_returns_default_dir(self):
        cwd = self.rig_manager.get_cwd()
        self.assertEqual(cwd, self.default_dir)

    def test_get_cores_returns_configured_cores(self):
        cores = self.rig_manager.get_cores()

        # Load the config manually to compare
        import json
        with open(Path(self.default_dir) / 'config.json', 'r') as f:
            config_dict = json.load(f)
        expected_cores = config_dict['cpu']['rx']

        self.assertEqual(cores, expected_cores)


if __name__ == '__main__':
    unittest.main()
