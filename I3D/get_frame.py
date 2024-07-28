import cv2
import numpy as np
import os
from multiprocessing import Pool, cpu_count
import os
import time
import pdb

if __name__ == '__main__':

    root_path = '/home/yeling/yeling/data/yeling_code/TackleVideos-190/'
    mx_path_save = '/home/yeling/yeling/data/yeling_code/frame_data'
    if not os.path.exists(mx_path_save):
        os.mkdir(mx_path_save)
    for fi in  os.listdir(root_path):
        mx_path=os.path.join(root_path,fi)

        videos = sorted(os.listdir(mx_path))
        for video_name in videos:
            
            video_path=os.path.join(mx_path_save,video_name.split('.')[0])

            if not os.path.exists(video_path):
                os.mkdir(video_path)
            cap = cv2.VideoCapture(os.path.join(mx_path,video_name))
            c_frame = 1
            while (True):

                # print(cap.isOpened(),cap.read(),c_frame,os.path.join(mx_path,video_name))
                ret, frame = cap.read()
                # pdb.set_trace()
                if ret:
                    cv2.imwrite(os.path.join(video_path, 'img_' + str('{:05d}'.format(c_frame)) + '.jpg'), frame)
                else:

                    break
                c_frame = c_frame + 1
            cap.release()
