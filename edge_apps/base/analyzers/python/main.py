import cv2 
import numpy as np
import json


class Analyzer:
    def __init__(self):
        self.model = None
        self.image = None
        self.results = []

    def load_model(self, prototxt_path, caffemodel_path):
        """
        Load the Caffe model.
        :param prototxt_path: Path to the model's deploy.prototxt file.
        :param caffemodel_path: Path to the model's .caffemodel file.
        """
        self.model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)
        print("Model loaded successfully.")

    def load_image(self, image_path):
        """
        Load the image to analyze.
        :param image_path: Path to the image file.
        """
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError(f"Image file '{image_path}' not found.")
        print("Image loaded successfully.")

    def analyze(self, input_size=(300, 300), confidence_threshold=0.2):

        """
        Perform object recognition on the loaded image.
        :param input_size: Tuple (width, height) for resizing the input image.
        :param confidence_threshold: Confidence threshold for filtering detections.
        """

        if self.model is None or self.image is None:
            raise ValueError("Model and image must be loaded before analyzing.")
        
        # Prepare the image for the model
        blob = cv2.dnn.blobFromImage(self.image, 1.0, input_size, (104.0, 117.0, 123.0))
        self.model.setInput(blob)
        detections = self.model.forward()

        # Parse the detections
        h, w = self.image.shape[:2]
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > confidence_threshold:
                class_id = int(detections[0, 0, i, 1])
                x1 = int(detections[0, 0, i, 3] * w)
                y1 = int(detections[0, 0, i, 4] * h)
                x2 = int(detections[0, 0, i, 5] * w)
                y2 = int(detections[0, 0, i, 6] * h)
                self.results.append((class_id, confidence, (x1, y1, x2, y2)))

        print(f"Detected {len(self.results)} objects.")

    def display_results(self, labels=None):
        """
        Display the results on the image.
        :param labels: List of class labels corresponding to the model's output.
        """
        for class_id, confidence, box in self.results:
            x1, y1, x2, y2 = box
            label = f"Class {class_id} {confidence:.2f}"
            if labels:
                label = f"{labels[class_id]} {confidence:.2f}"
            cv2.rectangle(self.image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(self.image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow("Results", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Instantiate the analyzer
    analyzer = Analyzer()

    # Paths to the model files (adjust these paths)
    prototxt_path = "models/SSD_512x512/deploy.prototxt"
    caffemodel_path = "models/SSD_512x512/VGG_coco_SSD_512x512_iter_360000.caffemodel"
    image_path = "test_images/alex-6mVD_D68thY-unsplash.jpg"

    # Class labels (adjust for your model)
    labels = []
    with open("models/SSD_512x512/labels.json") as f:
        labels = json.load(f)

    # Load and analyze
    analyzer.load_model(prototxt_path, caffemodel_path)
    analyzer.load_image(image_path)
    analyzer.analyze()
    analyzer.display_results(labels)

