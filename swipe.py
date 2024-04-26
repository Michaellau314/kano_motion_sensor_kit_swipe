'''
Kano Motion Sensor Kit Community Python SDK can be found at:
https://github.com/KanoComputing/community-sdk/releases
'''

from communitysdk import list_connected_devices, MotionSensorKit
import serial, pyautogui, time

devices = list_connected_devices()
msk_filter = filter(lambda device: isinstance(device, MotionSensorKit), devices)
msk = next(msk_filter, None) # Get first Motion Sensor Kit

if msk == None:
	print('No Motion Sensor was found :(')
else:
	def on_gesture(gestureValue):
		if gestureValue == 'left':
			pyautogui.press('left')
			print('Swipe ', gestureValue)
			time.sleep(1)
		if gestureValue == 'right':
			pyautogui.press('right')
			print('Swipe ', gestureValue)
			time.sleep(1)
	try:
		msk.set_mode('gesture')
	except Exception as e:
		print(e)
	msk.on_gesture = on_gesture
	#print('Wave your hand above the Motion Sensor:')