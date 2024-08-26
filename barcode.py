import cv2 as cv
import dbr
from dbr import *

BarcodeReader.init_license("t0073oQAAAIsT65fcCbyyACGAuMfjbVBZykH7XZvOYP7Utl1qbtwGnEMmIhoz3+JobdNoXIZBZGjeWin/gcMUfb20y/z3vBcAx+8iFg==")
reader = BarcodeReader()

def process_frame(frame):
    results = None
    try:
        results = reader.decode_buffer(frame)
    except BarcodeReaderError as bre:
        print(bre)
    
    return results


camera = cv.VideoCapture(0)
ret, frame = camera.read()

detected = False

while True:
    ret, frame = camera.read()
    results = process_frame(frame)
    if results != None:
        for result in results:
            points = result.localization_result.localization_points
            cv.line(frame, points[0], points[1], (0,255,0), 2)
            cv.line(frame, points[1], points[2], (0,255,0), 2)
            cv.line(frame, points[2], points[3], (0,255,0), 2)
            cv.line(frame, points[3], points[0], (0,255,0), 2)
            cv.putText(frame, result.barcode_text, points[0], cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
            detected = True

    cv.imshow('Barcode & QR Code Scanner', frame)
    ch = cv.waitKey(1)
    if ch == 27:
        break
    elif detected == True:
        break

scanned = result.barcode_text
print(scanned)