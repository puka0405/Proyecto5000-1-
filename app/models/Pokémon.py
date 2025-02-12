from app import mongo

class Pokemon:
    collection = mongo.db.pokemons

    @staticmethod
    def find_all():
        pokemons = Pokemon.collection.find()
        return list(pokemons)
    
    @staticmethod
    def find_by_id(pokemon_id):
        pokemon = Pokemon.collection.find.one({
            "_id": pokemon_id
        })
        return pokemon
    
    @staticmethod
    def create(data):
        pokemon = Pokemon.collection.insert_one(data)
        return pokemon.inserted_id
    
    @staticmethod
    def update(pokemon_id, data):
        pokemon = Pokemon.collection.update_one({
            "_id":pokemon_id
        },{
            "$set":data
        })
        return pokemon
    
    @staticmethod
    def delete(pokemon_id):
        return Pokemon.collection.delete_one({"_id":pokemon_id})
    
class User:
    collection = mongo.db.users

    @staticmethod
    def find_all():
        users = User.collection.find()
        return list(users)
    
    @staticmethod
    def find_by_id(user_id):
        user = User.collection.find_one({
            "_id": user_id
        })
        return user
    
    @staticmethod
    def create(data):
        user = User.collection.insert_one(data)
        return user.inserted_id
    
    @staticmethod
    def update(user_id, data):
        user = User.collection.update_one({
            "_id": user_id
        }, {
            "$set": data
        })
        return user
    
    @staticmethod
    def delete(user_id):
        return User.collection.delete_one({"_id": user_id})


class PokemonSaved:
    collection = mongo.db.pokemon_saved

    @staticmethod
    def find_all():
        pokemon_saved = PokemonSaved.collection.find()
        return list(pokemon_saved)
    
    @staticmethod
    def find_by_id(p_saved_id):
        pokemon_saved = PokemonSaved.collection.find_one({
            "_id": p_saved_id
        })
        return pokemon_saved
    
    @staticmethod
    def create(data):
        pokemon_saved = PokemonSaved.collection.insert_one(data)
        return pokemon_saved.inserted_id
    
    @staticmethod
    def update(p_saved_id, data):
        pokemon_saved = PokemonSaved.collection.update_one({
            "_id": p_saved_id
        }, {
            "$set": data
        })
        return pokemon_saved
    
    @staticmethod
    def delete(p_saved_id):
        return PokemonSaved.collection.delete_one({"_id": p_saved_id})