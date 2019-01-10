from random import randint
class chess:
    def __init__(self, importb):
        self.board = importb

    def printrawboard(self):
        print self.board

        return 0


    def printboard(self):
        for i in range(63,-1,-1):
            if self.board[i] == 0:
                print " " + str(self.board[i]),
            else: print self.board[i],
            if (i == 8 or i == 16 or i == 24 or i == 32 or i == 40 or i == 48 or i == 56 or i == 0):
                print 


    def GPP(self, player):#get player positions
        if player != 10 and player != 20:
            return -1
        retlist = []
        if player == 10:
            for i in range(0,64):
                if self.board[i] > 9 and self.board[i] < 20:
                    retlist = retlist + [i]
        else:
            for i in range(0,64):
                if self.board[i] > 19 and self.board[i] < 30:
                    retlist = retlist + [i]

        return retlist

    def GPLM(self, BW, position):#legal moves
        retpos = []
        current = position

        if BW == 10:
            if(self.board[current] == 10):
                retpos = self.pawn(10, current)
                return retpos
            elif(self.board[current] == 13):
                retpos = self.rook(10, current)
                return retpos
            elif(self.board[current] == 12):
                retpos = self.bishop(10, current)
                return retpos
            elif(self.board[current] == 11):
                retpos = self.knight(10, current)
                return retpos
            elif(self.board[current] == 14):
                retpos = self.queen(10, current)
                return retpos
            elif(self.board[current] == 15):
                retpos = self.king(10, current)
                return retpos
            else:
                retpos = []

        
        if BW == 20:
            if(self.board[current] == 20):
                retpos = self.pawn(20, current)
                return retpos
            elif(self.board[current] == 23):
                retpos = self.rook(20, current)
                return retpos
            elif(self.board[current] == 22):
                retpos = self.bishop(20, current)
                return retpos
            elif(self.board[current] == 21):
                retpos = self.knight(20, current)
                return retpos
            elif(self.board[current] == 24):
                retpos = self.queen(20, current)
                return retpos
            elif(self.board[current] == 25):
                retpos = self.king(20, current)
                return retpos
            else:
                retpos = []
        
        return retpos
    def APM(self, BW):

        pos = []
        for i in range(0, 64):
            pos = pos + self.GPLM(BW, i)
        return pos
       
    def pawn(self, BW, position):#should add diagonal movement
        retpos = []
        
        temp = position
        curr = position
        value = 1
        if BW == 10:#white
            if  (temp + 8) < 64 and self.board[temp + 8] == 0:
                temp = temp + 8
                retpos = retpos + [[[curr, temp], self.Threat(BW, temp)]]

            temp = position
            if temp + 9 < 64 and temp + 9 != 16 and temp + 9 != 24 and temp + 9 != 32 and temp + 9 != 40 and temp + 9 != 48 and temp + 9 != 56:
                if self.board[temp + 9] > 16:
                    retpos = retpos + [[[curr, temp + 9], ((self.board[temp + 9]%10)*(self.board[temp + 9]%10) + 1) + value*self.Threat(BW, temp + 9)]]

            temp = position
            if temp + 7 < 64 and temp + 7 != 7 and temp + 7 != 15 and temp + 7 != 23 and temp + 7 != 31 and temp + 7 != 39 and temp + 7 != 47 and temp + 7 != 55:

                if self.board[temp + 7] > 16:
                    retpos = retpos + [[[curr, temp + 7], ((self.board[temp + 7]%10)*(self.board[temp + 7]%10) + 1) + value*self.Threat(BW, temp + 7)]]


        else:#black
            if  (temp - 8) > 0 and self.board[temp - 8] == 0:
                temp = temp - 8
                retpos = retpos + [[[curr, temp], self.Threat(BW, temp)]]

            temp = position
            if temp - 9 > -1 and temp - 9 != 7 and temp - 9 != 15 and temp - 9 != 23 and temp - 9 != 31 and temp - 9 != 39 and temp - 9 != 47 and temp - 9 != 55:
                if self.board[temp - 9] < 16 and self.board[temp -9] > 0:
                    retpos = retpos + [[[curr, temp - 9], ((self.board[temp - 9]%10)*(self.board[temp - 9]%10) + 1) + value*self.Threat(BW, temp - 9)]]

            temp = position
            if temp - 7 > -1 and temp - 7 != 8 and temp - 7 != 16 and temp - 7 != 24 and temp - 7 != 32 and temp - 7 != 40 and temp - 7 != 48 and temp - 7 != 0:

                if self.board[temp - 7] < 16 and self.board[temp -7] > 0:
                    retpos = retpos + [[[curr, temp - 7], ((self.board[temp - 7]%10)*(self.board[temp - 7]%10) + 1) + value*self.Threat(BW, temp - 7)]]




        return retpos
    def rook(self, BW, position):
        value = 4
        retpos = []
        current = position
        curr = position
        i = 1
        if current + i < 64:
            while self.board[current + i] == 0:#horizontal -> right

                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 56:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]
                if current + i + 1 < 64:
                    if self.board[current+i+1] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+i+1], ((self.board[current + i + 1]%10)*(self.board[current + i + 1]%10) + 1) + value*self.Threat(BW, current + i + 1)]]
                    if self.board[current+i+1] < 19 and self.board[current + i + 1] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+i+1], ((self.board[current + i + 1]%10)*(self.board[current + i + 1]%10) + 1) + value*self.Threat(BW, current + i + 1)]]
                current = current + 1
                if current + 1> 63: break

        current = position
        i = -1
        if current + i > -1:
            while self.board[current + i] == 0:#horizontal -> left

                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

                if self.board[current + i-1] > 19 and BW == 10 and current + i - 1 > -1:
                    retpos = retpos + [[[curr, current+i-1], ((self.board[current + i - 1]%10)*(self.board[current + i - 1]%10) - 1) + value*self.Threat(BW, current + i - 1)]]
                if self.board[current + i-1] < 19 and self.board[current + i -1] > 9 and BW == 20:
                    retpos = retpos + [[[curr, current+i-1], ((self.board[current + i - 1]%10)*(self.board[current + i - 1]%10) - 1) + value*self.Threat(BW, current + i - 1)]]
                current = current - 1
                if current < 0: break
                


        current = position
        i = 8
        if current + i < 64:
            while self.board[current + i] == 0 and current + i < 64:#vertical -> down
                
                


                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]
                
                if current + 16 < 64:
                    if self.board[current + i+8] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+i+8], ((self.board[current + i + 8]%10)*(self.board[current + i + 8]%10) + 1) + value*self.Threat(BW, current + i + 8)]]
                    if self.board[current + i+8] < 19 and self.board[current + i + 8] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+i+8], ((self.board[current + i + 8]%10)*(self.board[current + i + 8]%10) + 1) + value*self.Threat(BW, current + i + 8)]]

                if current + 8 < 64:
                    current = current + 8
                if current + i > 63:
                    break

                
                

        current = position
        i = -8
        if current + i > 0 :
            while self.board[current + i] == 0:#vertical -> up
                
                if current + i < 0:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

                if current - 16 > -1:
                    if self.board[current + i - 8] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+i-8], ((self.board[current + i - 8]%10)*(self.board[current + i - 8]%10) + 1) + value*self.Threat(BW, current + i - 8)]]
                    if self.board[current + i - 8] < 19 and self.board[current + i -8] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+i-8], ((self.board[current + i - 8]%10)*(self.board[current + i - 8]%10) + 1) + value*self.Threat(BW, current + i - 8)]]

                if current - 8 > -1:
                    current = current - 8 
                if current + i < 0:
                    break
                


        current = position
        #enemy piece beside current position
        if current + 1 < 64:
            if self.board[current + 1] != 0 and self.board[current + 1] > 16 and BW == 10 and current + 1 < 64:
                retpos = retpos + [[[curr, current+1], ((self.board[current + 1]%10)*(self.board[current + 1]%10) + 1) + value*self.Threat(BW, current + 1)]]
            if self.board[current + 1] != 0 and self.board[current + 1] < 16 and BW == 20 and current + 1 < 64:
                retpos = retpos + [[[curr, current+1], ((self.board[current + 1]%10)*(self.board[current + 1]%10) + 1) + value*self.Threat(BW, current + 1)]]

        if current - 1 > -1:
            if self.board[current - 1] != 0 and self.board[current - 1] > 16 and BW == 10 and current - 1 > 0:
                retpos = retpos + [[[curr, current - 1], ((self.board[current - 1]%10)*(self.board[current - 1]%10) + 1) + value*self.Threat(BW, current - 1)]]
            if self.board[current - 1] != 0 and self.board[current - 1] < 16 and BW == 20 and current - 1 > 0:
                retpos = retpos + [[[curr, current - 1], ((self.board[current - 1]%10)*(self.board[current - 1]%10) + 1) + value*self.Threat(BW, current - 1)]]

        if current + 8 < 64:
            if self.board[current + 8] != 0 and self.board[current + 8] > 16 and BW == 10 and current + 8 < 64:
                retpos = retpos + [[[curr, current + 8], ((self.board[current + 8]%10)*(self.board[current + 8]%10) + 1) + value*self.Threat(BW, current + 8)]]
            if self.board[current + 8] != 0 and self.board[current + 8] < 16 and BW == 20 and current + 8 < 64:
                retpos = retpos + [[[curr, current + 8], ((self.board[current + 8]%10)*(self.board[current + 8]%10) + 1) + value*self.Threat(BW, current + 8)]]

        if current - 8 > -1:
            if self.board[current - 8] != 0 and self.board[current - 8] > 16 and BW == 10 and current - 8 > 0:
                retpos = retpos + [[[curr, current - 8], ((self.board[current - 8]%10)*(self.board[current - 8]%10) + 1) + value*self.Threat(BW, current - 8)]]
            if self.board[current - 8] != 0 and self.board[current - 8] < 16 and BW == 20 and current - 8 > 0:
                retpos = retpos + [[[curr, current - 8], ((self.board[current - 8]%10)*(self.board[current - 8]%10) + 1) + value*self.Threat(BW, current - 8)]]




        return retpos
    def bishop(self, BW, position):
        value = 3
        retpos = []
        current = position
        curr = position



        i = -9
        while self.board[current + i] == 0 and current + i > -1:#up -> left


            if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                break
            retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

            if self.board[current + i] == 0 and current + i - 9 > -1 and current + i - 9 != 7 and current + i-9 != 15 and current + i-9 != 23 and current + i-9 != 31 and current + i-9 != 39 and current + i-9 != 47 and current + i-9 != 55:
                if self.board[current + i - 9] > 19 and BW == 10:
                    retpos = retpos + [[[curr, current+ i - 9], ((self.board[current + i - 9]%10)*(self.board[current + i - 9]%10) + 1) + value*self.Threat(BW, current + i - 9)]]
                if self.board[current + i - 9] < 19 and self.board[current + i - 9] > 9 and BW == 20:
                    retpos = retpos + [[[curr, current+ i - 9], ((self.board[current + i - 9]%10)*(self.board[current + i - 9]%10) + 1) + value*self.Threat(BW, current + i - 9)]]

            current = current - 9

        i = -7
        current = position

        while self.board[current + i] == 0 and current + i > -1:#up -> right


            if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 0 or current + i == 56:
                break
            retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

            if self.board[current + i] == 0 and current + i - 7 > -1 and current + i-7 != 8 and current + i-7 != 16 and current + i-7 != 24 and current + i-7 != 32 and current + i-7 != 40 and current + i-7 != 48 and current + i-7 != 0 and current + i - 7 != 56:
                if self.board[current + i - 7] > 19 and BW == 10:
                    retpos = retpos + [[[curr, current+ i - 7], ((self.board[current + i - 7]%10)*(self.board[current + i - 7]%10) + 1) + value*self.Threat(BW, current + i - 7)]]
                if self.board[current + i - 7] < 19 and self.board[current + i - 7] > 9 and BW == 20:
                    retpos = retpos + [[[curr, current+ i - 7], ((self.board[current + i - 7]%10)*(self.board[current + i - 7]%10) + 1) + value*self.Threat(BW, current + i - 7)]]
            current = current -7

        i = 7
        current = position
        if current + i < 64:
            while self.board[current + i] == 0:#down -> left
                
                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

                if self.board[current + i] == 0 and current +i+7 < 64 and current + i+7 != 7 and current + i+7 != 15 and current + i+7 != 23 and current + i+7 != 31 and current + i+7 != 39 and current + i+7 != 47 and current + i+7 != 55:
                    
                    if self.board[current + i + 7] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+ i + 7], ((self.board[current + i + 7]%10)*(self.board[current + i + 7]%10) + 1) + value*self.Threat(BW, current + i + 7)]]
                    if self.board[current + i + 7] < 19 and self.board[current + i + 7] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+ i + 7], ((self.board[current + i + 7]%10)*(self.board[current + i + 7]%10) + 1) + value*self.Threat(BW, current + i + 7)]]

                if current + 7 < 64:    
                    current = current + 7
                if current + i > 63:
                    break


        i = 9
        current = position
        if current + i < 64:
            while self.board[current + i] == 0:#down -> right

                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 56:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

                if self.board[current + i] == 0 and current +i+9 < 64 and current + i+9 != 8 and current + i+9 != 16 and current + i+9 != 24 and current + i+9 != 32 and current + i+9 != 40 and current + i+9 != 48 and current + i+9 != 56:
                    
                    if self.board[current + i+9] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+ i + 9], ((self.board[current + i + 9]%10)*(self.board[current + i + 9]%10) + 1) + value*self.Threat(BW, current + i + 9)]]
                    if self.board[current + i+9] < 19 and self.board[current + i + 9] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+ i + 9], ((self.board[current + i + 9]%10)*(self.board[current + i + 9]%10) + 1) + value*self.Threat(BW, current + i + 9)]]



                if current + 9 < 64: 
                    current = current + 9
                if current + i > 63:
                    break

        current = position
        #enemy piece beside current position
        
        if current + 9 < 64 and current +9 != 8 and current +9 != 16 and current +9 != 24 and current +9 != 32 and current +9 != 40 and current +9 != 48 and current +9 != 56:
            if self.board[current + 9] != 0 and self.board[current + 9] > 16 and BW == 10:
                retpos = retpos + [[[curr, current + 9], ((self.board[current  + 9]%10)*(self.board[current  + 9]%10) + 1) + value*self.Threat(BW, current  + 9)]]
            if self.board[current + 9] != 0 and self.board[current + 9] < 16 and BW == 20:
                retpos = retpos + [[[curr, current + 9], ((self.board[current  + 9]%10)*(self.board[current  + 9]%10) + 1) + value*self.Threat(BW, current  + 9)]]


        if current - 9 > -1 and current  - 9 != 7 and current -9 != 15 and current -9 != 23 and current -9 != 31 and current -9 != 39 and current -9 != 47 and current -9 != 55:
            if self.board[current - 9] != 0 and self.board[current - 9] > 16 and BW == 10:
                retpos = retpos + [[[curr, current - 9], ((self.board[current  - 9]%10)*(self.board[current  - 9]%10) + 1) + value*self.Threat(BW, current  - 9)]]
            if self.board[current - 9] != 0 and self.board[current - 9] < 16 and BW == 20:
                retpos = retpos + [[[curr, current - 9], ((self.board[current  - 9]%10)*(self.board[current  - 9]%10) + 1) + value*self.Threat(BW, current  - 9)]]


        if current + 7 < 64 and current +7 < 64 and current +7 != 7 and current +7 != 15 and current +7 != 23 and current +7 != 31 and current +7 != 39 and current +7 != 47 and current +7 != 55:
            if self.board[current + 7] != 0 and self.board[current + 7] > 16 and BW == 10:
                retpos = retpos + [[[curr, current + 7], ((self.board[current  + 7]%10)*(self.board[current  + 7]%10) + 1) + value*self.Threat(BW, current  + 7)]]
            if self.board[current + 7] != 0 and self.board[current + 7] < 16 and BW == 20:
                retpos = retpos + [[[curr, current + 7], ((self.board[current  + 7]%10)*(self.board[current  + 7]%10) + 1) + value*self.Threat(BW, current  + 7)]]


        if current - 7 > -1 and current-7 != 8 and current-7 != 16 and current-7 != 24 and current-7 != 32 and current-7 != 40 and current-7 != 48 and current-7 != 0 and current - 7 != 56:
            if self.board[current - 7] != 0 and self.board[current - 7] > 16 and BW == 10:
                retpos = retpos + [[[curr, current - 7], ((self.board[current  - 7]%10)*(self.board[current  - 7]%10) + 1) + value*self.Threat(BW, current  - 7)]]
            if self.board[current - 7] != 0 and self.board[current - 7] < 16 and BW == 20:
                retpos = retpos + [[[curr, current - 7], ((self.board[current  - 7]%10)*(self.board[current  - 7]%10) + 1) + value*self.Threat(BW, current  - 7)]]

        return retpos
    def queen(self, BW, position):
        value = 8
        retpos = []
        current = position
        curr = position



        i = -9
        while self.board[current + i] == 0 and current + i > -1:#up -> left


            if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                break
            retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

            if current + i - 9 > -1 and current + i - 9 != 7 and current + i-9 != 15 and current + i-9 != 23 and current + i-9 != 31 and current + i-9 != 39 and current + i-9 != 47 and current + i-9 != 55:
                if self.board[current + i - 9] > 19 and BW == 10:
                    retpos = retpos + [[[curr, current+ i - 9], ((self.board[current + i - 9]%10)*(self.board[current + i - 9]%10) + 1) + value*self.Threat(BW, current + i - 9)]]
                if self.board[current + i - 9] < 19 and self.board[current + i - 9] > 9 and BW == 20:
                    retpos = retpos + [[[curr, current+ i - 9], ((self.board[current + i - 9]%10)*(self.board[current + i - 9]%10) + 1) + value*self.Threat(BW, current + i - 9)]]

            current = current - 9

        i = -7
        current = position

        while self.board[current + i] == 0 and current + i > -1:#up -> right


            if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 0 or current + i == 56:
                break
            retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

            if current + i - 7 > -1 and current + i-7 != 8 and current + i-7 != 16 and current + i-7 != 24 and current + i-7 != 32 and current + i-7 != 40 and current + i-7 != 48 and current + i-7 != 0:
                if self.board[current + i - 7] > 19 and BW == 10:
                    retpos = retpos + [[[curr, current+ i - 7], ((self.board[current + i - 7]%10)*(self.board[current + i - 7]%10) + 1) + value*self.Threat(BW, current + i - 7)]]
                if self.board[current + i - 7] < 19 and self.board[current + i - 7] > 9 and BW == 20:
                    retpos = retpos + [[[curr, current+ i - 7], ((self.board[current + i - 7]%10)*(self.board[current + i - 7]%10) + 1) + value*self.Threat(BW, current + i - 7)]]
            current = current -7

        i = 7
        current = position
        if current + i < 64:
            while self.board[current + i] == 0:#down -> left
                
                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

                if current + i + 7 < 64 and current + i+7 != 7 and current + i+7 != 15 and current + i+7 != 23 and current + i+7 != 31 and current + i+7 != 39 and current + i+7 != 47 and current + i+7 != 55:
                    
                    if self.board[current + i + 7] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+ i + 7], ((self.board[current + i + 7]%10)*(self.board[current + i + 7]%10) + 1) + value*self.Threat(BW, current + i + 7)]]
                    if self.board[current + i + 7] < 19 and self.board[current + i + 7] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+ i + 7], ((self.board[current + i + 7]%10)*(self.board[current + i + 7]%10) + 1) + value*self.Threat(BW, current + i + 7)]]

                if current + 7 < 64:    
                    current = current + 7
                if current + 7 > 63:
                    break


        i = 9
        current = position
        if current + i < 64:
            while self.board[current + i] == 0:#down -> right

                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 56:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

                if current + i +9 < 64 and current + i+9 != 8 and current + i+9 != 16 and current + i+9 != 24 and current + i+9 != 32 and current + i+9 != 40 and current + i+9 != 48 and current + i+9 != 56:
                    
                    if self.board[current + i+9] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+ i + 9], ((self.board[current + i + 9]%10)*(self.board[current + i + 9]%10) + 1) + value*self.Threat(BW, current + i + 9)]]
                    if self.board[current + i+9] < 19 and self.board[current + i + 9] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+ i + 9], ((self.board[current + i + 9]%10)*(self.board[current + i + 9]%10) + 1) + value*self.Threat(BW, current + i + 9)]]



                if current + 9 < 64: 
                    current = current + 9
                if current + 9 > 63:
                    break

        current = position
        #enemy piece beside current position
        
        if current + 9 < 64 and current +9 != 8 and current +9 != 16 and current +9 != 24 and current +9 != 32 and current +9 != 40 and current +9 != 48 and current +9 != 56:
            if self.board[current + 9] != 0 and self.board[current + 9] > 16 and BW == 10:
                retpos = retpos + [[[curr, current + 9], ((self.board[current  + 9]%10)*(self.board[current  + 9]%10) + 1) + value*self.Threat(BW, current  + 9)]]
            if self.board[current + 9] != 0 and self.board[current + 9] < 16 and BW == 20:
                retpos = retpos + [[[curr, current + 9], ((self.board[current  + 9]%10)*(self.board[current  + 9]%10) + 1) + value*self.Threat(BW, current  + 9)]]


        if current - 9 > -1 and current  - 9 != 7 and current -9 != 15 and current -9 != 23 and current -9 != 31 and current -9 != 39 and current -9 != 47 and current -9 != 55:
            if self.board[current - 9] != 0 and self.board[current - 9] > 16 and BW == 10:
                retpos = retpos + [[[curr, current - 9], ((self.board[current  - 9]%10)*(self.board[current  - 9]%10) + 1) + value*self.Threat(BW, current  - 9)]]
            if self.board[current - 9] != 0 and self.board[current - 9] < 16 and BW == 20:
                retpos = retpos + [[[curr, current - 9], ((self.board[current  - 9]%10)*(self.board[current  - 9]%10) + 1) + value*self.Threat(BW, current  - 9)]]


        if current + 7 < 64 and current +7 < 64 and current +7 != 7 and current +7 != 15 and current +7 != 23 and current +7 != 31 and current +7 != 39 and current +7 != 47 and current +7 != 55:
            if self.board[current + 7] != 0 and self.board[current + 7] > 16 and BW == 10:
                retpos = retpos + [[[curr, current + 7], ((self.board[current  + 7]%10)*(self.board[current  + 7]%10) + 1) + value*self.Threat(BW, current  + 7)]]
            if self.board[current + 7] != 0 and self.board[current + 7] < 16 and BW == 20:
                retpos = retpos + [[[curr, current + 7], ((self.board[current  + 7]%10)*(self.board[current  + 7]%10) + 1) + value*self.Threat(BW, current  + 7)]]


        if current - 7 > -1 and current-7 != 8 and current-7 != 16 and current-7 != 24 and current-7 != 32 and current-7 != 40 and current-7 != 48 and current-7 != 0 and current - 7 != 56:
            if self.board[current - 7] != 0 and self.board[current - 7] > 16 and BW == 10:
                retpos = retpos + [[[curr, current - 7], ((self.board[current  - 7]%10)*(self.board[current  - 7]%10) + 1) + value*self.Threat(BW, current  - 7)]]
            if self.board[current - 7] != 0 and self.board[current - 7] < 16 and BW == 20:
                retpos = retpos + [[[curr, current - 7], ((self.board[current  - 7]%10)*(self.board[current  - 7]%10) + 1) + value*self.Threat(BW, current  - 7)]]

        current = position
        i = 1
        if current + i < 64:
            while self.board[current + i] == 0:#horizontal -> right

                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 56:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]
                if current + i + 1 < 64:
                    if self.board[current+i+1] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+i+1], ((self.board[current + i + 1]%10)*(self.board[current + i + 1]%10) + 1) + value*self.Threat(BW, current + i + 1)]]
                    if self.board[current+i+1] < 19 and self.board[current + i + 1] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+i+1], ((self.board[current + i + 1]%10)*(self.board[current + i + 1]%10) + 1) + value*self.Threat(BW, current + i + 1)]]

                current = current + 1
                if current + i> 63:
                    break

        current = position
        i = -1
        if current + i > -1:
            while self.board[current + i] == 0:#horizontal -> left

                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

                if self.board[current + i-1] > 19 and BW == 10:
                    retpos = retpos + [[[curr, current+i-1], ((self.board[current + i - 1]%10)*(self.board[current + i - 1]%10) - 1) + value*self.Threat(BW, current + i - 1)]]
                if self.board[current + i-1] < 19 and self.board[current + i -1] > 9 and BW == 20:
                    retpos = retpos + [[[curr, current+i-1], ((self.board[current + i - 1]%10)*(self.board[current + i - 1]%10) - 1) + value*self.Threat(BW, current + i - 1)]]
                current = current - 1
                if current < 0: break
                


        current = position
        i = 8
        if current + i < 64:
            while self.board[current + i] == 0 and current + i < 64:#vertical -> down
                
                


                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]
                
                if current + 16 < 64:
                    if self.board[current + i+8] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+i+8], ((self.board[current + i + 8]%10)*(self.board[current + i + 8]%10) + 1) + value*self.Threat(BW, current + i + 8)]]
                    if self.board[current + i+8] < 19 and self.board[current + i + 8] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+i+8], ((self.board[current + i + 8]%10)*(self.board[current + i + 8]%10) + 1) + value*self.Threat(BW, current + i + 8)]]

                if current + 8 < 64:
                    current = current + 8
                if current + i > 63:
                    break

                
                

        current = position
        i = -8
        if current + i > 0 :
            while self.board[current + i] == 0:#vertical -> up
                
                if current + i < 0:
                    break
                retpos = retpos + [[[curr, current+i], value*self.Threat(BW, current + i)]]

                if current - 16 > -1:
                    if self.board[current + i - 8] > 19 and BW == 10:
                        retpos = retpos + [[[curr, current+i-8], ((self.board[current + i - 8]%10)*(self.board[current + i - 8]%10) + 1) + value*self.Threat(BW, current + i - 8)]]
                    if self.board[current + i - 8] < 19 and self.board[current + i -8] > 9 and BW == 20:
                        retpos = retpos + [[[curr, current+i-8], ((self.board[current + i - 8]%10)*(self.board[current + i - 8]%10) + 1) + value*self.Threat(BW, current + i - 8)]]

                if current - 8 > -1:
                    current = current - 8 
                if current + i < 0:
                    break
                


        current = position
        #enemy piece beside current position
        if current + 1 < 64:
            if self.board[current + 1] != 0 and self.board[current + 1] > 16 and BW == 10 and current + 1 < 64:
                retpos = retpos + [[[curr, current+1], ((self.board[current + 1]%10)*(self.board[current + 1]%10) + 1) + value*self.Threat(BW, current + 1)]]
            if self.board[current + 1] != 0 and self.board[current + 1] < 16 and BW == 20 and current + 1 < 64:
                retpos = retpos + [[[curr, current+1], ((self.board[current + 1]%10)*(self.board[current + 1]%10) + 1) + value*self.Threat(BW, current + 1)]]

        if current - 1 > -1:
            if self.board[current - 1] != 0 and self.board[current - 1] > 16 and BW == 10 and current - 1 > 0:
                retpos = retpos + [[[curr, current - 1], ((self.board[current - 1]%10)*(self.board[current - 1]%10) + 1) + value*self.Threat(BW, current - 1)]]
            if self.board[current - 1] != 0 and self.board[current - 1] < 16 and BW == 20 and current - 1 > 0:
                retpos = retpos + [[[curr, current - 1], ((self.board[current - 1]%10)*(self.board[current - 1]%10) + 1) + value*self.Threat(BW, current - 1)]]

        if current + 8 < 64:
            if self.board[current + 8] != 0 and self.board[current + 8] > 16 and BW == 10 and current + 8 < 64:
                retpos = retpos + [[[curr, current + 8], ((self.board[current + 8]%10)*(self.board[current + 8]%10) + 1) + value*self.Threat(BW, current + 8)]]
            if self.board[current + 8] != 0 and self.board[current + 8] < 16 and BW == 20 and current + 8 < 64:
                retpos = retpos + [[[curr, current + 8], ((self.board[current + 8]%10)*(self.board[current + 8]%10) + 1) + value*self.Threat(BW, current + 8)]]

        if current - 8 > -1:
            if self.board[current - 8] != 0 and self.board[current - 8] > 16 and BW == 10 and current - 8 > 0:
                retpos = retpos + [[[curr, current - 8], ((self.board[current - 8]%10)*(self.board[current - 8]%10) + 1) + value*self.Threat(BW, current - 8)]]
            if self.board[current - 8] != 0 and self.board[current - 8] < 16 and BW == 20 and current - 8 > 0:
                retpos = retpos + [[[curr, current - 8], ((self.board[current - 8]%10)*(self.board[current - 8]%10) + 1) + value*self.Threat(BW, current - 8)]]

        return retpos
    def knightthreat(self, BW, position):

        retpos = []

        current = position
        if BW == 10:
            if current + 15 < 64 and current + 15 != 15 and current + 15 != 23 and current + 15 != 31 and current + 15 != 39\
                 and current + 15 != 47 and current + 15 != 55 and current + 15 != 63:
                if self.board[current + 15] == 0:
                    retpos = retpos + [current + 15]
                elif self.board[current + 15] > 16:
                    retpos = retpos + [current + 15]
            if current + 17 < 64 and current + 17 != 24 and current + 17 != 32 and current + 17 != 40 and current + 17 != 48\
                 and current + 17 != 56:
                if self.board[current + 17] == 0:
                    retpos = retpos + [current + 17]
                elif self.board[current + 17] > 16:
                    retpos = retpos + [current + 17]

            if current + 10 < 64 and current + 10 != 57 and current + 10 != 56 and current + 10 != 49 and current + 10 != 48 \
                and current + 10 != 41 and current + 10 != 40 and current + 10 != 33 and current + 10 != 32 and current + 10 != 25\
                 and current + 10 != 24 and current + 10 != 16 and current + 10 != 17and current +10 != 9 and current +10 != 8\
                 and current + 10 != 1 and current +10  != 0:

                if self.board[current + 10] == 0:
                    retpos = retpos + [current + 10]
                elif self.board[current + 10] > 16:
                    retpos = retpos + [current + 10]

            if current - 6 > 0  and current - 6 != 57 and current - 6 != 56 and current - 6 != 49 and current - 6 != 48 \
                and current - 6 != 41 and current - 6 != 40 and current - 6 != 33 and current  - 6 != 32 and current -6 != 25\
                 and current -6 != 24 and current -6 != 16 and current -6 != 17 and current - 6 != 9 and current - 6 != 8\
                 and current - 6 != 1 and current - 6 != 0:

                if self.board[current - 6] == 0:
                    retpos = retpos + [current -6]
                elif self.board[current - 6] > 16:
                    retpos = retpos + [current -6]

            if current + 6 < 64 and current + 6 != 63 and current + 6 !=  62 and current + 6 != 55 and current + 6 != 54 \
                and current + 6 != 47 and current + 6 != 46 and current + 6 != 39 and current + 6 != 38 and current + 6 != 31\
                and current + 6 != 30 and current + 6 != 32 and current + 6 != 22 and current + 6 != 15 and current + 6 != 14\
                and current + 6 != 7 and current + 6 != 6:

                if self.board[current + 6] == 0:
                    retpos = retpos + [current + 6]
                elif self.board[current + 6] > 16:
                    retpos = retpos + [current + 6]


            if current - 10 > -1 and current - 10 != 63 and current -10 !=  62 and current -10 != 55 and current -10 != 54 \
                and current -10 != 47 and current -10 != 46 and current -10 != 39 and current -10 != 38 and current -10 != 31\
                and current -10 != 30 and current -10 != 32 and current -10 != 22 and current -10 != 15 and current -10 != 14\
                and current -10 != 7 and current -10 != 6:   

                if self.board[current -10] == 0:
                    retpos = retpos + [current - 10]
                elif self.board[current - 10] > 16:
                    retpos = retpos + [current - 10]

            if current - 17 > -1 and current - 17 != 15 and current - 17 != 23 and current - 17 != 31 and current -17 != 39\
                 and current - 17 != 47 and current - 17 != 55 and current -17 != 7:

                if self.board[current -17 ] == 0:
                    retpos = retpos + [current - 17]
                elif self.board[current - 17] > 16:
                    retpos = retpos + [current - 17]

            if current - 15 > -1 and current - 15 != 24 and current - 15 != 32 and current - 15 != 40 and current - 15 != 48\
                 and current - 15 != 0:
                if self.board[current -15] == 0:
                    retpos = retpos + [current - 15]
                elif self.board[current - 15] > 16:
                    retpos = retpos + [current - 15]
            

        else:
            if current + 15 < 64 and current + 15 != 15 and current + 15 != 23 and current + 15 != 31 and current + 15 != 39\
                 and current + 15 != 47 and current + 15 != 55 and current + 15 != 63:
                if self.board[current + 15] == 0:
                    retpos = retpos + [current + 15]
                elif self.board[current + 15] < 16:
                    retpos = retpos + [current + 15]
            if current + 17 < 64 and current + 17 != 24 and current + 17 != 32 and current + 17 != 40 and current + 17 != 48\
                 and current + 17 != 56:
                if self.board[current + 17] == 0:
                    retpos = retpos + [current + 17]
                elif self.board[current + 17] < 16:
                    retpos = retpos + [current + 17]

            if current + 10 < 64 and current + 10 != 57 and current + 10 != 56 and current + 10 != 49 and current + 10 != 48 \
                and current + 10 != 41 and current + 10 != 40 and current + 10 != 33 and current + 10 != 32 and current + 10 != 25\
                 and current + 10 != 24 and current + 10 != 16 and current + 10 != 17and current +10 != 9 and current +10 != 8\
                 and current + 10 != 1 and current +10  != 0:

                if self.board[current + 10] == 0:
                    retpos = retpos + [current + 10]
                elif self.board[current + 10] < 16:
                    retpos = retpos + [current + 10]

            if current - 7 > 0  and current - 6 != 57 and current - 6 != 56 and current - 6 != 49 and current - 6 != 48 \
                and current - 6 != 41 and current - 6 != 40 and current - 6 != 33 and current  - 6 != 32 and current -6 != 25\
                 and current -6 != 24 and current -6 != 16 and current -6 != 17 and current - 6 != 9 and current - 6 != 8\
                 and current - 6 != 1 and current - 6 != 0:

                if self.board[current - 6] == 0:
                    retpos = retpos + [current -6]
                elif self.board[current - 6] < 16:
                    retpos = retpos + [current -6]

            if current + 7 < 64 and current + 6 != 63 and current + 6 !=  62 and current + 6 != 55 and current + 6 != 54 \
                and current + 6 != 47 and current + 6 != 46 and current + 6 != 39 and current + 6 != 38 and current + 6 != 31\
                and current + 6 != 30 and current + 6 != 32 and current + 6 != 22 and current + 6 != 15 and current + 6 != 14\
                and current + 6 != 7 and current + 6 != 6:

                if self.board[current + 6] == 0:
                    retpos = retpos + [current + 6]
                elif self.board[current + 6] < 16:
                    retpos = retpos + [current + 6]


            if current - 10 > -1 and current - 10 != 63 and current -10 !=  62 and current -10 != 55 and current -10 != 54 \
                and current -10 != 47 and current -10 != 46 and current -10 != 39 and current -10 != 38 and current -10 != 31\
                and current -10 != 30 and current -10 != 32 and current -10 != 22 and current -10 != 15 and current -10 != 14\
                and current -10 != 7 and current -10 != 6:   

                if self.board[current -10] == 0:
                    retpos = retpos + [current - 10]
                elif self.board[current - 10] < 16:
                    retpos = retpos + [current - 10]

            if current - 17 > -1 and current - 17 != 15 and current - 17 != 23 and current - 17 != 31 and current -17 != 39\
                 and current - 17 != 47 and current - 17 != 55 and current -17 != 7:

                if self.board[current -17 ] == 0:
                    retpos = retpos + [current - 17]
                elif self.board[current - 17] < 16:
                    retpos = retpos + [current - 17]

            if current - 15 > -1 and current - 15 != 24 and current - 15 != 32 and current - 15 != 40 and current - 15 != 48\
                 and current - 15 != 0:
                if self.board[current -15] == 0:
                    retpos = retpos + [current - 15]
                elif self.board[current - 15] < 16:
                    retpos = retpos + [current - 15]

        return retpos
    def knight(self, BW, position):

        retpos = []
        value = 2
        current = position
        if BW == 10:
            if current + 15 < 64 and current + 15 != 15 and current + 15 != 23 and current + 15 != 31 and current + 15 != 39\
                 and current + 15 != 47 and current + 15 != 55 and current + 15 != 63:
                if self.board[current + 15] == 0:
                    retpos = retpos + [[[current, current + 15], value*self.Threat(10, current + 15)]]
                elif self.board[current + 15] > 16:
                    retpos = retpos + [[[current, current + 15], ((self.board[current + 15]%10)*(self.board[current + 15]%10) + 1) + value*self.Threat(10, current + 15)]]
            if current + 17 < 64 and current + 17 != 24 and current + 17 != 32 and current + 17 != 40 and current + 17 != 48\
                 and current + 17 != 56:
                if self.board[current + 17] == 0:
                    retpos = retpos + [[[current, current + 17], value*self.Threat(10, current + 17)]]
                elif self.board[current + 17] > 16:
                    retpos = retpos + [[[current, current + 17], ((self.board[current + 17]%10)*(self.board[current + 17]%10) + 1) + value*self.Threat(10, current + 17)]]

            if current + 10 < 64 and current + 10 != 57 and current + 10 != 56 and current + 10 != 49 and current + 10 != 48 \
                and current + 10 != 41 and current + 10 != 40 and current + 10 != 33 and current + 10 != 32 and current + 10 != 25\
                 and current + 10 != 24 and current + 10 != 16 and current + 10 != 17and current +10 != 9 and current +10 != 8\
                 and current + 10 != 1 and current +10  != 0:

                if self.board[current + 10] == 0:
                    retpos = retpos + [[[current, current + 10], value*self.Threat(10, current + 10)]]
                elif self.board[current + 10] > 16:
                    retpos = retpos + [[[current, current + 10], ((self.board[current + 10]%10)*(self.board[current + 10]%10) + 1) + value*self.Threat(10, current + 10)]]

            if current - 7 > 0  and current - 6 != 57 and current - 6 != 56 and current - 6 != 49 and current - 6 != 48 \
                and current - 6 != 41 and current - 6 != 40 and current - 6 != 33 and current  - 6 != 32 and current -6 != 25\
                 and current -6 != 24 and current -6 != 16 and current -6 != 17 and current - 6 != 9 and current - 6 != 8\
                 and current - 6 != 1 and current - 6 != 0:

                if self.board[current - 6] == 0:
                    retpos = retpos + [[[current, current -6], value*self.Threat(10, current - 6)]]
                elif self.board[current - 6] > 16:
                    retpos = retpos + [[[current, current - 6], ((self.board[current - 6]%10)*(self.board[current - 6]%10) + 1) + value*self.Threat(10, current - 6)]]

            if current + 7 < 64 and current + 6 != 63 and current + 6 !=  62 and current + 6 != 55 and current + 6 != 54 \
                and current + 6 != 47 and current + 6 != 46 and current + 6 != 39 and current + 6 != 38 and current + 6 != 31\
                and current + 6 != 30 and current + 6 != 32 and current + 6 != 22 and current + 6 != 15 and current + 6 != 14\
                and current + 6 != 7 and current + 6 != 6:

                if self.board[current + 6] == 0:
                    retpos = retpos + [[[current, current + 6], value*self.Threat(10, current + 6)]]
                elif self.board[current + 6] > 16:
                    retpos = retpos + [[[current, current + 6], ((self.board[current + 6]%10)*(self.board[current + 6]%10) + 1) + value*self.Threat(10, current + 6)]]


            if current - 10 > -1 and current - 10 != 63 and current -10 !=  62 and current -10 != 55 and current -10 != 54 \
                and current -10 != 47 and current -10 != 46 and current -10 != 39 and current -10 != 38 and current -10 != 31\
                and current -10 != 30 and current -10 != 32 and current -10 != 22 and current -10 != 15 and current -10 != 14\
                and current -10 != 7 and current -10 != 6:   

                if self.board[current -10] == 0:
                    retpos = retpos + [[[current, current - 10], value*self.Threat(10, current - 10)]]
                elif self.board[current - 10] > 16:
                    retpos = retpos + [[[current, current - 10], ((self.board[current - 10]%10)*(self.board[current - 10]%10) + 1) + value*self.Threat(10, current - 10)]]

            if current - 17 > -1 and current - 17 != 15 and current - 17 != 23 and current - 17 != 31 and current -17 != 39\
                 and current - 17 != 47 and current - 17 != 55 and current -17 != 7:

                if self.board[current -17 ] == 0:
                    retpos = retpos + [[[current, current - 17], value*self.Threat(10, current - 17)]]
                elif self.board[current - 17] > 16:
                    retpos = retpos + [[[current, current - 17], ((self.board[current - 17]%10)*(self.board[current - 17]%10) + 1) + value*self.Threat(10, current - 17)]]

            if current - 15 > -1 and current - 15 != 24 and current - 15 != 32 and current - 15 != 40 and current - 15 != 48\
                 and current - 15 != 0:
                if self.board[current -15] == 0:
                    retpos = retpos + [[[current, current - 15], value*self.Threat(10, current - 15)]]
                elif self.board[current - 15] > 16:
                    retpos = retpos + [[[current, current - 15], ((self.board[current - 15]%10)*(self.board[current - 15]%10) + 1) + value*self.Threat(10, current - 15)]]
            

        else:
            if current + 15 < 64 and current + 15 != 15 and current + 15 != 23 and current + 15 != 31 and current + 15 != 39\
                 and current + 15 != 47 and current + 15 != 55 and current + 15 != 63:
                if self.board[current + 15] == 0:
                    retpos = retpos + [[[current, current + 15], value*self.Threat(20, current + 15)]]
                elif self.board[current + 15] < 16:
                    retpos = retpos + [[[current, current + 15], ((self.board[current + 15]%10)*(self.board[current + 15]%10) + 1) + value*self.Threat(20, current + 15)]]
            if current + 17 < 64 and current + 17 != 24 and current + 17 != 32 and current + 17 != 40 and current + 17 != 48\
                 and current + 17 != 56:
                if self.board[current + 17] == 0:
                    retpos = retpos + [[[current, current + 17], value*self.Threat(20, current + 17)]]
                elif self.board[current + 17] < 16:
                    retpos = retpos + [[[current, current + 17], ((self.board[current + 17]%10)*(self.board[current + 17]%10) + 1) + value*self.Threat(20, current + 17)]]

            if current + 10 < 64 and current + 10 != 57 and current + 10 != 56 and current + 10 != 49 and current + 10 != 48 \
                and current + 10 != 41 and current + 10 != 40 and current + 10 != 33 and current + 10 != 32 and current + 10 != 25\
                 and current + 10 != 24 and current + 10 != 16 and current + 10 != 17and current +10 != 9 and current +10 != 8\
                 and current + 10 != 1 and current +10  != 0:

                if self.board[current + 10] == 0:
                    retpos = retpos + [[[current, current + 10], value*self.Threat(20, current + 10)]]
                elif self.board[current + 10] < 16:
                    retpos = retpos + [[[current, current + 10], ((self.board[current + 10]%10)*(self.board[current + 10]%10) + 1) + value*self.Threat(20, current + 10)]]

            if current - 7 > 0  and current - 6 != 57 and current - 6 != 56 and current - 6 != 49 and current - 6 != 48 \
                and current - 6 != 41 and current - 6 != 40 and current - 6 != 33 and current  - 6 != 32 and current -6 != 25\
                 and current -6 != 24 and current -6 != 16 and current -6 != 17 and current - 6 != 9 and current - 6 != 8\
                 and current - 6 != 1 and current - 6 != 0:

                if self.board[current - 6] == 0:
                    retpos = retpos + [[[current, current - 6], value*self.Threat(20, current - 6)]]
                elif self.board[current - 6] < 16:
                    retpos = retpos + [[[current, current - 6], ((self.board[current - 6]%10)*(self.board[current - 6]%10) + 1) + value*self.Threat(20, current - 6)]]

            if current + 7 < 64 and current + 6 != 63 and current + 6 !=  62 and current + 6 != 55 and current + 6 != 54 \
                and current + 6 != 47 and current + 6 != 46 and current + 6 != 39 and current + 6 != 38 and current + 6 != 31\
                and current + 6 != 30 and current + 6 != 32 and current + 6 != 22 and current + 6 != 15 and current + 6 != 14\
                and current + 6 != 7 and current + 6 != 6:

                if self.board[current + 6] == 0:
                    retpos = retpos + [[[current, current + 6], value*self.Threat(20, current + 6)]]
                elif self.board[current + 6] < 16:
                    retpos = retpos + [[[current, current + 6], ((self.board[current + 6]%10)*(self.board[current + 6]%10) + 1) + value*self.Threat(20, current + 6)]]


            if current - 10 > -1 and current - 10 != 63 and current -10 !=  62 and current -10 != 55 and current -10 != 54 \
                and current -10 != 47 and current -10 != 46 and current -10 != 39 and current -10 != 38 and current -10 != 31\
                and current -10 != 30 and current -10 != 32 and current -10 != 22 and current -10 != 15 and current -10 != 14\
                and current -10 != 7 and current -10 != 6:   

                if self.board[current -10] == 0:
                    retpos = retpos + [[[current, current - 10], value*self.Threat(20, current - 10)]]
                elif self.board[current - 10] < 16:
                    retpos = retpos + [[[current, current - 10], ((self.board[current - 10]%10)*(self.board[current - 10]%10) + 1) + value*self.Threat(20, current - 10)]]

            if current - 17 > -1 and current - 17 != 15 and current - 17 != 23 and current - 17 != 31 and current -17 != 39\
                 and current - 17 != 47 and current - 17 != 55 and current -17 != 7:

                if self.board[current -17 ] == 0:
                    retpos = retpos + [[[current, current - 17], value*self.Threat(20, current - 17)]]
                elif self.board[current - 17] < 16:
                    retpos = retpos + [[[current, current - 17], ((self.board[current - 17]%10)*(self.board[current - 17]%10) + 1) + value*self.Threat(20, current - 17)]]

            if current - 15 > -1 and current - 15 != 24 and current - 15 != 32 and current - 15 != 40 and current - 15 != 48\
                 and current - 15 != 0:
                if self.board[current -15] == 0:
                    retpos = retpos + [[[current, current - 15], value*self.Threat(20, current - 15)]]
                elif self.board[current - 15] < 16:
                    retpos = retpos + [[[current, current - 15], ((self.board[current - 15]%10)*(self.board[current - 15]%10) + 1) + value*self.Threat(20, current - 15)]]

        return retpos
    def king(self, BW, position):
        retpos = []
        current = position
        curr = position
        value = 100

        if BW == 10:
            if current + 8 < 64:
                if self.board[current + 8] == 0:
                    retpos = retpos + [[[curr, current + 8], value * self.Threat(10, current + 8)]]
                elif self.board[current + 8]  > 16:
                    retpos = retpos + [[[curr, current + 8], ((self.board[current + 8]%10)*(self.board[current + 8]%10) + 1) + value * self.Threat(10, curr + 8)]]

            if current - 8 > -1:
                if self.board[current -8] == 0:
                    retpos = retpos + [[[curr, current - 8], value * self.Threat(10, current - 8)]]
                elif self.board[current - 8]  > 16:
                    retpos = retpos + [[[curr, current - 8], ((self.board[current - 8]%10)*(self.board[current - 8]%10) + 1) + value * self.Threat(10, curr - 8)]]
            i = 1
            if current + 1 < 64 and current + i != 8 and current + i != 16 and current + i != 24 and current + i != 32 and current + i != 40 and current + i != 48 and current + i != 56:
                if self.board[current + 1] == 0:
                    retpos = retpos + [[[curr, current + 1], value * self.Threat(10, current + 1)]]
                elif self.board[current + 1]  > 16:
                    retpos = retpos + [[[curr, current + 1], ((self.board[current + 1]%10)*(self.board[current + 1]%10) + 1) + value * self.Threat(10, curr + 1)]]
            i = - 1
            if current - 1 > -1 and current + i != 7 and current + i != 15 and current + i != 23 and current + i != 31 and current + i != 39 and current + i != 47 and current + i != 55:
                if self.board[current - 1] == 0:
                    retpos = retpos + [[[curr, current - 1], value * self.Threat(10, current -1)]]
                elif self.board[current - 1]  > 16:
                    retpos = retpos + [[[curr, current - 1], ((self.board[current - 1]%10)*(self.board[current - 1]%10) + 1) + value * self.Threat(10, curr - 1)]]

            i = -9
            if current + i > -1 and current + i != 7 and current + i != 15 and current + i != 23 and current + i != 31 and current + i != 39 and current + i != 47 and current + i != 55:
                if self.board[current + i] == 0:
                    retpos = retpos + [[[curr, current + i], value * self.Threat(10, current + i)]]
                elif self.board[current + i] > 16:
                    retpos = retpos + [[[curr, current + i], ((self.board[current + i]%10)*(self.board[current + i]%10) + 1) + value * self.Threat(10, curr + i)]]


            i = 9   
            if current + i < 64 and current + i != 8 and current + i != 16 and current + i != 24 and current + i != 32 and current + i != 40 and current + i != 48 and current + i != 56:
                if self.board[current + i] == 0:
                    retpos = retpos + [[[curr, current + i], value * self.Threat(10, current + i)]]
                elif self.board[current + i] > 16:
                    retpos = retpos + [[[curr, current + i], ((self.board[current + i]%10)*(self.board[current + i]%10) + 1) + value * self.Threat(10, curr + i)]]


            i = -7
            if current + i > -1 and current + i != 8 and current + i != 16 and current + i != 24 and current + i != 32 and current + i != 40 and current + i != 48 and current + i != 0 and current + i != 56: 
                if self.board[current + i] == 0:
                    retpos = retpos + [[[curr, current + i], value * self.Threat(10, current + i)]]
                elif self.board[current + i] > 16:
                    retpos = retpos + [[[curr, current + i], ((self.board[current + i]%10)*(self.board[current + i]%10) + 1) + value * self.Threat(10, curr + i)]]


            i = 7
            if current + i < 64 and current + i != 7 and current + i != 15 and current + i != 23 and current + i != 31 and current + i != 39 and current + i != 47 and current + i != 55 and current + i != 63:
                if self.board[current + i] == 0:
                    retpos = retpos + [[[curr, current + i], value * self.Threat(10, current + i)]]
                elif self.board[current + i] > 16:
                    retpos = retpos + [[[curr, current + i], ((self.board[current + i]%10)*(self.board[current + i]%10) + 1) + value * self.Threat(10, curr + i)]]
       


        else:

            if current + 8 < 64:
                if self.board[current + 8] == 0:
                    retpos = retpos + [[[curr, current + 8], value * self.Threat(20, current + 8)]]
                elif self.board[current + 8]  < 16:
                    retpos = retpos + [[[curr, current + 8], ((self.board[current + 8]%10)*(self.board[current + 8]%10) + 1) + value * self.Threat(20, curr + 8)]]

            if current - 8 > -1:
                if self.board[current -8] == 0:
                    retpos = retpos + [[[curr, current - 8], value * self.Threat(20, current - 8)]]
                elif self.board[current - 8]  < 16:
                    retpos = retpos + [[[curr, current - 8], ((self.board[current - 8]%10)*(self.board[current - 8]%10) + 1) + value * self.Threat(20, curr - 8)]]

            i = 1
            if current + 1 < 64 and current + i != 8 and current + i != 16 and current + i != 24 and current + i != 32 and current + i != 40 and current + i != 48 and current + i != 56:
                if self.board[current + 1] == 0:
                    retpos = retpos + [[[curr, current + 1], value * self.Threat(20, current + 1)]]
                elif self.board[current + 1]  < 16:
                    retpos = retpos + [[[curr, current + 1], ((self.board[current + 1]%10)*(self.board[current + 1]%10) + 1) + value * self.Threat(20, curr + 1)]]
            i = - 1
            if current - 1 > -1 and current + i != 7 and current + i != 15 and current + i != 23 and current + i != 31 and current + i != 39 and current + i != 47 and current + i != 55:
                if self.board[current - 1] == 0:
                    retpos = retpos + [[[curr, current - 1], value * self.Threat(20, current -1)]]
                elif self.board[current - 1]  < 16:
                    retpos = retpos + [[[curr, current - 1], ((self.board[current - 1]%10)*(self.board[current - 1]%10) + 1) + value * self.Threat(20, curr - 1)]]

            i = -9
            if current + i > -1 and current + i != 7 and current + i != 15 and current + i != 23 and current + i != 31 and current + i != 39 and current + i != 47 and current + i != 55:
                if self.board[current + i] == 0:
                    retpos = retpos + [[[curr, current + i], value * self.Threat(20, current + i)]]
                elif self.board[current + i] < 16:
                    retpos = retpos + [[[curr, current + i], ((self.board[current + i]%10)*(self.board[current + i]%10) + 1) + value * self.Threat(20, curr + i)]]


            i = 9   
            if current + i < 64 and current + i != 8 and current + i != 16 and current + i != 24 and current + i != 32 and current + i != 40 and current + i != 48 and current + i != 56:
                if self.board[current + i] == 0:
                    retpos = retpos + [[[curr, current + i], value * self.Threat(20, current + i)]]
                elif self.board[current + i] < 16:
                    retpos = retpos + [[[curr, current + i], ((self.board[current + i]%10)*(self.board[current + i]%10) + 1) + value * self.Threat(20, curr + i)]]


            i = -7
            if current + i > -1 and current + i != 8 and current + i != 16 and current + i != 24 and current + i != 32 and current + i != 40 and current + i != 48 and current + i != 0:
                if self.board[current + i] == 0:
                    retpos = retpos + [[[curr, current + i], value * self.Threat(20, current + i)]]
                elif self.board[current + i] < 16:
                    retpos = retpos + [[[curr, current + i], ((self.board[current + i]%10)*(self.board[current + i]%10) + 1) + value * self.Threat(20, curr + i)]]


            i = 7
            if current + i < 64 and current + i != 7 and current + i != 15 and current + i != 23 and current + i != 31 and current + i != 39 and current + i != 47 and current + i != 55:
                if self.board[current + i] == 0:
                    retpos = retpos + [[[curr, current + i], value * self.Threat(20, current + i)]]
                elif self.board[current + i] < 16:
                    retpos = retpos + [[[curr, current + i], ((self.board[current + i]%10)*(self.board[current + i]%10) + 1) + value * self.Threat(20, curr + i)]]
        return retpos

    def Threat(self, BW, position):

        safe = 0

        current = position
        if BW == 10:
            #horizontals/verticals
            i = 8
            while(current + i< 64):
                if self.board[current + i] == 24 or self.board[current + i] == 23:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i + 8
            i = -8
            while (current +i> -1):
                if self.board[current + i] == 24 or self.board[current + i] == 23:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i - 8
            i = 1
            while (current + i < 64):
                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 56:
                    break
                if self.board[current + i] == 24 or self.board[current + i] == 23:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i + 1
            i = -1
            while (current + i> -1):
                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                if self.board[current + i] == 24 or self.board[current + i] == 23:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i - 1
            #diagonals
            i = 9
            while(current + i < 64):

                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 56:
                    break
                if self.board[current + i] == 24 or self.board[current + i] == 22:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i + 9
            i = 7
            while (current + i < 64):
                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                if self.board[current + i] == 24 or self.board[current + i] == 22:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i + 7
            i = -7
            while (current + i > -1):
                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 0:
                    break
                if self.board[current + i] == 24 or self.board[current + i] == 22:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i-7
            i = -9
            while (current + i > -1):
                
                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                if self.board[current + i] == 24 or self.board[current + i] == 22:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i - 9


            #knight check
            knights = self.knightthreat(10, position)
            #print knights
            for i in range(0, len(knights)):
                if self.board[knights[i]] == 21:
                    safe = -1
                    return safe


            #pawn check
            i = 9
            if(current + i < 64 and current + i != 8 and current + i != 16 and current + i != 24 and current + i != 32 and current + i != 40 and current + i != 48 and current + i != 56):

              
                if self.board[current + i] == 20:
                    safe = -1
                    return safe
               
                
            i = 7
            if (current + i < 64 and current + i != 7 and current + i != 15 and current + i != 23 and current + i != 31 and current + i != 39 and current + i != 47 and current + i != 55):

                if self.board[current + i] == 20:
                    safe = -1
                    return safe

            return safe


        else:
            #horizontals/verticals
            i = 8
            while(current + i< 64):
                if self.board[current + i] == 14 or self.board[current + i] == 13:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i + 8
            i = -8
            while (current +i> -1):
                if self.board[current + i] == 14 or self.board[current + i] == 13:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i - 8
            i = 1
            while (current + i < 64):
                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 56:
                    break
                if self.board[current + i] == 14 or self.board[current + i] == 13:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i + 1
            i = -1
            while (current + i> -1):
                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                if self.board[current + i] == 14 or self.board[current + i] == 13:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i - 1
            #diagonals
            i = 9
            while(current + i < 64):

                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 56:
                    break
                if self.board[current + i] == 14 or self.board[current + i] == 12:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i + 9
            i = 7
            while (current + i < 64):
                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                if self.board[current + i] == 14 or self.board[current + i] == 12:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i + 7
            i = -7
            while (current + i > -1):
                if current + i == 8 or current + i == 16 or current + i == 24 or current + i == 32 or current + i == 40 or current + i == 48 or current + i == 0:
                    break
                if self.board[current + i] == 14 or self.board[current + i] == 12:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i-7
            i = -9
            while (current + i > -1):
                
                if current + i == 7 or current + i == 15 or current + i == 23 or current + i == 31 or current + i == 39 or current + i == 47 or current + i == 55:
                    break
                if self.board[current + i] == 14 or self.board[current + i] == 12:
                    safe = -1
                    return safe
                elif self.board[current + i] != 0:
                    break
                i = i - 9


            #knight check
            knights = self.knightthreat(20, position)
            #print knights
            for i in range(0, len(knights)):
                if self.board[knights[i]] == 11:
                    safe = -1
                    return safe


            #pawn check
           
                

              
            i = -7
            if (current + i > -1 and current + i != 8 and current + i != 16 and current + i != 24 and current + i != 32 and current + i != 40 and current + i != 48 and current + i != 0):
          
                if self.board[current + i] == 10:
                    safe = -1
                    return safe
              
            i = -9
            if(current + i > -1 and current + i != 7 and current + i != 15 and current + i != 23 and current + i != 31 and current + i != 39 and current + i != 47 and current + i != 55):
                
               
                if self.board[current + i] == 10:
                    safe = -1
                    return safe


            return safe




    def move(self, initial, final):
        return 0



C = chess(           [13, 11, 12, 15, 14, 12, 11, 13, \
                      10, 10, 10, 10, 10, 10, 10, 10, \
                       0,  0,  0,  0,  0,  0,  0,  0, \
                       0,  0,  0,  0,  0,  0,  0,  0, \
                       0,  0,  0,  0,  0,  0,  0,  0, \
                       0,  0,  0,  0,  0,  0,  0,  0, \
                      20, 20, 20, 20, 20, 20, 20, 20, \
                      23, 21, 22, 25, 24, 22, 21, 23])

#print (" ----- Black Side -----")
#C.printboard()
#rint (" ----- White Side -----")

#print("")

#print ("Raw Board: "),
#C.printrawboard()

#Y = C.GPP(10)
#X = C.GPP(20)

#print ("")
#print "White: " + str(Y)
#print "Black: " + str(X)


#est2 = C.APM(20)

#print test2

#test3 = sorted(test2, key=key1, reverse=True)
#print test3
boardt =  [0,0,0,0,0,0,0,0,\
           0,0,0,0,0,0,0,0,\
           0,0,0,0,0,0,0,0,\
           0,0,0,0,0,0,0,0,\
           0,0,0,0,0,0,0,0,\
           0,0,0,0,0,0,0,0,\
           0,0,0,0,0,0,0,0,\
           0,0,0,0,0,0,0,0,]


def key1(item):
    return item[1]

def chessPlayer(board, player):
    C = chess(board)
    move = [0,0]
    candidateMoves = []
    evalTree = []
    retval = [True, move, candidateMoves, evalTree]
    candidateMoves = C.APM(player)
    for i in range(0, len(candidateMoves)):
        candidateMoves[i][1] = float(candidateMoves[i][1])
    #print candidateMoves
    moves = sorted(candidateMoves, key=key1, reverse = True)
    #print moves
    if len(moves) > 0:
        move = moves[0][0]
    move1 = []
    move0 = []
    if len(moves) > 1:
        pin = len(moves) - 1
        for i in range (1, len(moves)):
            if moves[i][1] != moves [i-1][1]:
                pin = i-1
                break
        move1 = moves[randint(0,pin)]
        move0 = move1[0]

   # print move1

    mv = []
    if len(moves) > 1:
        mv = moves
        #print mv
        mv.remove(move1)
    #print mv


    evalTree = evalTree + [move1]
    #print evalTree
    evalTree = evalTree + mv
    #print evalTree

    #print move
  #  for i in range (0, len(moves)):
   #     evalTree = evalTree + [moves[i][0]]
    #for i in range (0, len(moves)):
     #   evalTree = evalTree + [moves[i][1]]

    #print evalTree
    #print candidateMoves
    #print evalTree
    retval = [True, move0, candidateMoves, evalTree]
    return retval

#debugging


print ("error test")

#hi = chessPlayer(boardt, 20)
#for i in range(0, 64):
boardt = [0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,25,10,15,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0] 


#   boardt[i] = 20
C = chess(boardt)
C.printboard()
#   print boardt
hi = chessPlayer(boardt, 20)
print hi
print
print
print
print



for i in range(0, 11):
    print ("Test " + str(i))
    boardt =      [0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,\
                   0,0,0,0,0,0,0,0,]
    for i in range(0,15):
        position = randint(0,63)
        piece = randint(10,15)
        boardt[position] = piece
    for i in range(0,15):
        position = randint(0,63)
        piece = randint(20,25)
        boardt[position] = piece
    C = chess(boardt)
    C.printboard()
    print
    print

    C.printrawboard()

    print
    print("-----White Movement-----")
    white = chessPlayer(boardt, 10)
    print white
    print
    print("-----Black Movement-----")
    black = chessPlayer(boardt, 20)
    print black
    print 
    print 
    print



print ("error check")
E = chess(boardt)
EE = E.Threat(20, 38)
print EE




#print hi
#print hi
#[  0, 13, 12, 15,  0,  0,  13,  0, \
 #                     10, 10, 10, 10,  23, 10, 10, 10, \
   #                    0,  0, 11,  0, 10, 12,  0,  0, \
    #                   0,  0, 20,  0,  0,  0, 20,  0, \
     #                  0,  0,  0, 20,  15,  0,  0,  0, \
      #                20, 14, 21,  0, 20,  0,  0, 21, \
       #                0, 20,  0, 22,  0,  0, 20, 20, \
        #               23, 0,  0, 25, 24, 22,  0, 23]
