from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Mainapp(App):
    def build(self):
        self.icon = "3976419.png"
        self.Operators = ["/","*","+","-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            background_color=[1, 1, 1, 1],
            foreground_color=[0, 0, 0, 1],
            multiline=False,
            font_size=55,
            halign="right",
            readonly=True
        )
        main_layout.add_widget(self.solution)

        buttons= [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","+"],
            [".","0","C","-"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, font_size=30,
                    background_color=[0.7,0.7,0.7,1],
                    pos_hint={"center_x":0.5, "center_y":0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text="=", font_size=30,
            background_color=[0.6,0.6,0.6,1],
            pos_hint={"center_x":0.5, "center_y":0.5},
        )
        equal_button.bind(on_press=self.on_solutions)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text.upper() == 'C':
            self.solution.text = ""
            self.last_was_operator = None
        else:
            if current and self.last_was_operator and button_text in self.Operators:
                return
            elif not current and button_text in self.Operators:
                return
            else:
                self.solution.text += button_text

        self.last_was_operator = button_text in self.Operators
        self.last_button = button_text

    def on_solutions(self, instance):
        text = self.solution.text
        if text:
            try:
                solution = str(eval(text))
                self.solution.text = solution
            except Exception:
                self.solution.text = "Error"

if __name__ == "__main__":
    app = Mainapp()
    app.run()
