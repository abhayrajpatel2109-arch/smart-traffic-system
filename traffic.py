# import cv2

# # Use webcam (0) or video file
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Resize for better view
#     frame = cv2.resize(frame, (800, 600))

#     # Draw stop line
#     line_y = 300
#     cv2.line(frame, (0, line_y), (800, line_y), (0, 0, 255), 3)

#     # Convert to gray
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Simple motion detection
#     _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

#     # Find contours (moving objects)
#     contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     for cnt in contours:
#         x, y, w, h = cv2.boundingRect(cnt)

#         # Ignore small objects
#         if w > 50 and h > 50:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

#             # Check if object crosses line
#             if y + h > line_y:
#                 cv2.putText(frame, "Violation Detected!", (200, 50),
#                             cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

#     cv2.imshow("Traffic Simulation", frame)

#     if cv2.waitKey(1) == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()
  
#--------------------------------------------------------------------------------------------
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

# Background subtractor (for motion detection)
fgbg = cv2.createBackgroundSubtractorMOG2()

signal = "GREEN"
last_switch = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))

    # --- SIGNAL LOGIC ---
    current_time = time.time()
    if current_time - last_switch > 5:  # switch every 5 sec
        signal = "RED" if signal == "GREEN" else "GREEN"
        last_switch = current_time

    # Draw signal
    color = (0,255,0) if signal == "GREEN" else (0,0,255)
    cv2.putText(frame, f"Signal: {signal}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    # --- STOP LINE ---
    line_y = 350
    cv2.line(frame, (0, line_y), (800, line_y), (255, 0, 0), 3)

    # --- MOTION DETECTION ---
    fgmask = fgbg.apply(frame)
    _, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if w > 50 and h > 50:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

            # --- VIOLATION CONDITION ---
            if signal == "RED" and (y + h > line_y):
                cv2.putText(frame, "VIOLATION!", (250, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)

                # Save image
                cv2.imwrite(f"violation_{int(time.time())}.jpg", frame)

    cv2.imshow("Traffic System", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()