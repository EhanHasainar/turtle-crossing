# 🐢 Turtle Crossing Game

A simple arcade-style game built with Python's `turtle` module. Help the turtle cross a busy road without getting hit by cars! With each successful crossing, the game gets more challenging.

---

## 🎮 Features

- **🚗 Random Car Generation**: Cars of different colors and random vertical positions move across the screen.
- **⬆️ Level Progression**: The game includes 3 levels, with car speeds increasing after each level.
- **💥 Collision Detection**: The game ends if the turtle collides with any car.
- **🛑 Game Over Screen**: Displays "GAME OVER" when the player loses or completes all levels.

---

## 🕹️ How to Play

1. Press the `W` key to move the turtle forward.
2. Avoid the cars moving from right to left.
3. Reach the top of the screen to advance to the next level.
4. Complete all 3 levels or avoid crashing for as long as possible.

---

## 📁 Project Structure

```
turtle-crossing-game/
├── main.py           # Main game logic and loop
├── player.py         # Player class for turtle movement
├── car_manager.py    # CarManager class for handling car behavior
├── scoreboard.py     # Scoreboard class for level and game over display
```

---

## 📄 File Descriptions

- **`main.py`**: Initializes the game and handles:
  - Creating and moving cars
  - Detecting collisions
  - Progressing levels
  - Ending the game

- **`player.py`**: Defines the `Player` class (the turtle). Handles movement and reset upon level-up.

- **`car_manager.py`**: Defines the `CarManager` class to:
  - Create cars randomly
  - Move cars across the screen
  - Increase speed as levels increase

- **`scoreboard.py`**: Defines the `Scoreboard` class to:
  - Track and display the current level
  - Show "GAME OVER" message when needed

---

## 📦 Requirements

- Python 3.x
- `turtle` module (comes pre-installed with Python)

---

## ▶️ How to Run

1. Clone or download the repository.
2. Make sure all files (`main.py`, `player.py`, `car_manager.py`, `scoreboard.py`) are in the same directory.
3. Run the game using:
   ```bash
   main.py
   ```

---

## 🧠 Game Flow

- The turtle starts at the bottom of the screen.
- Cars are randomly generated and move leftward.
- The player must avoid cars and reach the top to level up.
- Game ends if:
  - The turtle collides with a car
  - The player successfully completes **3 levels**

---

## 🛠️ Customization

- **Number of Levels**: Change the `if scoreboard.level > 3` condition in `main.py`.
- **Car Speed**: Adjust `STARTING_MOVE_DISTANCE` and `MOVE_INCREMENT` in `car_manager.py`.
- **Collision Sensitivity**: Modify the distance condition (`if car.distance(player) < 20`) in `main.py`.

---

## 🖼️ Example Gameplay

- The turtle moves up with each `W` key press.
- Cars zoom past horizontally.
- The level and challenge increase as the turtle reaches the top.
- If the turtle touches a car, it’s game over!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

This project is a great beginner-friendly exercise in using Python’s `turtle` module and learning basic game development and object-oriented programming concepts.

Happy crossing! 🚦
