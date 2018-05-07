class GameManager:
    toys = []

    def __init__(self):
        pass

    def sort_by_age(self):
        self.toys.sort(key=lambda toy: toy.age)

    def find_by_group(self, size, age, toy_type):
        founded_toys = []

        for toy in self.toys:
            if toy.age == age or toy.size == size or toy.toy_type == toy_type:
                founded_toys.append(toy)

        return founded_toys

    def add_toy(self, toy):
        self.toys += toy

    def print_list(self):
        for toy in self.toys:
            print(toy)
        print()
