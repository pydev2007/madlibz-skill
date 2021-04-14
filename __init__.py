from mycroft import MycroftSkill, intent_file_handler


class Madlibz(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('madlibz.intent')
    def handle_madlibz(self, message):
        self.speak_dialog('madlibz')


def create_skill():
    return Madlibz()

