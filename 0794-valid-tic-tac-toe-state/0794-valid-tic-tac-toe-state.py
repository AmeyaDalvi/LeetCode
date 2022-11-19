class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        def checkWin(s):
            i=0
            while i<3:
                if board[i][0] == board[i][1] == board[i][2] == s: return True
                i+=1
            i=0
            while i<3:
                if board[0][i] == board[1][i] == board[2][i] == s: return True
                i+=1
            
            if board[0][0] == board[1][1] == board[2][2] == s: return True
            if board[0][2] == board[1][1] == board[2][0] == s: return True
            
            return False
            
        
        xCount = 0
        oCount = 0
        flag = False
        
        for string in board:
            xCount += string.count('X')
            oCount += string.count('O')
             
            
        if xCount < oCount or xCount-oCount >= 2:
            return False
        
        if xCount>=3:
            if xCount==oCount and checkWin('X'):
                return False
            if xCount!=oCount and checkWin('O'): 
                return False
        
        return True
        
        