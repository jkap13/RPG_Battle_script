from classes.game import bcolors, Person


magic= [{"name": "Fire", "cost": 10, "damage": 100},
        {"name": "Thunder", "cost": 10, "damage": 124},
        {"name": "Water", "cost": 10, "damage": 120},
        {"name": "Land", "cost": 10, "damage": 100},
        {"name": "Wind", "cost": 10, "damage": 107}]
player = Person(500, 100, 50, 25, magic)
enemy = Person(1000,65,45,25,magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
        print("=====================")
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
                dmg = player.generate_dmg()
                enemy.take_dmg(dmg)
                print("You attacked for", dmg, "points of damage.")
        elif index == 1:
                player.choose_magic()
                magic_choice = int(input("Choose Magic:")) - 1
                magic_dmg = player.generate_spell_dmg(magic_choice)
                spell = player.get_spell_name(magic_choice)
                cost = player.get_spell_mp_cost(magic_choice)

                current_mp = player.get_mp()
                if cost > current_mp:
                        print(bcolors.FAIL + "\n Not enough MP\n" + bcolors.ENDC)
                        continue

                player.reduce_mp(cost)
                enemy.take_dmg(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        enemy_choice = 1
        enemy_dmg = enemy.generate_dmg()
        player.take_dmg(enemy_dmg)
        print("Enemy attack for", enemy_dmg, "points of damage.")

        print("*****************************")
        print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp) + "/" + str(enemy.max_hp()) + bcolors.ENDC + "\n")
        print("Your HP:", bcolors.FAIL + str(player.get_hp) + "/" + str(player.max_hp()) + bcolors.ENDC + "\n")

        if enemy.get_hp() == 0:
                print(bcolors.OKGREEN + "You have won the Battle!" + bcolors.ENDC)
                running = False
        elif player.get_hp() == 0:
                print(bcolors.FAIL + "You have lost the Battle!" + bcolors.ENDC)
                running = False



