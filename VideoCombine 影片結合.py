import numpy as np
import cv2

#intput video setting 影片輸入設定

cap1 = cv2.VideoCapture('7穩定.avi')#讀取輸入影片1 Read input video1
cap2 = cv2.VideoCapture('gopro8 1 60fps.mp4')#讀取輸入影片2 Read input video2


# Get width and height of video1,2 取得影片12的高跟寬 

w1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
w2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
h2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Get frames video1,2 second (fps) 取得影片12的fps 
fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

# Define the codec for output video 定義輸出的設定 
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# Set up output video 輸出的設定 
out = cv2.VideoWriter('video_out_combine2.avi', fourcc, fps1, (w1+w2, h1))

# Get frame count 計算總禎數 
n_frames = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))

# start combine 開始結合影片 
for i in range(n_frames-1):

    #顯示處理進度
    print(str(i+1)+"/"+str(cap1.get(cv2.CAP_PROP_FRAME_COUNT)) )
    
    # Read next frame 讀取下一禎 
    success, frame1 = cap1.read()
    success, frame2 = cap2.read()

    # if fail 如果沒有讀取成功
    if not success:
        break

    # add word on video 加字
    text1 = 'Gopro7穩定'
    text2 = 'Gopro8'
    
    # cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
    cv2.putText(frame1, text1, (640, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL,5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame2, text2, (640, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL,5, (0, 0, 255), 2, cv2.LINE_AA)

    # Combine 結合影片並且寫入
    frame_out = cv2.hconcat([frame1, frame2])
    out.write(frame_out)

    # save frame
    #cv2.imwrite("1.jpg",frame_out)
    #cv2.imshow("frame_out",frame_out)
    

# Release Memory 釋放記憶體 
cap1.release()
cap2.release()
out.release()

# Close windows 關掉視窗
cv2.destroyAllWindows()
