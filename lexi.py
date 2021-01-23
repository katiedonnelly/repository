# lexi is cute

print('hello,world')
# import pippip.main (['install','pyfirmata'])
# from pyfirmata import Arduino,util

try:
    from pyfirmata import Ardunio, util
except:
    import pip
    pip.main (['install','pyfirmata'])
    from pyfirmata import Arduino,util
board = Arduino('COM6')
iterator = util.Iterator(board)
iterator.start()
something = board.get_pin('a:0:1')



countin=0
countout=0
total =0
# something =16
# while(1==1):
    # if (something>15 and something<30):
      #  countin = countin+1
    # if (something<15 and something>0):
      #   countout = countout+1
    # total = countin-countout
    # print(total)



















