import numpy
import cv2

cap = cv2.VideoCapture(0)
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter("out",fourcc,20.00,(640,480))

print(cap)
while True: 
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if(cv2.waitKey(1)) & 0xFF == ord('q'):
        break
cap.release()
# out.release()
cv2.destroyAllWindows()
