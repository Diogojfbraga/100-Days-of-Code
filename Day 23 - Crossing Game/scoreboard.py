from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("BLACK")   # black text on black background was invisible
        self.penup()
        self.hideturtle()

        self.game_level = 1
        self.update_levelScore()

    def update_levelScore(self):
        self.clear()
        self.goto(-280, 260)
        self.write(
            f"Level: {self.game_level}",
            align="left",
            font=FONT
        )

    def level(self):
        self.clear()
        self.game_level += 1
        self.update_levelScore()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=("Courier", 36, "normal")
        )