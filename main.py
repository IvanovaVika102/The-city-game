from cities import cities_list

class Cities():
    """Игра в города"""
    def __init__(self) -> None:
        self._cities_list_lower = []
        self._user1_name = None
        self._user1_score = 0
        self._user2_name = None
        self._user2_score = 0
        self._current_letter = None
        self._is_user1_first = True
        self._gameover = False
        self._winner_number = None

    def before(self):
        """Ввод данных игроков"""
        for city in cities_list:
            self._cities_list_lower.append(city.lower())
        self._user1_name = input("Имя первого игрока: ")
        self._user2_name = input("Имя первого игрока: ")
        choise = int(input(f"Кто делает первый ход? {self._user1_name} - нажмите 1, {self._user2_name} - нажмите 2: "))
        if choise == 2:
            self._is_user1_first = False

    def stop_game(self):
        """Подведение итогов игры"""
        if self._winner_number == 1:
            print(f"Игрок {self._user1_name} выиграл!")
        else:
            print(f"Игрок {self._user2_name} выиграл!")
        print(f"Счет {self._user1_name}: {self._user1_score} - {self._user2_name}: {self._user2_score}")

    def make_move(self, player_number: int) -> bool:
        """Сделать ход"""
        city = None
        curent_user = None
        if player_number == 1:
            curent_user = self._user1_name
        else:
            curent_user = self._user2_name

        if self._current_letter is None:
            city = input(f"{curent_user}, введите название любого города: ")
        else:
            city = input(f"{curent_user}, введите название любого города на букву '{self._current_letter}': ")

        if self.check_city(city):
            if city[-1].lower() in ('ь', 'ы', 'ъ'):
                self._current_letter = city[-2].lower()
            else:
                self._current_letter = city[-1].lower()
            return True
        return False

    def start_game(self):
        """Цикл игры"""
        if self._is_user1_first is False:
            result = self.make_move(2)
            if result:
                self._user2_score += 1
            else:
                self._gameover = True
                self._winner_number = 1

        while self._gameover is False:
            result = self.make_move(1)
            if result:
                self._user1_score += 1
            else:
                self._winner_number = 2
                break

            result = self.make_move(2)
            if result:
                self._user2_score += 1
            else:
                self._winner_number = 1
                break

    def check_city(self, city: str) -> bool:
        if city[0].lower() != self._current_letter and self._current_letter:
            print("Неверная буква!")
            return False
        if city.lower() in self._cities_list_lower:
            self._cities_list_lower.remove(city.lower())
            return True
        print("Такого города нет!")
        return False


def main():
    cities = Cities()
    cities.before()
    cities.start_game()
    cities.stop_game()

if __name__ == "__main__":
    main()
