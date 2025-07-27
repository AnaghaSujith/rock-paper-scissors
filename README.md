# rock-paper-scissors
A fun two-player **Rock-Paper-Scissors** game built using **Python Tkinter** for the GUI and **PIL (Pillow)** for image handling. The game provides a dynamic interface where each player's selection updates the canvas with corresponding images, and the winner is displayed in real-time.

##  Features

-  Two-player gameplay with individual choice buttons.
-  Real-time image updates based on player selections.
-  Game logic for determining winners, draws, and displaying results.
-  GUI built using Tkinter with support for image assets via Pillow.

---

##  Preview

<img width="913" height="152" alt="image" src="https://github.com/user-attachments/assets/6973aa69-acae-4c8d-9fd9-32a343964013" />
<img width="1195" height="1064" alt="image" src="https://github.com/user-attachments/assets/e44766e0-277f-4eaa-9f96-703b293cd51d" />


---

##  Getting Started

###  Prerequisites

Make sure Python and the Pillow library are installed:

```bash
pip install pillow
```

###  Project Structure
```bash
rock-paper-scissors-gui/
├── rock_paper_scissors_gui.py         # Main game script
├──assets
  ├── default.jpg                        # Default image for player panels
  ├── rock.jpg                           # Rock choice image
  ├── paper.jpg                          # Paper choice image
  ├── scissors.jpg                       # Scissor choice image
  ├── bigger+logo.jpg                    # Decorative banner/logo image
└── README.md                          # This file
```
### Run the Game
Use the following command to start the game:
```bash
python rock_paper_scissors_gui.py
```
