# SpaceShooter Game

A 2D survival arcade game built using Python and the Pygame library. The player controls an aircraft navigating through space, avoiding hazards and collecting power-ups to prolong survival.

# Gameplay Mechanics

The core objective is survival. The game utilizes a basic collision detection system against incoming horizontal entities. The player starts with 5 lives. The game terminates when the life count reaches zero.

- Enemy Ships: Collision results in -1 life.

- Meteors: Collision results in -1 life.

- Shields: Collision grants +1 life.

# Controls

- W - Move Up

- S - Move Down

- A - Move Left

- D - Move Right

- ESC - Exit Game

# Prerequisites and Installation

Ensure you have Python 3.x installed on your system.

1. Download the source code.

2. Verify that all graphical assets (.png, .jpg) are located in the same root directory as main.py.

3. Install the required dependency:

`pip install pygame`


4. Execute the main script to launch the application:

`python main.py`


