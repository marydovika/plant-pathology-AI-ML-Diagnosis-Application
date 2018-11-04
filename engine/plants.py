import face_recognition as f
import cv2
import _pickle as c
import os


def display(loc, dpname):
    top, right, bottom, left = loc
    cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 0, 255), 2)
    cv2.rectangle(frame, (left * 4, bottom * 4 - 35),
                  (right * 4, bottom * 4), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, dpname, (left * 4 + 6, bottom * 4 - 6), font, 1.0, (255, 255, 255), 1)


print ("loading plant database")
plants = {}
for plant in os.listdir("plants/"):
    if not plant.startswith("."):
        with open("plants/" + plant, 'rb') as fp:
            plant_info = c.load(fp)
            plants[plant] = {}
            plants[plant]["info"] = plant_info
            plants[plant]["name"] = plant

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    sframe = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    sframe = sframe[:, :, ::-1]
    plant_locations = f.plant_locations(sframe)
    for loc in plant_locations:
        dpname = ""
        plant_enc = f.plant_encodings(sframe, [loc])[0]
        for plant in plants:
            match = f.compare_plants([plants[plant]["info"]], plant_enc, tolerance=0.5)
            if match[0]:
                dpname = plants[plant]["name"]
                break
        display(loc, dpname)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
