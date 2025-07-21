from flask import Flask, request, render_template, send_from_directory
import os
import cv2
from ultralytics import YOLO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
model = YOLO(r'C:\Users\shakt\OneDrive\Desktop\project\runs\detect\train\weights\best.pt')  # Update with your trained model path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Read image
        img = cv2.imread(filepath)

        # Perform detection
        results = model(img)

        # Draw bounding boxes
        for result in results:
            for box in result.boxes:
                cls = model.names[int(box.cls[0])]
                conf = box.conf[0]
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, f'{cls} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Save the annotated image
        annotated_path = os.path.join(app.config['UPLOAD_FOLDER'], 'annotated_' + file.filename)
        cv2.imwrite(annotated_path, img)

        return render_template('result.html', original=filepath, annotated=annotated_path)

if __name__ == '__main__':
    app.run(debug=True) 