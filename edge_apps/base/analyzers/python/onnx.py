import cv2

def load_model(model_path):
    return cv2.dnn.readNetFromONNX(model_path)


def run_inference(model, input_image, cuda=False):
    blob = cv2.dnn.blobFromImage(input_image, scalefactor=1/255.0, size=(224, 224), mean=(0, 0, 0), swapRB=True, crop=False)
    model.setInput(blob)

    if cuda:
        model.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        model.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    output = model.forward()
    return output


if __name__ == "__main__":

    model_path = "models/onnx/tinyyolov2-8/tinyyolov2-8.onnx"
    model = load_model(model_path)
    image = cv2.imread("/Users/nathanaday/SoftwareProjects/open4.0/edge_apps/base/analyzers/python/test_images/alex-6mVD_D68thY-unsplash.jpg")
    output = run_inference(model, image)
    print(type(output))
    print(output.shape)
