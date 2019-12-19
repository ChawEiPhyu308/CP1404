"""CP1404/CP5632 Practical"""


class ProgrammingLanguage:
    """Initialise a Language instance"""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    """To check language type is dynamic or not"""
    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True

    """Modifications"""
    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year)
