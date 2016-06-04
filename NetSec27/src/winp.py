from winpcapy import WinPcapUtils
# run on the first Ethernert interface and print a log for each packet
WinPcapUtils.capture_on_and_print("*Ethernet*")
