class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


class Template(list):
    def __init__(self, name, points):
        self.name = name
        super(Template, self).__init__(points)
#In Python 3, the super(Template, self) call is equivalent to the parameterless super() call.
#The first parameter refers to the subclass Template, while the second parameter refers to a Template object which, in this case, is self.

class WordTemplates:
    def __init__(self, keys_info):
        self.keys_info = keys_info

        self.word_list = ['it', 'we', 'he', 'on',
                          'the', 'but', 'his', 'are',
                          'copy', 'redo', 'undo', 'save',  # text editing commands
                          'people', 'before', 'during', 'number',
                          'problem', 'example', 'company', 'country',
                          'absolutely', 'dealership', 'noteworthy', 'surprising',
                          'information', 'development', 'outstanding', 'personality']
                          
        self.templates = []

    def set_templates(self):
        for w in self.word_list:
            points = []
            for c in w:
                for k in self.keys_info:
                    if c.lower() == k.key_name.lower():  # uppercase and lowercase characters are equally treated
                        # the centre point of the key
                        points.append(Point(int(k.key_top_left_x+k.key_width/2), int(k.key_top_left_y+k.key_height/2)))
            self.templates.append(Template(w, points))
        return self.templates


