import time

class BattleOperator:

    def show_stats(self, player1, player2):
        for i in (player1, player2):
            print(f"{i} has {i.health} health and {i.energy} energy.")

    def duel(self, player1, player2):
        damage = player1.attack()
        print(f"{player1.nickname} attacks {player2.nickname} with {damage} damage.")
        player2.lost_hp(damage)
        if player1.energy < 10:
            given_energy = player1.energy_regen()
            print(f"{player1.nickname} gained {given_energy} energy.")
            player1.energy += given_energy


    def battle(self, player1, player2):

        round_count = 1
        while player1.is_alive() and player2.is_alive():
            print(f"Round nr. {round_count}. \n")
            self.show_stats(player1,player2)
            self.duel(player1,player2)
            round_count += 1
            print("\n")
            time.sleep(1)

            print(f"Round nr. {round_count}. \n")
            self.show_stats(player1, player2)
            self.duel(player2, player1)
            round_count += 1
            print("\n")
            time.sleep(1)

        if player1.is_alive():
            print(f"{player1.nickname} won.")
        else:
            print(f"{player2.nickname} won.")

        time.sleep(1.2)





# dodac klase aby w mainie nie bylo zadnych funkcji, zmienic rundy aby byly na zmiane