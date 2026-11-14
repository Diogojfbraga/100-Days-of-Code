from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.color("white")
        self.penup()
        self.hideturtle()

        # Position scoreboard at the top
        self.goto(0, 350)

        self.update_scoreboard()

    ## Display the current score
    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            align="center",
            font=("Arial", 18, "normal")
        )

    ## Add points when a block is destroyed
    def add_score(self):
        self.score += 1
        self.update_scoreboard()