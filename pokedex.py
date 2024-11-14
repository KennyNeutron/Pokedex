from ast import main
from flask import Flask, jsonify, request
import requests
import tkinter as tk
from tkinter import font, PhotoImage
from PIL import Image, ImageTk

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

root = tk.Tk()
root.title("Pokédex using PokéAPI by KennyNeutron")
root.geometry("400x650")
pokemon_id = tk.IntVar()
poke_name = tk.StringVar()

icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)

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
        #result_text.insert("end", "ID: ", 'bold')
        #result_text.insert("end", f"{pokemon_data['id']}\n", 'data')
        #result_text.insert("end", "Name: ", 'bold')
        #result_text.insert("end", f"{pokemon_data['name']}\n", 'data')
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
        result_text.insert("end", "Type(s): ", 'bold')
        result_text.insert("end", ", ".join(pokemon_data['types']), 'data')
        pokemon_id.set(pokemon_data['id'])
        print("pokename:" + pokemon_data['name'])
        poke_name.set(pokemon_data['name'].capitalize())
        update_image()
        update_name()


def update_image():
    formatted_count = "{:03d}".format(pokemon_id.get())
    print(f'count: {formatted_count}')
    img_path = f'thumbnails/{formatted_count}.png'
    print(f'image name: {img_path}')
    image = Image.open(img_path)
    photo = ImageTk.PhotoImage(image)
    poke_img_label.config(image=photo)
    poke_img_label.image = photo  # Keep a reference to the image

def update_name():
    print("flag")
    formatted_id = "{:03d}".format(pokemon_id.get())
    display_name = f'{formatted_id} - {poke_name.get()}'
    print(f'pokemon name: {display_name}')
    entry_name.config(text=display_name)

global entry, result_text

label_font = font.Font(family="Arial", size=12, weight="bold")
entry_label = tk.Label(root, text="Enter the name of the Pokémon:")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=search_pokemon)
search_button.pack(pady=30)

poke_img_label = tk.Label(root)
poke_img_label.pack(pady=5)

name_font = font.Font(family="Helvetica", size=24, weight="bold")
entry_name = tk.Label(root, font=name_font)
entry_name.pack(pady=3)

result_text = tk.Text(root, width=45, height=13)
result_text.pack(pady=10)

root.mainloop()

if __name__ == "__main__":
    main()