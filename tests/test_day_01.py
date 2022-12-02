
def test_find_elf_carrying_most_calories():
    inventories = read_inventories("data/puzzle")
    expedition = Expedition(inventories)
    expedition.the_elf_carrying_most_calories()
    with open(puzzle) as file:
        print(file.readlines())