# Pokédex API Application by KennyNeutron

This project is a GUI-based Pokédex application that uses **PyQt5** for the graphical interface and **PokéAPI** for retrieving Pokémon data. The application allows users to view Pokémon details, including their stats, abilities, types, height, and weight.

---

## Features

- **Pokémon Browsing:**
  - Navigate through Pokémon using **Next** and **Previous** buttons.
  - Search for Pokémon by name or ID.

- **Pokémon Details:**
  - Displays the Pokémon's image, ID, name, and types.
  - Shows base stats (HP, Attack, Defense, Special Attack, Special Defense, Speed) using color-coded progress bars.
  - Displays abilities, height, and weight.

- **Dynamic Interface:**
  - Type buttons and background gradients change dynamically based on the Pokémon's type(s).

- **Integrated with PokéAPI:**
  - Fetches real-time Pokémon data from the [PokéAPI](https://pokeapi.co/).

---

## Pokémon Base Stats

The application visualizes these base stats for each Pokémon:
- **HP (Hit Points)**: Represents the Pokémon's total health.
- **Attack**: Determines the power of physical moves.
- **Defense**: Reduces damage taken from physical moves.
- **Special Attack**: Determines the power of special moves.
- **Special Defense**: Reduces damage taken from special moves.
- **Speed**: Determines move order in battle.

### Stat Maximums
- **HP Maximum:** 700
- **Other Stat Maximums:** 460 (Attack, Defense, Special Attack, Special Defense, Speed)

---

## Prerequisites

### Python Libraries
Ensure the following libraries are installed:
- PyQt5
- Flask
- Requests

Install them using pip:
```bash
pip install pyqt5 flask requests
