from arcade import Window
from arcade import run


class MyWindow(Window):
    """Главное окно в игре"""
    def __init__(self):
        """Конструктор для создания обычного окна"""
        super().__init__(fullscreen=False)


def game(window: MyWindow = MyWindow()):
    """Запускает игру"""
    run()


if __name__ == "__main__":
    game()
