"""CP1404/CP5632 Practical"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initialise a Language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """To check language type is dynamic or not"""
        if self.typing == "Dynamic":
            return True


def __str__(self):
    """Return to the details of the output"""
    return "{}, {} Typing, Reflection={}, First appeared in {}".format(
        self.name, self.typing, self.reflection, self.year)
