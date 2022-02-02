#!/usr/bin/env python
import cv2
import numpy as np

print(f"OpenCV {cv2.__version__}")
print(f"numpy  {np.__version__}")

def getSamplingRectangle(img_size):
    """Get a rectangle specified by upper left and lower right points ((x1,y1),(x2,y2))"""
    img_width = img_size[1]
    img_height = img_size[0]

    rect_width = 100
    rect_height = 80

    center_x = img_width//2
    center_y = int(img_height*4/5)
    x_left = np.clip(center_x - rect_width//2, 0, img_width)
    x_right = np.clip(x_left + rect_width, 0, img_width)
    y_top = np.clip(center_y - rect_height//2, 0, img_height)
    y_bottom = np.clip(y_top + rect_height, 0, img_height)
    
    return (
        (x_left, y_top),
        (x_right, y_bottom)
    )

def extractFeatures(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #return cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    # Extracting B, G, R channels, so just return a copy
    #return np.copy(frame)
    
def extractTrainingSamples(feature_image, sampling_rectangle):
    """Retun samples within a rectangle as a n x ch vector"""
    
    def rectangleToSlice(sampling_rectangle):
        """Convert a rectangle to a slice to be used with np arrays ((x1:x2)(y1:y2))"""
        tl, br = sampling_rectangle
        xx,yy = zip(tl,br)
        return slice(*yy), slice(*xx)
    
    y_range, x_range = rectangleToSlice(sampling_rectangle)
    patch = feature_image[y_range, x_range]
    samples = patch.reshape(-1,3)
    return samples

def performSegmentation(input_image, thresh, use_otsu):
    # We need to represent the distances in uint16 because of Otsu's method.
    # We get a pretty good resolution by multiplying the distances with 1000.
    scale = 1000
    scaled_input = np.uint16(input_image * scale)
    thresh_val = thresh * scale

    thresh_type = cv2.THRESH_BINARY_INV
    if use_otsu:
        thresh_type |= cv2.THRESH_OTSU
        
    thresh_val, segmented_image = cv2.threshold(scaled_input, thresh_val, 255, thresh_type)

    #structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    #segmented_image = cv2.morphologyEx(segmented_image, cv2.MORPH_OPEN, structuring_element)
    #segmented_image = cv2.morphologyEx(segmented_image, cv2.MORPH_CLOSE, structuring_element)
    return int(thresh_val/ scale), np.uint8(segmented_image)

def drawSamplingRectangle(image, sampling_rectangle):
    tl, dr = sampling_rectangle
    color = (0, 0, 255)
    thickness = 3
    image = cv2.rectangle(image, tl, dr, color, thickness)

def updateSamples(old_samples, new_samples, update_ratio):
    rand_num = np.random.rand(new_samples.shape[0])
    selected_samples = rand_num < update_ratio
    old_samples[selected_samples] = new_samples[selected_samples]

class MultivariateNormalModel:
    def __init__(self, samples):
        self.__performTraining(samples)

    def __performTraining(self, samples):
        self.mean = samples.mean(0)
        self.covariance = np.cov(samples, rowvar=False)
        self.inverse_covariance = np.linalg.inv(self.covariance)

    def computeMahalanobisDistances(self, image):
        import scipy.spatial.distance as SSD

        samples = np.float32(image).reshape(-1,3)
        mahalanobis_img = SSD.cdist(samples, self.mean[None, :], metric='mahalanobis', VI=self.inverse_covariance).reshape(image.shape[:2])
        
        return mahalanobis_img


def run_segmentation_lab():
    device_id = 0
    cap = cv2.VideoCapture(device_id)
    if not cap.isOpened():
        print(f"Could not open camera {device_id}")
        return
    else:
        print(f"Successfully opened camera {device_id}")

    use_otsu = False
    use_adaptive_model = False
    thresh_val = 8
    adaptive_update_ratio = 0.1

    def onchange(val):
        nonlocal thresh_val
        thresh_val = val

    success, frame = cap.read()
    
    if not success:
        return

    sampling_rectangle = getSamplingRectangle(frame.shape)
    feature_image = extractFeatures(frame)
    samples = extractTrainingSamples(feature_image, sampling_rectangle)
    model = MultivariateNormalModel(samples)

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.namedWindow('mahalanobis_img', cv2.WINDOW_NORMAL)
    cv2.namedWindow('segmented', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('Threshold', 'frame', thresh_val, 100, onchange)
    
    while(True):
        success, frame = cap.read()
        
        if not success:
            break

        feature_image = extractFeatures(frame)
        
        if use_adaptive_model:
            new_samples = extractTrainingSamples(feature_image, sampling_rectangle)
            updateSamples(samples, new_samples, adaptive_update_ratio)
            model = MultivariateNormalModel(samples)

        mahalanobis_img = model.computeMahalanobisDistances(feature_image)
        thresh_val, segmented = performSegmentation(mahalanobis_img, thresh_val, use_otsu)

        frame[segmented > 0] = (0,255,0)
        drawSamplingRectangle(frame, sampling_rectangle)
        viz = (mahalanobis_img - mahalanobis_img.min())/(mahalanobis_img.max() - mahalanobis_img.min())
        
        cv2.imshow('frame', frame)
        cv2.imshow('mahalanobis_img', viz)
        cv2.imshow('segmented', segmented)
        cv2.setTrackbarPos('Threshold', 'frame', thresh_val)
        
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord(' '):
            samples, patch = extractTrainingSamples(feature_image, sampling_rectangle)
            model = MultivariateNormalModel(samples)
        elif key == ord('o'):
            use_otsu = not use_otsu
        elif key == ord('a'):
            use_adaptive_model = not use_adaptive_model

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    """Hei"""
    run_segmentation_lab()