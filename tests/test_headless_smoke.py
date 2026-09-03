"""Minimal installed-package smoke test for the headless NeedleReach path."""

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
