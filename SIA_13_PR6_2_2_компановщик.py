class Mediator():
    def __init__(self):
        self.play_button = None
        self.stop_button = None
        self.pause_button = None
        self.text_box = None

    def set_play_button(self, play_button):
        self.play_button = play_button

    def set_stop_button(self, stop_button):
        self.stop_button = stop_button

    def set_pause_button(self, pause_button):
        self.pause_button = pause_button

    def set_text_box(self, text_box):
        self.text_box = text_box

    def play(self):
        self.text_box.set_text("Playing...")

    def stop(self):
        self.text_box.set_text("Stoppped.")

    def pause(self):
        self.text_box.set_text("Paused.")

class Buttton():
    def __init__(self, mediator):
        self.mediator = mediator

    def click(self):
        pass

class TextBox():
    def __init__(self, mediator):
        self.text = ""
        self.mediator = mediator

    def set_text(self, text):
        self.text = text
        print(self.text)

class PlayButton(Buttton):
    def click(self):
        self.mediator.play()

class StopButton(Buttton):
    def click(self):
        self.mediator.stop()

class PauseButton(Buttton):
    def click(self):
        self.mediator.pause()

mediator = Mediator()

play_button = PlayButton(mediator)
stop_button = StopButton(mediator)
pause_button = PauseButton(mediator)
text_box = TextBox(mediator)

mediator.set_play_button(play_button)
mediator.set_stop_button(stop_button)
mediator.set_pause_button(pause_button)
mediator.set_text_box(text_box)

play_button.click()
pause_button.click()
stop_button.click()