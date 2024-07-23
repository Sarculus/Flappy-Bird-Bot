import pytest
from domain.main.flappy_bird import FlappyBird


class TestFlappyBird:

    def setup_method(self):  # before each tests
        self.fb = FlappyBird()

    # def test_find_game_frame_area(self):
    #     assert self.fb.find_game_frame_area() == (590, 213)  # 1680x1050 screen
    #
    # def test_bird_position(self):
    #     assert self.fb.get_bird_position() == 532

    def test_unit_testing_method(self):
        assert self.fb.unit_testing_method() == 10

    def teardown_method(self):  # after each tests
        del self.fb  # example, happens automatically
