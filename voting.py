# import pippip.main (['install','pyfirmata'])
# from pyfirmata import Arduino,util

# try: from pyfirmata import Ardunio, util
# except:
    # import pip
# pip.main (['install','pyfirmata'])
# from pyfirmata import Arduino,util
# board = Arduino('COM3')
# iterator = util.Iterator(board)
# interator.start()
# something = board.get_pin('a:0:1')
import random
countin=0
countout=0
total =0
voterbooths=int(input('booths at polling location '))

something= random.randint(0,500)

if (something>350 and something<500):
    countin = countin+1
if (something<350 and something>0):
    countout = countout+1
total = countin-countout
print(total)
people_in_line = total-voterbooths
go_to_next_available_booth = voterbooths - total
if (voterbooths==20): print ("allow 20 countin ")
if (voterbooths<total): print ("line "+ str(people_in_line))
if (voterbooths>total): print ("booth available"+ str(go_to_next_available_booth))














