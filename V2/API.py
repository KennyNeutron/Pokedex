from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v1"


@app.route("/")
def home():
    return "Welcome to the Pokémon API app!"


@app.route("/pokemon/<name>")
def get_pokemon(name):
    response = requests.get(f"{POKEAPI_BASE_URL}/pokemon/{name.lower()}")

    if response.status_code == 200:
        data = response.json()
        pokemon_data = {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "types": [ptype["type"]["name"] for ptype in data["types"]],
        }
        return jsonify(pokemon_data)
    else:
        return jsonify({"error": "Pokémon not found"}), 404


def get_pokemon_data(name):
    response = requests.get(f"{POKEAPI_BASE_URL}/pokemon/{name.lower()}")

    if response.status_code == 200:
        data = response.json()
        pokemon_data = {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "base_stats": {
                "hp": data["stats"][0]["base_stat"],
                "attack": data["stats"][1]["base_stat"],
                "defense": data["stats"][2]["base_stat"],
                "special_attack": data["stats"][3]["base_stat"],
                "special_defense": data["stats"][4]["base_stat"],
                "speed": data["stats"][5]["base_stat"],
            },
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "types": [ptype["type"]["name"] for ptype in data["types"]],
        }
        return pokemon_data
    else:
        return {"error": "Pokémon not found"}


def main():
    name = input("Enter the name of the Pokémon: ")
    pokemon_data = get_pokemon_data(name)
    print(pokemon_data)


if __name__ == "__main__":
    # app.run(debug=True)
    main()
