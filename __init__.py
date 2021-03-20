from mycroft import MycroftSkill, intent_file_handler


class Exercicodia(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('exercicodia.intent')
    def handle_exercicodia(self, message):
        self.speak_dialog('exercicodia')


def create_skill():
    return Exercicodia()

