import cv2


def compare_2_images(org_file, new_file):
    org_file = cv2.imread(org_file)
    new_file = cv2.imread(new_file)
    difference = cv2.subtract(org_file, new_file)
    b, g, r = cv2.split(difference)
    return cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0
