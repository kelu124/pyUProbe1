## A basic python framework to communicate with a ultrasound probe

Seems to work well with UProbe-1 Wireless Probe Ultrasound Scanner

* [Raw PCAP](/data/2017_03_01_193826.pcap) of the wireless traffic during acquisition

Basic acquisition while connected to the probe:

* [Listening to 5002](/pythonSDK/test5002.py) for data
* [Listening to 5003](/pythonSDK/test5003.py) for info

These tools create (via piping) the data files on which subsequent notebooks work on. (aka use _python test5002.py > 20170404-patates.data_ to get the data).

Some notebooks:

* [Understanding the headers](/20170410-CrackingHeaders.ipynb)
* [Getting data, and processing it in a video](/20170404-Crunching_Video.ipynb)
* [Creating a pseudo-valid DICOM with data](/20170411-DICOM.ipynb)
	




![](/uprobe1.jpg)


### Some loops ?

Before scan conversion:

![](/video/20170404-potatoes.gif)

### Others

Licensed under CC-BY-SA 4.0

(c) kelu124, 2017
