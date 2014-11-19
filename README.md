NetCaPy
--------------------------------------------------------------------------------------------
A **ScaPy** and **PyQt** based network packet capturing and analysis tool

Requirements
--------------------------------------------------------------------------------------------
* Python 2.x
* ScaPy
* PyQt4
* Netifaces
* MatPlotLib

Install
--------------------------------------------------------------------------------------------
* Make sure all the installation requirements have been fulfilled. Due to incomplete setup file, the requirements may not be installed automatically
* Install using the command

	**# python setup.py install**

Uninstall
--------------------------------------------------------------------------------------------
* There is no automatic installation instruction available. Therefore, all files need to be deleted manually.
* Follow the following steps:
	* Install once again, and note the files which have been changed

		**# sudo python setup.py install --record files.txt**
	* All the files created are now listed in **files.txt**. Delete them using the following command
	
		**xargs rm -rf < files.txt**

Features
--------------------------------------------------------------------------------------------
* Capture packets by selecting the active interface to listen on OR load packets from an existing pcap file
* Apply BPF Filter on the packets
* Analyse the packets using various other tools
    * Graphical analysis using matplotlib
    * Individual packet analysis by observing its summary or Layer based detail
* Save packets into a pcap file for future use

Documentation
--------------------------------------------------------------------------------------------
* -

Future Work
--------------------------------------------------------------------------------------------
* -

More Info
--------------------------------------------------------------------------------------------
* -