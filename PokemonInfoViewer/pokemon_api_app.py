import requests
import json

BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{BASE_URL}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = {
            "Name": data['name'].capitalize(),
            "ID": data['id'],
            "Height": data['height'],
            "Weight": data['weight'],
            "Base Experience": data['base_experience'],
            "Types": [t['type']['name'].capitalize() for t in data['types']],
            "Abilities": [a['ability']['name'].capitalize() for a in data['abilities']]
        }
        return info
    else:
        return f"Error fetching data: {response.status_code}"

def get_pokemon_types():
    url = f"{BASE_URL}/type"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        types = [t['name'].capitalize() for t in data['results']]
        return types
    else:
        return f"Error fetching data: {response.status_code}"

def get_type_info(type_name):
    url = f"{BASE_URL}/type/{type_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = {
            "Name": data['name'].capitalize(),
            "Damage Relations": {
                "No Damage To": [t['name'].capitalize() for t in data['damage_relations']['no_damage_to']],
                "Half Damage To": [t['name'].capitalize() for t in data['damage_relations']['half_damage_to']],
                "Double Damage To": [t['name'].capitalize() for t in data['damage_relations']['double_damage_to']],
                "No Damage From": [t['name'].capitalize() for t in data['damage_relations']['no_damage_from']],
                "Half Damage From": [t['name'].capitalize() for t in data['damage_relations']['half_damage_from']],
                "Double Damage From": [t['name'].capitalize() for t in data['damage_relations']['double_damage_from']]
            },
            "Pokemon": [p['pokemon']['name'].capitalize() for p in data['pokemon']]
        }
        return info
    else:
        return f"Error fetching data: {response.status_code}"

def get_pokemon_abilities():
    url = f"{BASE_URL}/ability"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        abilities = [a['name'].capitalize() for a in data['results']]
        return abilities
    else:
        return f"Error fetching data: {response.status_code}"

def get_ability_info(ability_name):
    url = f"{BASE_URL}/ability/{ability_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = {
            "Name": data['name'].capitalize(),
            "Effect": data['effect_entries'][0]['effect'],
            "Pokemon": [p['pokemon']['name'].capitalize() for p in data['pokemon']]
        }
        return info
    else:
        return f"Error fetching data: {response.status_code}"

def main():
    while True:
        print("\nOptions:")
        print("1. Get Pokemon Info")
        print("2. Get Pokemon Types")
        print("3. Get Pokemon Type Info")
        print("4. Get Pokemon Abilities")
        print("5. Get Pokemon Ability Info")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the Pokemon name: ").lower()
            info = get_pokemon_info(name)
            print(json.dumps(info, indent=4))

        elif choice == '2':
            types = get_pokemon_types()
            print(json.dumps(types, indent=4))

        elif choice == '3':
            type_name = input("Enter the Pokemon type name: ").lower()
            info = get_type_info(type_name)
            print(json.dumps(info, indent=4))

        elif choice == '4':
            abilities = get_pokemon_abilities()
            print(json.dumps(abilities, indent=4))

        elif choice == '5':
            ability_name = input("Enter the Pokemon ability name: ").lower()
            info = get_ability_info(ability_name)
            print(json.dumps(info, indent=4))

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
