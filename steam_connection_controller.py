import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import sys
import ctypes
from pathlib import Path
import threading
import time
import psutil

class SteamConnectionController:
    def __init__(self, root):
        self.root = root
        self.root.title("Steam Connection Controller")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Steam executable file paths
        self.steam_paths = self.find_steam_paths()
        
        # Create GUI
        self.create_gui()
        
        # Check status at startup
        self.check_connection_status()
    
    def find_steam_paths(self):
        """Find Steam installation paths"""
        possible_paths = [
            "C:\\Program Files (x86)\\Steam\\steam.exe",
            "C:\\Program Files\\Steam\\steam.exe",
            "D:\\Steam\\steam.exe",
            "E:\\Steam\\steam.exe"
        ]
        
        steam_paths = []
        for path in possible_paths:
            if os.path.exists(path):
                steam_paths.append(path)
                # Add other important files from Steam folder
                steam_dir = os.path.dirname(path)
                webhelper_path = os.path.join(steam_dir, "bin", "cef", "cef.win7x64", "steamwebhelper.exe")
                if os.path.exists(webhelper_path):
                    steam_paths.append(webhelper_path)
        
        return steam_paths
    
    def create_gui(self):
        """Create GUI interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Steam Connection Controller", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Status indicator
        self.status_label = ttk.Label(main_frame, text="Checking status...", 
                                     font=("Arial", 12))
        self.status_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Status indicator frame
        status_frame = ttk.LabelFrame(main_frame, text="Connection Status", padding="10")
        status_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.connection_status = ttk.Label(status_frame, text="●", font=("Arial", 20))
        self.connection_status.grid(row=0, column=0, padx=(0, 10))
        
        self.connection_text = ttk.Label(status_frame, text="Checking...", 
                                        font=("Arial", 11))
        self.connection_text.grid(row=0, column=1)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.block_button = ttk.Button(button_frame, text="Block Connection", 
                                      command=self.block_steam, width=15)
        self.block_button.grid(row=0, column=0, padx=(0, 10))
        
        self.unblock_button = ttk.Button(button_frame, text="Allow Connection", 
                                        command=self.unblock_steam, width=15)
        self.unblock_button.grid(row=0, column=1, padx=(10, 0))
        
        # Refresh button
        refresh_button = ttk.Button(main_frame, text="Refresh Status", 
                                   command=self.check_connection_status)
        refresh_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Steam paths info
        info_frame = ttk.LabelFrame(main_frame, text="Steam Information", padding="10")
        info_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        if self.steam_paths:
            info_text = f"Found Steam files: {len(self.steam_paths)}"
        else:
            info_text = "Steam not found!"
        
        ttk.Label(info_frame, text=info_text, font=("Arial", 9)).grid(row=0, column=0)
    
    def is_admin(self):
        """Check administrator privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def run_as_admin(self):
        """Run program as administrator"""
        if self.is_admin():
            return True
        else:
            messagebox.showwarning("Administrator Rights Required", 
                                 "This operation requires administrator privileges.\n"
                                 "The program will restart as administrator.")
            try:
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                self.root.quit()
                return False
            except:
                messagebox.showerror("Error", "Could not obtain administrator privileges!")
                return False
    
    def execute_firewall_command(self, command):
        """Execute firewall command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def is_steam_running(self):
        """Check if Steam is running"""
        try:
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] and 'steam.exe' in process.info['name'].lower():
                    return True
            return False
        except Exception:
            return False
    
    def close_steam(self):
        """Close Steam"""
        try:
            # Close Steam gracefully
            subprocess.run("taskkill /im steam.exe /t", shell=True, capture_output=True)
            time.sleep(2)  # Wait for Steam to close
            
            # Force close if still running
            if self.is_steam_running():
                subprocess.run("taskkill /f /im steam.exe /t", shell=True, capture_output=True)
                time.sleep(1)
            
            # Close other Steam-related processes
            steam_processes = ['steamwebhelper.exe', 'steamservice.exe', 'steam.exe']
            for process_name in steam_processes:
                subprocess.run(f"taskkill /f /im {process_name} /t", shell=True, capture_output=True)
            
            time.sleep(2)  # Wait for all processes to close
            return True
        except Exception as e:
            print(f"Steam closing error: {e}")
            return False
    
    def start_steam(self):
        """Start Steam"""
        try:
            if self.steam_paths:
                # Use the first found Steam path
                steam_exe = self.steam_paths[0]
                subprocess.Popen([steam_exe], shell=True)
                return True
            return False
        except Exception as e:
            print(f"Steam starting error: {e}")
            return False
    
    def block_steam(self):
        """Block Steam"""
        if not self.run_as_admin():
            return
        
        if not self.steam_paths:
            messagebox.showerror("Error", "Steam not found!")
            return
        
        # Notify user that Steam will be closed
        if self.is_steam_running():
            result = messagebox.askyesno("Steam Will Be Closed", 
                                       "Steam is currently running. To block the connection, Steam will be closed and then restarted.\n\n"
                                       "Do you want to continue?")
            if not result:
                return
        
        self.status_label.config(text="Closing Steam and blocking connection...")
        self.root.update()
        
        def block_thread():
            steam_was_running = self.is_steam_running()
            
            # 1. Close Steam
            if steam_was_running:
                self.root.after(0, lambda: self.status_label.config(text="Closing Steam..."))
                self.close_steam()
            
            # 2. Create firewall rules
            self.root.after(0, lambda: self.status_label.config(text="Creating firewall rules..."))
            success_count = 0
            for steam_path in self.steam_paths:
                # Block outbound connections
                cmd_out = f'netsh advfirewall firewall add rule name="Block Steam Out - {os.path.basename(steam_path)}" dir=out action=block program="{steam_path}"'
                success_out, _, _ = self.execute_firewall_command(cmd_out)
                
                # Block inbound connections
                cmd_in = f'netsh advfirewall firewall add rule name="Block Steam In - {os.path.basename(steam_path)}" dir=in action=block program="{steam_path}"'
                success_in, _, _ = self.execute_firewall_command(cmd_in)
                
                if success_out and success_in:
                    success_count += 1
            
            # 3. Restart Steam (if it was running)
            if steam_was_running and success_count > 0:
                self.root.after(0, lambda: self.status_label.config(text="Restarting Steam..."))
                time.sleep(1)
                self.start_steam()
            
            self.root.after(0, lambda: self.block_complete(success_count, steam_was_running))
        
        threading.Thread(target=block_thread, daemon=True).start()
    
    def block_complete(self, success_count, steam_was_running=False):
        """Blocking operation completed"""
        if success_count > 0:
            restart_msg = "\nSteam has been restarted." if steam_was_running else ""
            messagebox.showinfo("Success", f"Steam connection blocked!\n"
                                          f"Rules created for {success_count} files.{restart_msg}")
        else:
            messagebox.showerror("Error", "Could not block Steam!")
        
        self.check_connection_status()
    
    def unblock_steam(self):
        """Remove Steam block"""
        if not self.run_as_admin():
            return
        
        # Notify user that Steam will be closed
        if self.is_steam_running():
            result = messagebox.askyesno("Steam Will Be Closed", 
                                       "Steam is currently running. To allow the connection, Steam will be closed and then restarted.\n\n"
                                       "Do you want to continue?")
            if not result:
                return
        
        self.status_label.config(text="Closing Steam and allowing connection...")
        self.root.update()
        
        def unblock_thread():
            steam_was_running = self.is_steam_running()
            
            # 1. Close Steam
            if steam_was_running:
                self.root.after(0, lambda: self.status_label.config(text="Closing Steam..."))
                self.close_steam()
            
            # 2. Remove firewall rules
            self.root.after(0, lambda: self.status_label.config(text="Removing firewall rules..."))
            success_count = 0
            
            # Remove all Steam-related rules
            for steam_path in self.steam_paths:
                basename = os.path.basename(steam_path)
                
                # Remove outbound rules
                cmd_out = f'netsh advfirewall firewall delete rule name="Block Steam Out - {basename}"'
                success_out, _, _ = self.execute_firewall_command(cmd_out)
                
                # Remove inbound rules
                cmd_in = f'netsh advfirewall firewall delete rule name="Block Steam In - {basename}"'
                success_in, _, _ = self.execute_firewall_command(cmd_in)
                
                if success_out or success_in:
                    success_count += 1
            
            # 3. Restart Steam (if it was running)
            if steam_was_running:
                self.root.after(0, lambda: self.status_label.config(text="Restarting Steam..."))
                time.sleep(1)
                self.start_steam()
            
            self.root.after(0, lambda: self.unblock_complete(success_count, steam_was_running))
        
        threading.Thread(target=unblock_thread, daemon=True).start()
    
    def unblock_complete(self, success_count, steam_was_running=False):
        """Unblocking operation completed"""
        if success_count > 0:
            restart_msg = "\nSteam has been restarted." if steam_was_running else ""
            messagebox.showinfo("Success", f"Steam connection allowed!\n"
                                          f"Rules removed for {success_count} files.{restart_msg}")
        else:
            messagebox.showinfo("Info", "No rules found to remove.")
        
        self.check_connection_status()
    
    def check_connection_status(self):
        """Check connection status"""
        def check_thread():
            blocked_count = 0
            
            for steam_path in self.steam_paths:
                basename = os.path.basename(steam_path)
                
                # Check outbound rules
                cmd = f'netsh advfirewall firewall show rule name="Block Steam Out - {basename}"'
                success, output, _ = self.execute_firewall_command(cmd)
                
                if success and "Block Steam Out" in output:
                    blocked_count += 1
                    break
            
            self.root.after(0, lambda: self.update_status(blocked_count > 0))
        
        threading.Thread(target=check_thread, daemon=True).start()
    
    def update_status(self, is_blocked):
        """Update status indicator"""
        if is_blocked:
            self.connection_status.config(text="●", foreground="red")
            self.connection_text.config(text="Connection Blocked")
            self.status_label.config(text="Steam's internet connection is blocked")
        else:
            self.connection_status.config(text="●", foreground="green")
            self.connection_text.config(text="Connection Allowed")
            self.status_label.config(text="Steam's internet connection is allowed")

def main():
    root = tk.Tk()
    app = SteamConnectionController(root)
    root.mainloop()

if __name__ == "__main__":
    main()