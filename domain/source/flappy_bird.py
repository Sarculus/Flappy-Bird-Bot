from PIL import Image, ImageOps
import mss
import mss.tools
import pyautogui
import time
import numpy as np
import win32api
import win32con


class FlappyBird:
    frame_count = 0
    pipe_position = -1

    def __init__(self):
        pass

    def unit_testing_method(self):
        return 10

    def start_game(self):
        top_left_x_y_cor = self.find_game_frame_area()
        #pyautogui.click((game_cor[0] + 250, game_cor[1] + 480))
        pyautogui.click((top_left_x_y_cor[0] + 250, top_left_x_y_cor[1] + 550))
        time.sleep(0.3)
        pyautogui.leftClick()
        return top_left_x_y_cor

    def start_gameplay_loop(self, frame_count, top_left_x_y_cor, pipe_position_top):
        while True:
            self.update_saved_screen(frame_count, top_left_x_y_cor)
            self.check_end_game(frame_count)
            self.crop_bird_area(frame_count)
            self.crop_pipe_area(frame_count)
            frame_count += 1
            bird_position = self.get_bird_position() + 15  # bird head to centre is 15 px
            pipe_position_update = self.get_pipe_position()  # + 90  #half of pipe gape is 90 px
            if pipe_position_update != 0:
                pipe_position_top = pipe_position_update
            print(bird_position, pipe_position_top, pipe_position_top + 180)
            if pipe_position_top == -1 or bird_position == -1:
                self.go_down()  # self.go_steady()
            elif bird_position < pipe_position_top:
                self.go_down()
            elif bird_position > pipe_position_top + 180:  # 180 is pipe gap in pixels
                self.go_up()
            else:
                self.go_steady()
            print("--------------------------")

    def find_game_frame_area(self):
        with mss.mss() as sct:
            sct.shot(output="../images/main_screen.png")  # taking a screenshot and saving it to an image file

        main_screen = Image.open('../images/main_screen.png')
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

    def go_up(self):
        #time.sleep(0.10)
        print('go up')
        #pyautogui.leftClick()
        self.click()

    def go_down(self):
        #time.sleep(0.30)
        print('go down')
        #pyautogui.leftClick()

    def go_steady(self):
        #time.sleep(0.25)
        print('go steady')
        #pyautogui.leftClick()
        self.click()

    def update_saved_screen(self, count, game_cor):
        img_name = '../images/screen{0}.png'.format(count)
        with mss.mss() as sct:
            sct_img = sct.grab({"top": game_cor[1], "left": game_cor[0], "width": 500, "height": 700})
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=img_name)
        # iml = pyautogui.screenshot(region=(game_cor[0], game_cor[1], 500, 700))  # 50% slower then mss
        # iml.save(img_name)


    def check_end_game(self, count):
        frame = Image.open('../images/screen{0}.png'.format(count))

        origin_x = 140 # top left corner of the image section
        origin_y = 599 # top left corner of the image section
        size_x = 1  # section width
        size_y = 1  # section height

        end_game_screen = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        image_pixel_values = np.array(end_game_screen.getdata())
        if image_pixel_values[0][0] == 227:
            print("end game")
            print("-------------------------------")
            exit()
            # time.sleep(1.2)
            # start_game()

    def crop_bird_area(self, count):
        frame = Image.open('../images/screen{0}.png'.format(count))  # opening latest screenshot from the image file

        origin_x = 142  # top left corner of the image section
        origin_y = 0  # top left corner of the image section
        size_x = 1  # section width
        size_y = 600  # section height

        image_section_bird = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        image_section_bird.save('../images/cropped_screen_bird.png')

    def crop_pipe_area(self, count):
        frame = Image.open('../images/screen{0}.png'.format(count))
        #frame = Image.open('./screen.png')  # opening latest screenshot from the image file

        origin_x = 390 #499  # top left corner of the image section
        origin_y = 0  # top left corner of the image section
        size_x = 1  # section width
        size_y = 600  # section height

        image_section_pipe = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))
        image_section_pipe.save('../images/cropped_screen_pipe.png')

    def get_bird_position(self):
        frame = Image.open('../images/cropped_screen_bird.png')

        gray_frame = ImageOps.grayscale(frame)
        image_pixel_values = np.array(gray_frame.getdata())  # turn into an array of rgb numbers (0-255)

        bird_position = -1
        for i in range(len(image_pixel_values)):
            if image_pixel_values[i] == 181:
                bird_position = i
                break

        return bird_position

    def get_pipe_position(self):
        frame = Image.open('../images/cropped_screen_pipe.png')

        gray_frame = ImageOps.grayscale(frame)
        image_pixel_values = np.array(gray_frame.getdata())  # turn into an array of rgb numbers (0-255)

        pipe_position = -1
        for i in range(len(image_pixel_values)):
            if image_pixel_values[i] == 176:
                pipe_position = i
                break

        return pipe_position
