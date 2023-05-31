import os
import cv2

def read_files(relative_path):
    images = []
    files = os.listdir(relative_path)
    files.sort()
    for filename in files:
        img = cv2.GaussianBlur(cv2.cvtColor(cv2.imread(os.path.join(relative_path, filename)), cv2.COLOR_BGR2RGB),
                               (5, 5), 0)
        if img is not None:
            images.append(img)
    return images

def create_video():
    image_folder = 'Shedegi1'  # Use the folder
    video_name = 'circle.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or
              img.endswith(".jpeg") or img.endswith("png")]
    images.sort()
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()


def read_image(path):
    image = cv2.imread(path)
    return image


def object_detection():
    capture = cv2.VideoCapture("1.mp4")
    img_2 = read_image("frames/frame100.png")

    count = 0
    left = []
    right = []
    while capture.isOpened():
        ret, img_1 = capture.read()
        if ret:
            diff = cv2.absdiff(img_1, img_2)

            diff_blur = cv2.GaussianBlur(diff, (5, 5), 0)

            _, thresh_bin = cv2.threshold(diff_blur, 50, 255, cv2.THRESH_BINARY)
            wow = cv2.cvtColor(thresh_bin,cv2.COLOR_BGR2GRAY)
            img_1 = img_1[50:250, 100:1500]
            wow = wow[50:250, 100:1500]
            contours, hierarchy = cv2.findContours(wow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            #
            cv2.line(img_1, (164, 82), (265, 82), (255, 0, 0), 5)

            cv2.line(img_1, (1355, 82), (1446, 82), (255, 0, 0), 5)

            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                if cv2.contourArea(contour) > 50:
                    cv2.rectangle(img_1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    if y == 82:
                        left.append(count)
                    if y == 69:
                        right.append(count)
            cv2.drawContours(img_1, contours, -1, (0, 255, 0), 2)
            count += 1

            cv2.imshow("Detecting Motion...", img_1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    if len(right) != 0:
        frames = abs((left[0] - right[len(right)-1]))
        time = frames / 20
        print("time: ", time)
        distance = 43

        speed = distance / time * 3600 / 1000
        print("Speed: ", speed )
        print("frames: " , frames)


create_video()
object_detection()
