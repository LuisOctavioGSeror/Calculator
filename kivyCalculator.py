import kivy
import numpy
kivy.require('1.11.0')
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

operation = []
listToStr = ""
start = True

class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        entry = TextInput(text = ("0"),readonly = True, font_size=72, halign='right', foreground_color=(1, 1, 1, 0.9), background_color=(0, 0, 0, 0.1), size_hint=(1, .4), pos_hint={'center_x': .5,'center_y': .8}) # foreground_color 0, 1, 0.6, 0.75 its also beautiful


        def color_black(instance):

            instance.background_color = (0, 0, 0, 1)

        def color_gray(instance):

            instance.background_color = (20, 20, 20, 0.05)

        def main_function(instance):
            print('The button <%s> is being pressed' % instance.text)

            instance.background_color = (0, 2, 1, 0.5)

            global start #pois e... bizarro...

            if(start):
                entry.text = ""
                start = False

            entry.text += instance.text

            if(instance.text != "=" and instance.text != "C"):
                operation.append(instance.text)
                listToStr = ''.join([str(elem) for elem in operation])

            elif(instance.text == "="):
                listToStr = ''.join([str(elem) for elem in operation])
                print ("Operation = " + listToStr)
                answer = eval(listToStr)
                print ("Answer = " + str(answer))
                entry.text = ""
                entry.text += str(answer)
                operation.clear()
                operation.append(str(answer))

            elif(instance.text == "C"):
                entry.text = "0"
                operation.clear()
                start = True


        def number_button(n, x, y):

            btn = Button(text = n, font_size = 32, color = (1, 1, 1, 0.75), background_color = (0, 0, 0, 1), on_press=main_function, on_release=color_black, size_hint = (.25, .15), pos_hint={'center_x': x, 'center_y': y})

            return btn

        def operation_button(n, x, y):

            btn = Button(text = n, color = (1, 1, 1, 0.5), font_size = 32, background_color = (20, 20, 20, 0.05), on_press = main_function, on_release = color_gray, size_hint = (0.125, 0.15), pos_hint = {'center_x': x, 'center_y': y})

            return btn

        def special_button(n, x, y):

            btn = Button(text = n, font_size = 32, background_color = (0, 2, 1, 0.5), on_press=main_function, size_hint=(.25, .15), pos_hint={'center_x': x, 'center_y': y})

            return btn


        self.add_widget(operation_button('.', 0.0625, 0.075))

        self.add_widget(operation_button(')', 0.0625, 0.225))

        self.add_widget(operation_button('(', 0.0625, 0.375))

        self.add_widget(operation_button('**', 0.0625, 0.525))

        self.add_widget(special_button('C', 0.25, 0.075))

        self.add_widget(number_button('0', 0.5, 0.075))

        self.add_widget(special_button('=', 0.75, 0.075))

        self.add_widget(operation_button('+', 0.9375, 0.075))

        self.add_widget(number_button('1', 0.25, 0.225))

        self.add_widget(number_button('2', 0.5, 0.225))

        self.add_widget(number_button('3', 0.75, 0.225))

        self.add_widget(operation_button('-', 0.9375, 0.225))

        self.add_widget(number_button('4', 0.25, 0.375))

        self.add_widget(number_button('5', 0.5, 0.375))

        self.add_widget(number_button('6', 0.75, 0.375))

        self.add_widget(operation_button('*', 0.9375, 0.375))

        self.add_widget(number_button('7', 0.25, 0.525))

        self.add_widget(number_button('8', 0.5, 0.525))

        self.add_widget(number_button('9', 0.75, 0.525))

        self.add_widget(operation_button('/', 0.9375, 0.525))

        self.add_widget(entry)

''' tentativa de reduzir o codigo
        number_array=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        counter = 0
        for y in numpy.arange(0.225, 0.525, 0.15):
            for x in numpy.arange(0.25, 0.75, 0.25):
                self.add_widget(number_button(number_array[counter], x, y))
                counter = counter + 1

        self.add_widget(number_button('0', 0.5, 0.075))

        counter = 0
        operation_array = ['.', ')', '(', '**', '+', '-', '*', '/']
        for y in numpy.arange(0.0625, 0.9375, 0.875):
            for x in numpy.arange(0.075, 0.525, 0.15):
                self.add_widget(operation_button(operation_array[counter], y, x))
                counter = counter + 1

        self.add_widget(special_button('C', 0.25, 0.075))
        self.add_widget(special_button('=', 0.75, 0.075))
        self.add_widget(entry)
'''
class CalculatorApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        with root.canvas.before:  #64 101 60 0.6
            Color(20, 20, 20, 0.1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    CalculatorApp().run()


