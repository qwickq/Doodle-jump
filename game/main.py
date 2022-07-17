from arcade import Sprite, SpriteList, Window, color, run, set_background_color


class MyWindow(Window):
    """Главное окно в игре"""
    def __init__(self, background: tuple[int, int, int] = color.PURPLE_NAVY):
        """Конструктор для создания обычного окна"""
        super().__init__(fullscreen=False)

        self.hero: Sprite = ...
        self.players: SpriteList = ...

        set_background_color(background)

    def setup(self):
        """Загружает и создает все необходимые объекты для игры/уровня/режима"""
        self.hero = Sprite("assets/main_hero.png", 1.5)

        self.players = SpriteList()
        self.players.append(self.hero)

    def on_draw(self):
        """Прорисовка всех объектов и структур на экране"""
        self.clear()
        self.players.draw()


def game(window: MyWindow = MyWindow()):
    """Запускает игру"""
    window.setup()
    run()


if __name__ == "__main__":
    game()
