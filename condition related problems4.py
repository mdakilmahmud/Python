angle1=float(input('Enter the first angle of the triangle: '))
angle2=float(input('Enter the second angle of the triangle: '))
angle3=float(input('Enter the third angle of the triangle: '))
if 0<angle1<180 and 0<angle2<180 and 0<angle3<180 :
      if angle1+angle2+angle3==180:
            print("The triangle is valid.")
      else:
            print("The triangle is not valid.")
else:
      print("Enter a valid trianle.")