class Checkers:
    def __init__(self, n):
        self.grid = [["#"] * n for _ in range(n)]
        self.n = n


    def intro(self):
        print("Welcome to my Checkers Game!")


    def populate_board(self):
        for i in range(self.n):
            for j in range(self.n):
                if i < 3 and (i+j) % 2 == 1:
                    self.grid[i][j] = "R"
                elif i > 4 and (i+j) % 2 == 1:
                    self.grid[i][j] = "B"
                else:
                    continue




    def in_bounds(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n


    def is_empty_cell(self, x, y):
        return self.grid[x][y] == "#"


    def is_one_move(self, diff_x, diff_y):
        if diff_x == -1 and abs(diff_y) == 1:
            return True
        if diff_x == 1  and abs(diff_y) == 1:
            return True
        return False


    def print_board(self):
        for row in self.grid:
            print(" ".join(row))
        print()


    def is_valid_move(self, start, end, current_player):
        start_x, start_y = start
        end_x, end_y = end
        diff_x, diff_y = end_x - start_x, end_y - start_y


       # check if it is inside the bounds
        if not self.in_bounds(end_x, end_y):
            return False
        if self.grid[start_x][start_y] != current_player:
            return False


        if not self.is_empty_cell(end_x, end_y):
            return False


       # check if the cell is empty, then if the difference is one then it is a normal move, check if it is (1, 1), (-1, -1), (-1, 1), (1, -1)
        if abs(diff_x) == 1 and self.is_one_move(diff_x, diff_y):
            if current_player == "B" and diff_x == -1 or (current_player == "R" and diff_x == 1):
                self.grid[start_x][start_y] = "#"
                self.grid[end_x][end_y] = current_player
                return True


       # check if the cell on in the way is not empty and check if it is a valid move
        if abs(diff_x) == 2 and self.is_one_move(diff_x//2, diff_y//2):
            mid_x, mid_y = start_x + diff_x // 2, start_y + diff_y // 2
            mid_piece = self.grid[mid_x][mid_y]


            if mid_piece != "#" and mid_piece.upper() != current_player:
                self.grid[start_x][start_y] = "#"
                self.grid[mid_x][mid_y] = "#"
                self.grid[end_x][end_y] = current_player
                return True


        return False


    def check_winner(self):
        blue, red = 0, 0


        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].upper() == "B":
                    blue += 1
                elif self.grid[i][j].upper() == "R":
                    red += 1
        return blue, red


    def play_game(self):
        self.populate_board()
        current_player = "B"
        while True:
            self.print_board()
            print(f"{current_player}: play please!")
            blue, red = self.check_winner()
            if not blue:
                print("Red Won!")
                break
            elif not red:
                print("Blue Won!")
                break




            start_x = int(input("Enter the piece you wanna move from (row): "))
            start_y = int(input("Enter the piece you wanna move from (column): "))
            end_x = int(input("Enter the piece you wanna move to (row): "))
            end_y = int(input("Enter the piece you wanna move to (column): "))


            if self.is_valid_move( (start_x, start_y), (end_x, end_y), current_player):
                current_player = "B" if current_player == "R" else "R"
                print(f"Good move, now {current_player}'s turn")
            else:
                print("Sorry, invalid move")




def main():
    play_again = "y"
    while play_again != "n":
        checkers = Checkers(8)
        checkers.intro()
        checkers.play_game()
        play_again = input("Play again? (y/n)")


if __name__ == "__main__":
    main()

