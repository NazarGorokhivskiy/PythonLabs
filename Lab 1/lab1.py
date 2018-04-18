class Computer:
    totalAmount = 0

    def __init__(self, name="default", price=0, amount=0, quality="default", color="default"):
        self.name = name
        self.price = price
        self.amount = amount
        self.quality = quality
        self.color = color
        Computer.totalAmount += amount

    def to_string(self):
        print("Name: " + self.name + "; Price:", self.price,
              "; Amount:", self.amount, "; Quality:" + self.quality + "; Color:", self.color, ";")

    def print_sum(self):
        print("Кількість " + self.name + ": ", self.amount)

    @staticmethod
    def print_static_sum():
        print("Загальна кількість: ", Computer.totalAmount)


if __name__ == '__main__':
    dell = Computer("Dell Inspiron", 42, 400, "bullshit", "Toilet paper")
    macbook = Computer()
    xiaomi = Computer("Apple Macbook 13", 47, 1088, "awesome")
    
    print("\n")
    dell.to_string()
    macbook.to_string()
    xiaomi.to_string()
    
    print("\n")
    dell.print_sum()
    macbook.print_sum()
    xiaomi.print_sum()
    
    print("\n")
    Computer.print_static_sum()