name="Computer"
distance=3
for i in list (name):
      if ord(i)+distance<ord('2'):
              print(chr(ord(i)+distance))
      else:
           new=ord(i)+distance-ord('2')
           print(chr(96+new))  