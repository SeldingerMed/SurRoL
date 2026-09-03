"""Minimal installed-package smoke test for the headless NeedleReach path."""

import numpy as np

from surrol.tasks.needle_reach import NeedleReach


def test_headless_needle_reach() -> None:
    env = NeedleReach(render_mode=None)
    try:
        observation = env.reset()
        assert set(observation) == {"achieved_goal", "desired_goal", "observation"}
        action = env.get_oracle_action(observation)
        assert action.shape == (5,)
        _, _, done, info = env.step(action)
        assert done is False
        assert "is_success" in info
    finally:
        env.close()


def _seeded_goal(seed: int) -> np.ndarray:
    env = NeedleReach(render_mode=None)
    try:
        env.seed(seed)
        return env.reset()["desired_goal"]
    finally:
        env.close()


def test_headless_needle_reach_seed_controls_anatomy() -> None:
    np.testing.assert_array_equal(_seeded_goal(7), _seeded_goal(7))
    assert not np.array_equal(_seeded_goal(7), _seeded_goal(8))
