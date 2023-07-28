import cv2
import os

# 获取视频文件列表
video_path = "F:\MCE_3c_10"
video_files = [f for f in os.listdir(video_path) if f.endswith('.avi')]

# 循环遍历每个视频文件
for video_file in video_files:
    # 打开视频文件
    cap = cv2.VideoCapture(os.path.join(video_path, video_file))
    # 获取视频帧率
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # 获取视频名称
    video_name = os.path.splitext(video_file)[0]
    # 创建保存图像的文件夹
    save_path = os.path.join(video_path, video_name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 循环遍历每个视频帧并保存为图像文件
    frame_count = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            # 保存图像文件
            frame_count += 1
            frame_file = os.path.join(save_path, video_name + "_" + str(frame_count) + ".png")
            cv2.imwrite(frame_file, frame)
        else:
            break

    cap.release()
