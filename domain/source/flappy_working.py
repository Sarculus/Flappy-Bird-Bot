from PIL import Image, ImageOps
import numpy as np
from datetime import date
import time
import mss
import mss.tools
import threading
from threading import Timer
import win32api
from win32api import GetSystemMetrics
import win32con
import redis


class FlappyBird:
    pipe_position = -1
    bird_position = 295
    old_bird_speed = 0
    position_click_on = True


    def start_game(self):
        self.make_screenshot()
        screen_resolution = [GetSystemMetrics(0), GetSystemMetrics(1)]
        top_left_x_y_cor = self.find_game_frame_area('domain/images/main_screen.png', screen_resolution)
        win32api.SetCursorPos((top_left_x_y_cor[0] + 250, top_left_x_y_cor[1] + 550))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        return top_left_x_y_cor

    def make_screenshot(self):
        with mss.mss() as sct:
            sct.shot(output="domain/images/main_screen.png")

    def find_game_frame_area(self, image_path, screen_resolution):
        main_screen = Image.open(image_path)
        origin_x = int(screen_resolution[0] / 2)
        origin_y = int(screen_resolution[1] / 2)
        x_gamescreen = main_screen.crop((0, origin_y, screen_resolution[0], origin_y + 1))
        y_gamescreen = main_screen.crop((origin_x, 100, origin_x + 1, screen_resolution[1]))
        gray_frame_x = ImageOps.grayscale(x_gamescreen)
        gray_frame_y = ImageOps.grayscale(y_gamescreen)
        image_pixel_values_x = np.array(gray_frame_x.getdata())
        image_pixel_values_y = np.array(gray_frame_y.getdata())

        x_cor_gamescreen = 0; y_cor_gamescreen = 0
        for i in range(len(image_pixel_values_x)):
            if image_pixel_values_x[i] == 176:
                x_cor_gamescreen = i
                break
        for i in range(len(image_pixel_values_y)):
            if image_pixel_values_y[i] == 176:
                y_cor_gamescreen = i + 100  # +100 because i is 0 at pixel-y = 100
                break

        return x_cor_gamescreen, y_cor_gamescreen


    def start_gameplay_loop(self, top_left_x_y_cor, pipe_position_top, old_bird_position, old_bird_speed):
        image_path = 'domain/images/screen.png'
        while True:
            self.update_saved_screen(top_left_x_y_cor)
            new_bird_position = self.get_bird_position(image_path) + 15  # bird head to centre is 15 px
            new_bird_speed = new_bird_position - old_bird_position  # positive when going down
            bird_speed_avg = (new_bird_speed + old_bird_speed) / 2
            old_bird_speed = new_bird_speed
            old_bird_position = new_bird_position
            pipe_position_update = self.get_pipe_position(image_path)
            if pipe_position_update != 0 and self.bird_not_in_pipe(image_path):
                pipe_position_top = pipe_position_update
            print(new_bird_position, pipe_position_top, pipe_position_top + 180,bird_speed_avg,threading.active_count())
            self.do_a_click_action(new_bird_position, pipe_position_top)

            if (self.bird_0_to_30_from_bottom_pipe_and_going_down(new_bird_speed, new_bird_position, pipe_position_top) and  #TODO: second onewithout speed requirment?
                    29 < bird_speed_avg < 100) and self.position_click_on:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                print("position click---------------------->")
                t = Timer(0.0, self.go_click)
                t.start()
                self.position_click_on = False
            if self.check_end_game(image_path):
                self.end_game(top_left_x_y_cor, image_path)
                break
            print("---------------------------")

    def update_saved_screen(self, game_cor):
        img_name = 'domain/images/screen.png'
        with mss.mss() as sct:
            sct_img = sct.grab({"top": game_cor[1], "left": game_cor[0], "width": 500, "height": 600})
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=img_name)

    def get_bird_position(self, image_path):
        frame = Image.open(image_path)

        origin_x = 142
        origin_y = 0
        size_x = 1
        size_y = 600
        image_section_bird = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        gray_frame = ImageOps.grayscale(image_section_bird)
        image_pixel_values = np.array(gray_frame.getdata())

        bird_position = -1
        for i in range(len(image_pixel_values)):
            if image_pixel_values[i] == 181:
                bird_position = i
                break

        return bird_position

    def get_pipe_position(self, image_path):
        frame = Image.open(image_path)

        origin_x = 410
        origin_y = 0
        size_x = 1
        size_y = 600
        image_section_pipe = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        gray_frame = ImageOps.grayscale(image_section_pipe)
        image_pixel_values = np.array(gray_frame.getdata())  # turn into an array of rgb numbers (0-255)

        for i in range(len(image_pixel_values)):
            if image_pixel_values[i] == 176:
                pipe_position = i
                return pipe_position
        return -1

    def bird_not_in_pipe(self, image_path):
        frame = Image.open(image_path)

        origin_x = 150
        origin_y = 0
        size_x = 1
        size_y = 1
        image_section_pipe = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        gray_frame = ImageOps.grayscale(image_section_pipe)
        image_pixel_value = np.array(gray_frame.getdata())
        if image_pixel_value == 176:
            return True
        return False





    def bird_0_to_30_from_bottom_pipe_and_going_down(self, bird_speed, new_bird_position, pipe_position_top):
        if pipe_position_top + 72 < new_bird_position < pipe_position_top + 190 and bird_speed > 1:
            return True
        return False

    def do_a_click_action(self, bird_position, pipe_position_top):
        if pipe_position_top == -1 or bird_position == -1:
            print('no data, go down')
        elif pipe_position_top + 100 <= bird_position <= pipe_position_top + 180 and threading.active_count() < 3:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            print('go steady')
            t = Timer(0.0, self.go_steady)
            t.start()
        elif bird_position > pipe_position_top + 180 and threading.active_count() < 3:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            print('go up')
        elif bird_position < pipe_position_top + 98:
            print('go down')









    def go_steady(self):
        time.sleep(0.51)

    def go_click(self):
        time.sleep(0.20)
        self.position_click_on = True




    def check_end_game(self, image_path):
        frame = Image.open(image_path)

        origin_x = 140
        origin_y = 599
        size_x = 1
        size_y = 1

        end_game_screen = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        image_pixel_value = np.array(end_game_screen.getdata())
        if image_pixel_value[0][0] == 227:
            return True
        return False








    def end_game(self, top_left_x_y_cor, image_path):
        print("end game")
        print("-------------------------------")
        time.sleep(3)
        self.update_saved_screen(top_left_x_y_cor)
        score = self.get_score(image_path)
        print(score)
        date_dmy = f"{date.today().day}-{date.today().month}-{date.today().year}"
        r = redis.Redis(
            host='redis-17414.c327.europe-west1-2.gce.redns.redis-cloud.com',
            port=17414,
            password='TZgxGtwgJost678XJpsSKdndjYFBQltA',
            decode_responses=True)
        r.incr('idcounter')
        name = f"{r.get('idcounter')} {date_dmy}"
        r.zadd('highscorestest7', {name: score})

    def get_score(self, image_path):
        frame = Image.open(image_path)
        origin_x = 385; origin_y = 310; size_x = 22; size_y = 32
        first_digit = self.number_from_image(frame, origin_x, origin_y, size_x, size_y)

        origin_x = 357
        second_digit = self.number_from_image(frame, origin_x, origin_y, size_x, size_y)

        origin_x = 329
        third_digit = self.number_from_image(frame, origin_x, origin_y, size_x, size_y)

        print(third_digit, second_digit, first_digit)
        score = int(str(third_digit) + str(second_digit) + str(first_digit))
        return score

    def number_from_image(self, frame, origin_x, origin_y, size_x, size_y):
        end_game_screen = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        end_game_screen_pixel_topleft = frame.crop((origin_x + 2, origin_y + 9, origin_x + 3, origin_y + 10))
        end_game_screen_pixel_bottomleft = frame.crop((origin_x + 2, origin_y + 19, origin_x + 3, origin_y + 20))


        gray_frame = ImageOps.grayscale(end_game_screen)
        image_pixel_values = np.array(gray_frame.getdata())
        image_pixel_value = np.mean(image_pixel_values)
        print(round(image_pixel_value))

        topleft_pixel = np.array(end_game_screen_pixel_topleft.getdata())
        bottomleft_pixel = np.array(end_game_screen_pixel_bottomleft.getdata())

        if round(image_pixel_value) == 147 or round(image_pixel_value) == 144:
            return 1
        elif round(image_pixel_value) == 149:
            return 4
        elif round(image_pixel_value) == 165:
            return 6
        elif round(image_pixel_value) == 153:
            return 7
        elif round(image_pixel_value) == 172:
            return 8
        elif round(image_pixel_value) == 162 and bottomleft_pixel[0][0] == 0:
            return 9
        elif topleft_pixel[0][0] == 255 and bottomleft_pixel[0][0] == 255:
            return 0
        elif topleft_pixel[0][0] == 0 and bottomleft_pixel[0][0] == 255:
            return 2
        elif topleft_pixel[0][0] == 0 and bottomleft_pixel[0][0] == 0:
            return 3
        elif topleft_pixel[0][0] == 255 and bottomleft_pixel[0][0] == 0:
            return 5
        else:
            return 0
