import cv2

# holt die main Cam
cam = cv2.VideoCapture(0)

while True:
    # speicher die Bilder ab
    _, image = cam.read()

    # konvert farn bild in graues Bild
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 30, 100)

    cv2.imshow("LiveVideoVonMir", image)
    cv2.imshow("GrauBild", gray)
    cv2.imshow("Edges", edges)
    # ord ist für die konvetierung in eine zahl q  zu num
    # Klick q um zu beenden
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()