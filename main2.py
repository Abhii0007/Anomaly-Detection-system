from threading import Thread
from scapy.all import sniff, IP, TCP
from collections import defaultdict
import socket
import time
import threading
import ctypes
import time

# Define constants for window states
SW_MINIMIZE = 6

# Find the handle of the console window
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# Minimize the window using ShowWindow
ctypes.windll.user32.ShowWindow(hwnd, SW_MINIMIZE)


class IntrusionDetectionSystem:
    def __init__(self, interface="Wi-Fi", port=80):
        self.PORT_SCAN_THRESHOLD = 10  # Number of ports accessed in a short time for port scan detection
        self.SYN_FLOOD_THRESHOLD = 100
        self.interface = interface
        self.MONITOR_PORT = port
        self.detected = False
        self.suspicious_ips = defaultdict(list)
        self.port_access_count = defaultdict(set)
        self.syn_packet_count = defaultdict(int)
    
    def get_current_ip(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
        except Exception:
            return "No Network"
    
    def analyze_packet(self, packet):
        global main_window3
        if self.detected:
            return
        
        monitor_ip = self.get_current_ip()
        if packet.haslayer(IP) and packet.haslayer(TCP):
            ip_src = packet[IP].src
            dport = packet[TCP].dport
            tcp_flags = packet[TCP].flags
            
            if tcp_flags == "S":  # SYN packet
                self.syn_packet_count[ip_src] += 1
                if self.syn_packet_count[ip_src] > 100:
                    print(f"[ALERT] Possible SYN Flood detected from IP: {ip_src}")
                    main_window3.form.textEdit.setStyleSheet("color: rgb(255, 0,0);background-color: rgba(0, 0, 0,0.5);")
                    main_window3.form.textEdit.insertPlainText(f"[ALERT] Possible SYN Flood detected from IP: {ip_src}")

                    self.suspicious_ips[ip_src].append("Possible SYN Flood")
                    self.detected = True

            
                self.port_access_count[ip_src].add(dport)
                if len(self.port_access_count[ip_src]) > 10:
                    print(f"[ALERT] Possible Port Scan detected from IP: {ip_src}")
                    
                    main_window3.form.textEdit.insertPlainText(f"[ALERT] Possible Port Scan detected from IP: {ip_src}")

                    self.suspicious_ips[ip_src].append("Possible Port Scan")
            
            if ip_src == monitor_ip or dport == self.MONITOR_PORT:
                            
                
                main_window3.form.textEdit.insertPlainText(f"[ALERT] Traffic involving monitored IP/Port detected!\n")
                
                print(f"[ALERT] Traffic involving monitored IP/Port detected!")

    def reset_counts(self):
        while not self.detected:
            time.sleep(2)
            self.port_access_count.clear()
            self.syn_packet_count.clear()
            print("Counters reset")
            

            main_window3.form.textEdit.insertPlainText(f"Counters reset\n")
    
    def start_sniffing(self):
        print("Starting IDS...")
        sniff(iface=self.interface, prn=self.analyze_packet, store=False)
    
    def run(self):
        Thread(target=self.reset_counts, daemon=True).start()
        self.start_sniffing()


    def display_suspicious_ips(update_gui_callback):
        global detected
        while not detected:
            time.sleep(2)
            if update_gui_callback.suspicious_ips:
                alert_message = "\nSuspicious IPs and Activities Detected:\n"
                main_window3.form.textEdit.setStyleSheet("color: rgb(255, 0,0);background-color: rgba(0, 0, 0,0.5);")
                main_window3.form.textEdit.insertPlainText(f"\nSuspicious IPs and Activities Detected:\n")


                for ip, activities in update_gui_callback.suspicious_ips.items():
                    alert_message += f"IP: {ip} - Activities: {', '.join(activities)}\n"
                detected = True
                update_gui_callback(alert_message)
                break
            else:
                update_gui_callback("No suspicious activity detected.")
                main_window3.form.textEdit.setStyleSheet("color: rgb(0, 255,0);background-color: rgba(0, 0, 0,0.5);")
                main_window3.form.textEdit.insertPlainText(f"No suspicious activity detected.")


            time.sleep(10)


    
    def start_ids(interface, update_gui_callback):
        sniff(iface=interface, prn=interface.analyze_packet, store=False)
        display_thread = threading.Thread(
            target=interface.display_suspicious_ips, args=(update_gui_callback,), daemon=True
        )
        display_thread.start()










import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from threading import Thread

# Replace with your PySide6 UI file's class
from window3 import Ui_Form3  

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_Form3()
        self.form.setupUi(self)

        # Initialize and start IDS in a separate thread
        self.ids = IntrusionDetectionSystem(interface="Wi-Fi", port=80)
        self.ids_thread = Thread(target=self.ids.run, daemon=True)
        self.ids_thread.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window3 = MainWindow()
    main_window3.show()
    sys.exit(app.exec())
