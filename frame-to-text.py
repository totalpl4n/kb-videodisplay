import cv2
import sys
import os

def convert(x):
    binastr = "".join(x)
    bina = int(binastr,2)
    hexa = hex(bina)
    y = hexa[2:].zfill(2)
    return y

while True:
    final = "["

    path = "./frame"
    frames = 0
    for m in os.listdir(path):
        if os.path.isfile(os.path.join(path, m)):
            frames += 1
    
    temp = input("Press enter to start the script")
    
    print()
    print("vvvvvvv | Copy everything below until the other copy message | vvvvvvv")
    
    for i in range (frames):
        data = cv2.imread(str("./frame/frame" + str(i) + ".png"), 0)
        if not data is None:
            datalist = data.tolist()
        else:
            print("Error: Invalid file type / no data in 'frame' folder.")
            temp = input("Press enter to exit")
            sys.exit()
        if not len(datalist) == 8:
                print("Error: Frame size must be 16x8.")
                temp = input("Press enter to exit.")
                sys.exit()
        line = []
        for j in range(16): 
            for k in range(8): 
                linevalue = datalist[k].pop(0)
                if linevalue <= 127:
                    linevalue = 0
                elif linevalue > 127:
                    linevalue = 1
                line.append(str(linevalue))
            byte = convert(line) 
            line.clear()
            if j == 0: 
                final = str(final + r'b"\x' + byte)
            elif j > 0:
                final = str(final + r'\x' + byte)
        final = str(final + '"')
        if i < frames-1:
            final = str(final + ',')
    final = str(final + "]")
    print (final)
    print("^^^^^^^ | Copy everything above until the other copy message | ^^^^^^^")

