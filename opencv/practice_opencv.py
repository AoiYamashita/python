import numpy as np
import cv2

#flat = cv2.imread("./flat.jpg")

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'));

cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

cap2 = cap.set(cv2.CAP_PROP_FPS, 30)#30fps is bottom

bgr = [65,209,254]

#define const

bottom_thresh = 80

top_thresh = 80

px_rate = 8#distance of camera * px of object

circle_size = 0.026#meter

tan_view_angle = np.tan(78)#11.4/23.8#horizon angle,Verticalangle

max_circle_number = 10

while True:
	# 1フレームずつ取得する。
	ret, frame = cap.read()
	#フレームが取得できなかった場合は、画面を閉じる
	if not ret:
		break
	
	frame = cv2.resize(frame,None,fx=1.0,fy=1.0)
	
	#frame = cv2.addWeighted(frame, 1.0, flat, 0.55, -20)
	
	#frame_size = [frame.shape[0],frame.shape[1]]
	  
	minBGR = np.array([bgr[0] - bottom_thresh, bgr[1] - bottom_thresh, bgr[2] - bottom_thresh])
	maxBGR = np.array([bgr[0] + top_thresh, bgr[1] + top_thresh, bgr[2] + top_thresh])
	  
	#####################
	  
	#画像の2値化
	maskBGR = cv2.inRange(frame,minBGR,maxBGR)
	#画像のマスク（合成）
	resultBGR = cv2.bitwise_and(frame, frame, mask = maskBGR)

	#serch circle
	gray_bgr = cv2.cvtColor(resultBGR,cv2.COLOR_BGR2GRAY)
	
	ret, th_circle = cv2.threshold(gray_bgr, 90, 255, cv2.THRESH_BINARY)
	
	gray_bgr = cv2.medianBlur(gray_bgr,3)
	
	#cv2.imshow("result",gray_bgr)
	
	contours, hierarchy = cv2.findContours(th_circle,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	if len(contours) > 0:
		count = 0
		for cnt, i in enumerate(contours):
			if count > max_circle_number:
				break
				
			#ellipse
			"""
			if len(i) > 5:
				retval = cv2.fitEllipse(i)
				if int((retval[1][0]+retval[1][1])/2) > 5 and int((retval[1][0]+retval[1][1])/2) < 90:
					cv2.circle(frame,(int(retval[0][0]),int(retval[0][1])),int((retval[1][0]+retval[1][1])/2),(0,255,0),2)
					cv2.circle(frame,(int(retval[0][0]),int(retval[0][1])),1,(255,0,0),1)
			
			#circle
			"""
			
			center ,r = cv2.minEnclosingCircle(i)
			
			#sort
			"""
			center = np.array(center)
			r = np.array(r)
			
			center = center[np.argsort(r)]
			print(r.shape)
			r = np.sort(r)
			"""
			
			if int(r) > 5 and int(r) < 90:
				cv2.circle(frame,(int(center[0]),int(center[1])),int(r),(0,255,0),2)
				cv2.circle(frame,(int(center[0]),int(center[1])),2,(255,0,0),1)
				cv2.circle(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)),2,(255,0,0),1)
				
				distance = px_rate/r
				
				cv2.putText(frame,text=str(distance),org=(int(center[0]),int(center[1])),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0, 255, 0),thickness=2,lineType=cv2.LINE_AA)
				
				
				abs_center = center
				
				center = [center[0]-frame.shape[1]/2,-center[1]+frame.shape[0]/2]
				
				view_dis = np.sqrt(center[0]**2 + center[1]**2)*circle_size/(2*r)
				
				view_coord = [view_dis*center[0]/np.sqrt(center[0]**2 + center[1]**2),view_dis*center[1]/np.sqrt(center[0]**2 + center[1]**2)]
				
				obj_coord = [view_coord[0],np.sqrt(distance**2-view_dis**2)]
				
				cv2.putText(frame,text="x="+str(obj_coord[0]),org=(int(abs_center[0]),int(abs_center[1]+50)),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0, 255, 0),thickness=2,lineType=cv2.LINE_AA)
				cv2.putText(frame,text="y="+str(obj_coord[1]),org=(int(abs_center[0]),int(abs_center[1]+100)),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0, 255, 0),thickness=2,lineType=cv2.LINE_AA)
				
				count += 1
	
	cv2.circle(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)),2,(255,0,0),1)
	
	cv2.imshow("frame",frame)
	
	"""
	circles = cv2.HoughCircles(gray_bgr,cv2.HOUGH_GRADIENT,dp = 4,minDist = 90, param1 = 100, param2 = 50,minRadius = 0,maxRadius = 80)
	
	circle_result = frame
	
	if not(circles is None):
		circles = np.array(circles, dtype=np.uint8)
		for cir in circles[0,:]:
			cv2.circle(circle_result,(cir[0],cir[1]),cir[2],(0,255,0),5)
			cv2.circle(circle_result,(cir[0],cir[1]),5,(255,0,0),5)
		
	cv2.imshow("result",resultBGR)
	cv2.imshow("circle",cv2.Canny(gray_bgr,100,100))
    #print(balls)
	cv2.imshow("frame",circle_result)
	"""
  
	key = cv2.waitKey(1)
	# Escキーを入力されたら画面を閉じる
	if key == 27:
		break
    
cap.release()
cv2.destroyAllWindows()

