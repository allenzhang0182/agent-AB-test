import unittest

from src import recovery_probe


class RecoveryProbeTest(unittest.TestCase):
    def test_checkpoint_a(self):
        self.assertEqual(
            recovery_probe.checkpoint_a(),
            "workspace-loss-recovery-a",
        )
