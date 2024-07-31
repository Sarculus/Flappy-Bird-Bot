from domain.source.flappy_tester import FlappyBird

class TestFlappyBird:

    def setup_method(self):  # before each tests
        self.fb = FlappyBird()

    def test_find_game_frame_area(self):
        # screen_resolution_1 = (1366, 768)
        screen_resolution_2 = (1600, 900)
        screen_resolution_3 = (1680, 1050)
        screen_resolution_4 = (1920, 1080)
        screen_resolution_5 = (2560, 1440)
        screen_resolution_6 = (3840, 2160)
        # top_left_x_y_cor_1 = self.fb.find_game_frame_area('../tests/test_images/main_screen.png', screen_resolution_1)
        top_left_x_y_cor_2 = self.fb.find_game_frame_area('../tests/test_images/bird_900.png', screen_resolution_2)
        top_left_x_y_cor_3 = self.fb.find_game_frame_area('../tests/test_images/main_screen.png', screen_resolution_3)
        top_left_x_y_cor_4 = self.fb.find_game_frame_area('../tests/test_images/bird_1080.png', screen_resolution_4)
        top_left_x_y_cor_5 = self.fb.find_game_frame_area('../tests/test_images/bird_1440.png', screen_resolution_5)
        top_left_x_y_cor_6 = self.fb.find_game_frame_area('../tests/test_images/bird_4k.png', screen_resolution_6)
        # assert top_left_x_y_cor_1 == (443, 140)
        assert top_left_x_y_cor_2 == (546, 180)
        assert top_left_x_y_cor_3 == (502, 214)
        assert top_left_x_y_cor_4 == (666, 260)
        assert top_left_x_y_cor_5 == (1014, 412)
        assert top_left_x_y_cor_6 == (1622, 720)

    def test_check_end_game(self):
        assert self.fb.check_end_game('../tests/test_images/end_game.png') is True
        assert self.fb.check_end_game('../tests/test_images/non_end_game.png') is False
        assert self.fb.check_end_game('../tests/test_images/bird_position_pipe.png') is False

    def test_get_bird_position(self):
        assert self.fb.get_bird_position('../tests/test_images/bird_position_cloud.png') == 496
        assert self.fb.get_bird_position('../tests/test_images/bird_position_ground.png') == 563
        assert self.fb.get_bird_position('../tests/test_images/bird_position_pipe.png') == 508
        assert self.fb.get_bird_position('../tests/test_images/bird_position_sky.png') == 232

    def test_get_pipe_position(self):
        assert self.fb.get_pipe_position('../tests/test_images/all_sky.png') == 0
        assert self.fb.get_pipe_position('../tests/test_images/all_pipe.png') == 318

    def test_bird_not_in_pipe(self):
        assert self.fb.bird_not_in_pipe('../tests/test_images/all_sky.png') is True
        assert self.fb.bird_not_in_pipe('../tests/test_images/all_pipe.png') is False

    def test_bird_0_to_30_from_bottom_pipe_and_going_down(self):
        assert self.fb.bird_0_to_30_from_bottom_pipe_and_going_down(-1, 458, 298) is False
        assert self.fb.bird_0_to_30_from_bottom_pipe_and_going_down(1, 458, 298) is False
        assert self.fb.bird_0_to_30_from_bottom_pipe_and_going_down(6, 480, 298) is False
        assert self.fb.bird_0_to_30_from_bottom_pipe_and_going_down(6, 445, 298) is False
        assert self.fb.bird_0_to_30_from_bottom_pipe_and_going_down(6, 458, 298) is True

    # def teardown_method(self):  # after each tests
    #     del self.fb  # example, happens automatically
