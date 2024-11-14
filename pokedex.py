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
        result_text.tag_config('bold', font=('Helvetica', 12, 'bold'))
        result_text.tag_config('data', font=('Arial', 11))
        result_text.tag_config('sub_bold', font=('Helvetica', 11, 'bold italic'))
        result_text.insert("end", "ID: ", 'bold')
        result_text.insert("end", f"{pokemon_data['id']}\n", 'data')
        result_text.insert("end", "Name: ", 'bold')
        result_text.insert("end", f"{pokemon_data['name']}\n", 'data')
        result_text.insert("end", "Height: ", 'bold')
        result_text.insert("end", f"{pokemon_data['height']}\n", 'data')
        result_text.insert("end", "Weight: ", 'bold')
        result_text.insert("end", f"{pokemon_data['weight']}\n", 'data')
        result_text.insert("end", "Base Stats:\n", 'bold')
        result_text.insert("end", "  ", 'data')
        result_text.insert("end", "HP: ", 'sub_bold')
        result_text.insert("end", f"{pokemon_data['base_stats']['hp']}\n", 'data')
        result_text.insert("end", "  ", 'data')
        result_text.insert("end", "Attack: ", 'sub_bold')
        result_text.insert("end", f"{pokemon_data['base_stats']['attack']}\n", 'data')
        result_text.insert("end", "  ", 'data')
        result_text.insert("end", "Defense: ", 'sub_bold')
        result_text.insert("end", f"{pokemon_data['base_stats']['defense']}\n", 'data')
        result_text.insert("end", "  ", 'data')
        result_text.insert("end", "Special Attack: ", 'sub_bold')
        result_text.insert("end", f"{pokemon_data['base_stats']['special_attack']}\n", 'data')
        result_text.insert("end", "  ", 'data')
        result_text.insert("end", "Special Defense: ", 'sub_bold')
        result_text.insert("end", f"{pokemon_data['base_stats']['special_defense']}\n", 'data')
        result_text.insert("end", "  ", 'data')
        result_text.insert("end", "Speed: ", 'sub_bold')
        result_text.insert("end", f"{pokemon_data['base_stats']['speed']}\n", 'data')
        result_text.insert("end", "Abilities: ", 'bold')
        result_text.insert("end", ", ".join(pokemon_data['abilities']) + "\n", 'data')
        result_text.insert("end", "Types: ", 'bold')
        result_text.insert("end", ", ".join(pokemon_data['types']), 'data')


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

    result_text = Text(root, width=40, height=15)
    result_text.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()