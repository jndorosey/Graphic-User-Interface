class Key:
    def __init__(self, key_name, key_width, key_height, key_top_left_x, key_top_left_y):
        self.key_name = key_name
        self.key_width = key_width
        self.key_height = key_height
        self.key_top_left_x = key_top_left_x
        self.key_top_left_y = key_top_left_y
        self.key_color = 'light gray'
        self.key_tag = 0

class Keyboard:
    def __init__(self, keyboard_canvas):
        self.canvas = keyboard_canvas

        #  If you do not call the update function you will get the default value 1.
        keyboard_canvas.update()
        self.keyboard_width = keyboard_canvas.winfo_width()
        self.keyboard_height = keyboard_canvas.winfo_height()

        self.key_names = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                          ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                          ['Caps', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<--'],
                          ['123', 'Space', 'Return']]

        # Creating an empty list
        self.keys = []
        self.key_pressed = 0

    def get_keys(self):
        return self.keys

    def get_key_pressed(self):
        return self.key_pressed

    # design the keyboard layout
    def keyboard_layout(self):

        # the vertical gap between two keys
        vertical_key_gap = 8
        key_height = int((self.keyboard_height - vertical_key_gap * (len(self.key_names) + 1)) / 4)
        row = 0

        # the key layout for each row is different, so set each row respectively

        # the first row has the most keys, so we design key width according to the number of the first row the
        # horizontal gap between two keys, the gap before the first key and the gap after the last key.
        # In the first row, the three gap types are the same
        horizontal_key_gap = 8
        gap_two_sides = horizontal_key_gap
        key_width = int(
            (self.keyboard_width - gap_two_sides * 2 - horizontal_key_gap * (len(self.key_names[row]) - 1)) / len(
                self.key_names[row]))
        keyboard_upper_left_y = vertical_key_gap
        for k in range(len(self.key_names[row])):
            key = Key(self.key_names[row][k], key_width, key_height,
                      gap_two_sides + k * (key_width + horizontal_key_gap), keyboard_upper_left_y)
            self.keys.append(key)

        row += 1
        # the second row
        # there are only ten keys in the second row, so more spacing in front and at the end
        gap_two_sides = int((self.keyboard_width - (
                key_width * len(self.key_names[row]) + horizontal_key_gap * (len(self.key_names[row]) - 1))) / 2)
        for k in range(len(self.key_names[row])):
            key = Key(self.key_names[row][k], key_width, key_height,
                      gap_two_sides + k * (key_width + horizontal_key_gap),
                      keyboard_upper_left_y + key_height + vertical_key_gap)
            self.keys.append(key)

        row += 1
        # the third row
        # there are only ten keys in the third row, so larger size for the "Caps" key (1st key) and the "Backspace" key (10th key)
        for k in range(len(self.key_names[row])):
            if k == 0:  # the "Caps" key
                key = Key(self.key_names[row][k], gap_two_sides + key_width - horizontal_key_gap, key_height,
                          horizontal_key_gap + k * (key_width + horizontal_key_gap),
                          keyboard_upper_left_y + (key_height + vertical_key_gap) * 2)
            elif k == len(self.key_names[row]) - 1:  # the "Backspace" key
                key = Key(self.key_names[row][k], gap_two_sides + key_width - horizontal_key_gap, key_height,
                          gap_two_sides + k * (key_width + horizontal_key_gap),
                          keyboard_upper_left_y + (key_height + vertical_key_gap) * 2)
            else:
                key = Key(self.key_names[row][k], key_width, key_height,
                          gap_two_sides + k * (key_width + horizontal_key_gap),
                          keyboard_upper_left_y + (key_height + vertical_key_gap) * 2)

            self.keys.append(key)

        row += 1
        # the fourth row
        #  there are only three keys in the forth row, so larger size for the three keys
        for k in range(len(self.key_names[row])):
            if k == 0:  # '123' key
                key = Key(self.key_names[row][k], gap_two_sides + key_width * 2, key_height,
                          horizontal_key_gap, keyboard_upper_left_y + (key_height + vertical_key_gap) * 3)
            elif k == 2:  # 'Space' key
                key = Key(self.key_names[row][k], gap_two_sides + key_width * 2, key_height,
                          gap_two_sides + 7 * (key_width + horizontal_key_gap),
                          keyboard_upper_left_y + (key_height + vertical_key_gap) * 3)
            else:  # 'Return' key
                key = Key(self.key_names[row][k], key_width * 5 + horizontal_key_gap * 4, key_height,
                          gap_two_sides + 2 * (key_width + horizontal_key_gap),
                          keyboard_upper_left_y + (key_height + vertical_key_gap) * 3)

            self.keys.append(key)

        # paint the key in the canvas
        for k in self.keys:
            key_tag = self.canvas.create_rectangle(k.key_top_left_x, k.key_top_left_y,
                                                   k.key_top_left_x + k.key_width,
                                                   k.key_top_left_y + k.key_height, fill='light gray')

            self.canvas.create_text(k.key_top_left_x + int(k.key_width / 2),
                                    k.key_top_left_y + int(k.key_height / 2),
                                    text=k.key_name)  # font="Times 20 italic bold",
            k.key_tag = key_tag

    def key_press(self, event_x, event_y):
        for k in self.keys:
            if k.key_top_left_x <= event_x <= (k.key_top_left_x + k.key_width) and (
                    k.key_top_left_y) <= event_y <= (k.key_top_left_y + k.key_height):
                # self.canvas.itemconfig(k.key_tag, fill="dark slate gray")
                self.key_pressed = k.key_name

    def key_release(self, event_x, event_y):
        for k in self.keys:
            pass
            # self.canvas.itemconfig(k.key_tag, fill="light gray")

    def mouse_move_left_button_down(self, event_x, event_y):
        for k in self.keys:
            if k.key_top_left_x <= event_x <= (k.key_top_left_x + k.key_width) and (
                    k.key_top_left_y) <= event_y <= (k.key_top_left_y + k.key_height):
                pass
                # self.canvas.itemconfig(k.key_tag, fill="dark slate gray")
