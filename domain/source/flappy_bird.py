import threading
from threading import Timer
from PIL import Image, ImageOps
import mss
import mss.tools
import pyautogui
import time
import numpy as np
import win32api
import win32con

#TODO: variables: sleeptime of each click method, cusion distance between pipe, x cordinate of polling pixel line for a new pipe

class FlappyBird:
    frame_count = 0
    pipe_position = -1

    def __init__(self):
        pass


    def start_game(self):
        self.make_screenshot()
        top_left_x_y_cor = self.find_game_frame_area('../images/main_screen.png')
        # pyautogui.click((top_left_x_y_cor[0] + 250, top_left_x_y_cor[1] + 480))
        # time.sleep(0.3)
        pyautogui.click((top_left_x_y_cor[0] + 250, top_left_x_y_cor[1] + 550))
        time.sleep(0.3)
        pyautogui.leftClick()
        return top_left_x_y_cor

    def start_gameplay_loop(self, frame_count, top_left_x_y_cor, pipe_position_top):
        while True:
            self.update_saved_screen(frame_count, top_left_x_y_cor)
            image_path = '../images/screen{0}.png'.format(frame_count)
            if self.check_end_game(image_path):
                print("end game")
                print("-------------------------------")
                exit()
                # time.sleep(2.0)
                # self.start_game()
            bird_position = self.get_bird_position(image_path) + 15  # bird head to centre is 15 px
            pipe_position_update = self.get_pipe_position(image_path)  # + 90  #half of pipe gape is 90 px
            if pipe_position_update != 0 and (self.bird_not_in_pipe(image_path)):
                pipe_position_top = pipe_position_update
            frame_count += 1
            print(bird_position, pipe_position_top, pipe_position_top + 180)
            if threading.active_count() == 1:  # Only click when the previous click thread is finished
                self.do_a_click_action(bird_position, pipe_position_top)

    def do_a_click_action(self, bird_position, pipe_position_top):
        if pipe_position_top == -1 or bird_position == -1:  # TODO: extra flap when large distance to cover?
            t = Timer(0.0, self.go_down)
            t.start()  # method will execute after x seconds independent of the main thread
        elif bird_position < pipe_position_top + 94:  # 70top 110bottom seems good value, (100, 160)
            t = Timer(0.0, self.go_down)
            t.start()  # method will execute after x seconds independent of the main thread
        elif bird_position > pipe_position_top + 180:  # 180 is pipe gap in pixels
            self.click()
            t = Timer(0.0, self.go_up)
            t.start()  # method will execute after x seconds independent of the main thread
        else:
            self.click()
            t = Timer(0.0, self.go_steady)
            t.start()  # method will execute after x seconds independent of the main thread
        print("--------------------------thread started")

    def make_screenshot(self):
        with mss.mss() as sct:
            sct.shot(output="../images/main_screen.png")  # taking a screenshot and saving it to an image file


    def find_game_frame_area(self, image_path):
        main_screen = Image.open(image_path)
        screen_resolution = pyautogui.size()
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

    def click(self):
        # win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        # time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        print('-----------------------------clicked')

    def go_up(self):
        print('go up')
        #pyautogui.leftClick()
        # time.sleep(0.01)  # temp as a test
        #self.click()
        time.sleep(0.28)  #0.35 0.30 0.25

    def go_down(self):
        print('go down')
        #pyautogui.leftClick()
        # self.click()
        # time.sleep(0.40)

    def go_steady(self):
        print('go steady')
        #pyautogui.leftClick()
        #self.click()
        time.sleep(0.50)  #0.50 0.45 0.40

    def update_saved_screen(self, count, game_cor):
        img_name = '../images/screen{0}.png'.format(count)
        with mss.mss() as sct:
            sct_img = sct.grab({"top": game_cor[1], "left": game_cor[0], "width": 500, "height": 700})
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=img_name)
        # iml = pyautogui.screenshot(region=(game_cor[0], game_cor[1], 500, 700))  # 50% slower then mss
        # iml.save(img_name)


    def check_end_game(self, image_path):
        frame = Image.open(image_path)

        origin_x = 140 # top left corner of the image section
        origin_y = 599 # top left corner of the image section
        size_x = 1  # section width
        size_y = 1  # section height

        end_game_screen = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        image_pixel_value = np.array(end_game_screen.getdata())
        if image_pixel_value[0][0] == 227:
            return True
        return False


    def get_bird_position(self, image_path):
        frame = Image.open(image_path)  # opening latest screenshot from the image file

        origin_x = 142  # top left corner of the image section
        origin_y = 0  # top left corner of the image section
        size_x = 1  # section width
        size_y = 600  # section height
        image_section_bird = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        gray_frame = ImageOps.grayscale(image_section_bird)
        image_pixel_values = np.array(gray_frame.getdata())  # turn into an array of rgb numbers (0-255)

        bird_position = -1
        for i in range(len(image_pixel_values)):
            if image_pixel_values[i] == 181:
                bird_position = i
                break

        return bird_position

    def get_pipe_position(self, image_path):
        frame = Image.open(image_path)
        #frame = Image.open('./screen.png')  # opening latest screenshot from the image file

        origin_x = 400 #375 380 420 #390 #499  # top left corner of the image section
        origin_y = 0  # top left corner of the image section
        size_x = 1  # section width
        size_y = 600  # section height
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

        origin_x = 155  # 142
        origin_y = 0
        size_x = 1
        size_y = 1
        image_section_pipe = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        gray_frame = ImageOps.grayscale(image_section_pipe)
        image_pixel_value = np.array(gray_frame.getdata())
        if image_pixel_value == 176:
            return True
        return False
