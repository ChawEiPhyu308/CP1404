"""CP1404/CP5632 Practical- Store three programming language types in array
                            Show All Languages  with full details
                            Show with filter in dynamically typed languages"""

from Prac_6.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    list_of_languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are: ")
    for language in list_of_languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == '_main___':
    main()

