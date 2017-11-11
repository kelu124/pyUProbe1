import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import binascii
# For videos
import subprocess
matplotlib.use('Agg')
from PIL import Image

def CreateUSData(DataName,RAWDATA_LINE_IN_FRAME,RAWDATA_SAMPLE_IN_LINE):
	RawData = []
	Line = []
	BegLines = []
	video = []

	with open('data/'+DataName+'.data') as fp:
	    for line in fp:
		if ":5002 " in line:
			RawData.append(line.strip().split(":5002 ")[1])
	LenOfLines = len(RawData[0])
	## Creating the array
	for j in range(len(RawData)):
	    Data = RawData[j]
	    for i in range(LenOfLines/2):
		Line.append(int(Data[2*i]+Data[2*i+1], 32))
	## Knowing where the images start
	for pos in range(len(Line)-2):
		if (Line[pos] == 170):
		    if (Line[pos+1] == 325):
		        if (Line[pos+4] == 170):
		            if (Line[pos+5] == 325):
		                    BegLines.append(pos-1)
	NbImages = (int)(len(BegLines)/RAWDATA_LINE_IN_FRAME)
	## Assembling the video
	for k in range(NbImages):
	    image = []
	    for i in range(RAWDATA_LINE_IN_FRAME):
		line = []
		for j in range(RAWDATA_SAMPLE_IN_LINE):
		    line.append(Line[BegLines[i+RAWDATA_LINE_IN_FRAME*k]+j])
		image.append(line)

	    video.append(np.array(image).astype(float))

	return NbImages,video
	    


def CreateUSVideo(video,DataName,NbImages,VideoFrameRate):
	VideoFilName = "./video/"+DataName+'.avi'
	cmdstring = ('ffmpeg',
		     '-y',
		     '-r', '%d' % VideoFrameRate,
		     '-f','image2pipe',
		     '-vcodec', 'mjpeg',
		     '-i', 'pipe:', 
		     '-vcodec', 'libxvid',
		     VideoFilName
		     )
	p = subprocess.Popen(cmdstring, stdin=subprocess.PIPE, shell=False)
	for i in range(NbImages):
	    im = Image.fromarray(np.uint8(np.transpose(video[i])))
	    p.stdin.write(im.tobytes('jpeg','L'))
	    #p.communicate(im.tostring('jpeg','L'))
	p.stdin.close()
	return 1
