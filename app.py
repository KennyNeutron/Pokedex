from flask import Flask, jsonify, request
import requests
from tkinter import Tk, Label, Entry, Button, Text

app = Flask(__name__)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2"

@app.route('/')
def home():
    return "Welcome to the Pokémon API app!"

@app.route('/pokemon/<name>')
def get_pokemon(name):
    response = requests.get(f"{POKEAPI_BASE_URL}/pokemon/{name.lower()}")
    
    if response.status_code == 200:
        data = response.json()
        pokemon_data = {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "base_stats": {
                "hp": data["stats"][0]["base_stat"],
                "attack": data["stats"][1]["base_stat"],
                "defense": data["stats"][2]["base_stat"],
                "special_attack": data["stats"][3]["base_stat"],
                "special_defense": data["stats"][4]["base_stat"],
                "speed": data["stats"][5]["base_stat"]
            },
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "types": [ptype["type"]["name"] for ptype in data["types"]]
        }
        return jsonify(pokemon_data)
    else:
        return jsonify({"error": "Pokémon not found"}), 404

def get_pokemon_data(name):
    response = requests.get(f"{POKEAPI_BASE_URL}/pokemon/{name.lower()}")
    
    if response.status_code == 200:
        data = response.json()
        pokemon_data = {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "base_stats": {
                "hp": data["stats"][0]["base_stat"],
                "attack": data["stats"][1]["base_stat"],
                "defense": data["stats"][2]["base_stat"],
                "special_attack": data["stats"][3]["base_stat"],
                "special_defense": data["stats"][4]["base_stat"],
                "speed": data["stats"][5]["base_stat"]
            },
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "types": [ptype["type"]["name"] for ptype in data["types"]]
        }
        return pokemon_data
    else:
        return {"error": "Pokémon not found"}

def search_pokemon():
    pokemon_name = entry.get()
    pokemon_data = get_pokemon_data(pokemon_name)
    if "error" in pokemon_data:
        result_text.delete(1.0, "end")
        result_text.insert("end", pokemon_data["error"])
    else:
        result_text.delete(1.0, "end")
        result_text.insert("end", f"ID: {pokemon_data['id']}\nName: {pokemon_data['name']}\nHeight: {pokemon_data['height']}\nWeight: {pokemon_data['weight']}\nBase Stats:\n  HP: {pokemon_data['base_stats']['hp']}\n  Attack: {pokemon_data['base_stats']['attack']}\n  Defense: {pokemon_data['base_stats']['defense']}\n  Special Attack: {pokemon_data['base_stats']['special_attack']}\n  Special Defense: {pokemon_data['base_stats']['special_defense']}\n  Speed: {pokemon_data['base_stats']['speed']}\nAbilities: {pokemon_data['abilities']}\nTypes: {pokemon_data['types']}")

def main():
    global entry, result_text
    root = Tk()
    root.title("Pokémon API")
    root.geometry("400x500")

    entry_label = Label(root, text="Enter the name of the Pokémon:")
    entry_label.pack(pady=10)

    entry = Entry(root, width=20)
    entry.pack(pady=10)

    search_button = Button(root, text="Search", command=search_pokemon)
    search_button.pack(pady=10)

    result_text = Text(root, width=40, height=20)
    result_text.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()