class Pokemon:
    pokemons = {}
    BASE_HEALTH = 100 
    BASE_ATTACK = 20

    def __init__(self, pokemon_trainer): 

        self.pokemon_trainer = pokemon_trainer

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.health = Pokemon.BASE_HEALTH 
        self.attack = Pokemon.BASE_ATTACK 

        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self):
        url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.pokemon_number}.png'
        try:
            response = requests.get(url)
           

         
            return url  
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при загрузке изображения: {e}")
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()
            return data['name']
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении имени: {e}")
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}, Здоровье: {self.health}, Атака: {self.attack}"

    def show_img(self):
        return self.img

    # Метод для атаки другого покемона
    def attack_pokemon(self, other_pokemon):
        damage = randint(self.attack // 2, self.attack) # Случайный урон в диапазоне от половины атаки до полной атаки
        other_pokemon.health -= damage
        print(f"{self.name} атакует {other_pokemon.name} и наносит {damage} урона!")
        if other_pokemon.health <= 0:
            print(f"{other_pokemon.name} повержен!")
        else:
            print(f"У {other_pokemon.name} осталось {other_pokemon.health} здоровья.")

    @classmethod
    def set_base_health(cls, new_health):
        Pokemon.BASE_HEALTH = new_health
        print(f"Базовое здоровье покемонов изменено на {new_health}")

    @classmethod
    def set_base_attack(cls, new_attack):
        Pokemon.BASE_ATTACK = new_attack
        print(f"Базовая атака покемонов изменена на {new_attack}")


