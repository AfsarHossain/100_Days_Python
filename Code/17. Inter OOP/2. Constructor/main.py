class User:

    def __init__(self, userid, name):
        self.id = userid
        self.name = name


user1 = User(1, "Afsar")
user2 = User(2, "Tarek")

print(f"{user1.id}: {user1.name}.")
print(f"{user2.id}: {user2.name}.")
