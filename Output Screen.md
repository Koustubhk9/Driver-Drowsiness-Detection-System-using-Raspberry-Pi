<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/76b5bda0-202e-4326-8c65-c18692870858" /> 


Scenario 1: Eyes Open (Awake State)
In this normal condition, the subject is facing the camera with both eyes wide open. The EAR (eye aspect ratio) remains stable, generally above the threshold value of 0.25. The system continuously monitors the frame using the landmark model and tracks eye landmarks. No alert is triggered. This validates that the system doesn’t produce false positives during normal driving conditions. In this output screen, the user’s eyes are open, and green contours are drawn around the eyes using detected landmark points. EAR remains high, and no alert is shown.



<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/9598cf2b-5438-46c1-8f80-30ee03b60215" />

Scenario 2: Eyes Closed (Simulated Drowsiness)
In this scenario, the subject closes their eyes for 2 or more seconds to simulate microsleep or drowsiness. This is the core test of the project. The EAR falls below the critical threshold of 0.25 and remains low for more than 48–60 consecutive frames (about 2 seconds at 24 fps). The system raises a red-colored ALERT message on the screen.

