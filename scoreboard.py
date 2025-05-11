from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Start at level 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)  # Position the scoreboard at the top-left corner
        self.update_scoreboard()

    def update_scoreboard(self):
        """Display the current level on the screen."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level and update the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display 'Game Over' when the player loses."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

