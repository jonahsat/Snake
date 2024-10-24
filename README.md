# Python Snake Game

A classic Snake game implementation with a modern twist, built using Python and Pygame. This version features both traditional boundary-limited gameplay and an infinite wrap-around mode.

## Features

- Two distinct game modes:
  - Classic Mode (with boundaries)
  - Infinite Mode (wrap-around edges)
- Clean, grid-based gameplay
- Visual boundary indicators
- Score tracking in header bar
- Game over screen with multiple options
- Minimalist retro-style graphics

## Prerequisites

- Python 3.x
- Pygame library

## Installation

1. Clone this repository
2. Install Pygame by running `pip install pygame`
3. Run the game with `python game.py`

## How to Play

### Controls
- Arrow keys: Control snake direction
- Space: Restart game (after game over)
- Enter: Return to title screen (after game over)
- ESC: Quit game

### Game Modes
1. **Classic Mode (With Boundaries)**
   - Snake dies upon hitting walls
   - Visual boundaries shown
   - Traditional snake gameplay

2. **Infinite Mode (Without Boundaries)**
   - Snake wraps around screen edges
   - No boundaries
   - Continuous gameplay

### Scoring
- Each food item eaten increases score by 1
- Snake grows longer with each food item
- Game ends if snake collides with itself
- Current score displayed in header

## Game Structure

The game is built with several key components:
- Snake class: Handles snake movement and growth
- Food class: Manages food spawning
- Grid system: 20x20 pixel blocks
- Header bar: Displays current score
- Multiple game states: Title screen, gameplay, and game over screen

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with Pygame
- Inspired by the classic Snake game