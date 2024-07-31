from flappy_tester import FlappyBird

fb = FlappyBird()
top_left_x_y_cor = fb.start_game()  # runs only the first time when you start the python script
fb.start_gameplay_loop(fb.frame_count, top_left_x_y_cor, fb.pipe_position, fb.bird_position)

# ../images/main_screen.png
# if 1 thread