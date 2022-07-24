from arcade import (
    PhysicsEnginePlatformer,
    Sprite,
    SpriteList,
    Window,
    color,
    key,
    run,
    set_background_color,
    close_window,
)


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
        self.hero = Sprite("assets/main_hero.png", 1)
        self.hero.center_x = 100
        self.hero.center_y = 100

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
