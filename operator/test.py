import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    success, frame = cap.read()
    if success:
        # gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # model = cv2.CascadeClassifier('model.xml')
        # result = model.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1)
        # for (x, y, w, h) in result:
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 255), thickness=3)
        #     cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, w / 200, (255, 255, 255))

        # Кодируем кадр в бинарный формат
        print(len(frame))
        cv2.imshow('1', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break