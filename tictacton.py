import re

class TicTacTon:
    def __init__(self):

        self.board = ["１","２","３",
                      "４","５","６",
                      "７","８","９"]
        self.turn = 0
        self.winFlag = False
        self.play()
    

    def play(self):

        while True:
            print("".join(self.board[:3]) + "\n" + "".join(self.board[3:6])  + "\n" + "".join(self.board[6:]))

            try:
                self.put = int(input()) - 1

                if bool(re.fullmatch(r'([0-9]{1})', str(self.put))) != True: 
                    print("入力可能な数字を入力してください")
                    continue

                if self.board[self.put] == "〇" or self.board[self.put] == "×":
                    print("そこには置けません")
                    continue

            except ValueError:
                print("数字で入力してください")
                continue

            if self.turn % 2 == 0:
                self.board[self.put] = "〇"
            else:
                self.board[self.put] = "×"

            self.check()

            if self.winFlag == True:
                print(f"Player {self.turn%2+1} WIN!")
                break

            if self.turn == 8:
                print("".join(self.board[:3]) + "\n" + "".join(self.board[3:6])  + "\n" + "".join(self.board[6:]))
                print("DRAW")
                break

            self.turn += 1


    def check(self):

        if self.turn % 2 == 0:
            self.mark = "〇"
        else:
            self.mark = "×"

        self.checkboard = ["-"] * 16 + self.board[:3] + ["-"] * 4 + self.board[3:6] + ["-"] * 4 + self.board[6:] + ["-"] * 16
        self.checkNo = 16 + 7 * (self.put // 3) + self.put % 3

        if ( self.checkboard[self.checkNo-2:self.checkNo+3].count(self.mark)     == 3 or  # 横に並んでいるかを確認
             self.checkboard[self.checkNo-14:self.checkNo+22:7].count(self.mark) == 3 or  # 縦に並んでいるかを確認
             self.checkboard[self.checkNo-16:self.checkNo+25:8].count(self.mark) == 3 or  # 左斜めに並んでいるかを確認
             self.checkboard[self.checkNo-12:self.checkNo+19:6].count(self.mark) == 3 ) : # 右斜めに並んでいるかを確認
            
            self.winFlag = True


if __name__ == "__main__":
    TicTacTon()