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

class GameClientConnectionController: # Sınıf adı değiştirildi
    def __init__(self, root):
        self.root = root
        self.root.title("Game Client Connection Controller")
        self.root.geometry("550x440") # Rockstar için biraz daha genişletildi
        self.root.resizable(False, False)
        
        # Client executable file paths
        self.steam_paths = self.find_client_paths_steam() # Fonksiyon çağrısı güncellendi
        self.ubisoft_paths = self.find_ubisoft_paths()
        self.ea_paths = self.find_ea_paths()
        self.rockstar_paths = self.find_rockstar_paths() # Rockstar yolları eklendi
        
        self.selected_client = tk.StringVar(value="Steam") # Varsayılan istemci
        
        # Create GUI
        self.create_gui()
        
        # Check status at startup
        self.check_connection_status()
    
    def find_client_paths_steam(self): # Fonksiyon adı daha spesifik hale getirildi
        """Find Steam client installation paths"""
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
    
    def find_ubisoft_paths(self):
        """Find Ubisoft Connect installation paths and all relevant executables."""
        # Common main executables to locate the installation directory
        main_launcher_executables = [
            "upc.exe",
            "UbisoftGameLauncher.exe",
            "UbisoftConnect.exe"
        ]
        # Common installation directory roots
        possible_dir_roots = [
            "C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher",
            "C:\\Program Files\\Ubisoft\\Ubisoft Game Launcher",
            "D:\\Ubisoft Game Launcher",
            "E:\\Ubisoft Game Launcher"
        ]

        ubisoft_paths = []
        found_launcher_dir = None

        # Try to find the launcher directory
        for dir_root in possible_dir_roots:
            if os.path.isdir(dir_root):
                for main_exe in main_launcher_executables:
                    if os.path.exists(os.path.join(dir_root, main_exe)):
                        found_launcher_dir = dir_root
                        break
            if found_launcher_dir:
                break
        
        # If a launcher directory is found, scan for all known executables
        if found_launcher_dir:
            known_ubisoft_exes = [
                "upc.exe", "UbisoftGameLauncher.exe", "UbisoftConnect.exe",
                "UbisoftGameLauncher64.exe", "UbisoftExtension.exe",
                "UpcElevationService.exe", "UplayCrashReporter.exe",
                "UplayService.exe", "UplayWebCore.exe",
                "UbisoftGameLauncherService.exe", # Explicitly add service
                # "Uninstall.exe" # Genellikle engellenmesi gerekmeyen bir dosya
            ]
            for exe_name in known_ubisoft_exes:
                exe_path = os.path.join(found_launcher_dir, exe_name)
                if os.path.exists(exe_path) and exe_path not in ubisoft_paths:
                    ubisoft_paths.append(exe_path)
            
            # Fallback: if no specific exes found but dir exists, add the initially found main exe
            if not ubisoft_paths:
                 for main_exe in main_launcher_executables:
                    exe_path = os.path.join(found_launcher_dir, main_exe)
                    if os.path.exists(exe_path):
                        ubisoft_paths.append(exe_path)
                        # Add service if main exe is found this way too
                        service_exe_path = os.path.join(found_launcher_dir, "UbisoftGameLauncherService.exe")
                        if os.path.exists(service_exe_path) and service_exe_path not in ubisoft_paths:
                             ubisoft_paths.append(service_exe_path)
                        break # Add first found main exe

        # If directory not found via common roots, try the old method as a last resort
        if not ubisoft_paths:
            legacy_possible_paths = [
                "C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\upc.exe",
                "C:\\Program Files\\Ubisoft\\Ubisoft Game Launcher\\upc.exe",
                "D:\\Ubisoft Game Launcher\\upc.exe",
                "E:\\Ubisoft Game Launcher\\upc.exe",
                "C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\UbisoftGameLauncher.exe",
                "C:\\Program Files\\Ubisoft\\Ubisoft Game Launcher\\UbisoftGameLauncher.exe",
            ]
            for path in legacy_possible_paths:
                if os.path.exists(path):
                    if path not in ubisoft_paths:
                        ubisoft_paths.append(path)
                    launcher_dir = os.path.dirname(path)
                    helper_exe = os.path.join(launcher_dir, "UbisoftGameLauncherService.exe")
                    if os.path.exists(helper_exe) and helper_exe not in ubisoft_paths:
                        ubisoft_paths.append(helper_exe)
        
        return list(set(ubisoft_paths)) # Remove duplicates

    def find_ea_paths(self):
        """Find EA Desktop (EA Play) installation paths and all relevant executables."""
        main_launcher_executables = [
            "EADesktop.exe",
            "EALauncher.exe"
        ]
        possible_dir_roots = [
            "C:\\Program Files\\Electronic Arts\\EA Desktop\\EA Desktop",
            "C:\\Program Files (x86)\\Electronic Arts\\EA Desktop\\EA Desktop",
            "D:\\EA Games\\EA Desktop", # Örnek ek sürücü yolları
            "E:\\EA Games\\EA Desktop"
        ]

        ea_paths = []
        found_launcher_dir = None

        for dir_root in possible_dir_roots:
            if os.path.isdir(dir_root):
                for main_exe in main_launcher_executables:
                    if os.path.exists(os.path.join(dir_root, main_exe)):
                        found_launcher_dir = dir_root
                        break
            if found_launcher_dir:
                break
        
        if found_launcher_dir:
            known_ea_exes = [
                "EADesktop.exe", "EABackgroundService.exe", "EALauncher.exe",
                "EAConnect_microsoft.exe", "EACrashReporter.exe", "EAUpdater.exe",
                "EALocalHostSvc.exe", "EAGEP.exe", "EACefSubProcess.exe",
                "IGOProxy32.exe", "Link2EA.exe", "ErrorReporter.exe",
                "EAUninstall.exe", "GetGameToken32.exe", "GetGameToken64.exe",
                "OriginLegacyCompatibility.exe" # Eski Origin uyumluluğu için
            ]
            for exe_name in known_ea_exes:
                exe_path = os.path.join(found_launcher_dir, exe_name)
                if os.path.exists(exe_path) and exe_path not in ea_paths:
                    ea_paths.append(exe_path)
            
            if not ea_paths: # Fallback
                 for main_exe in main_launcher_executables:
                    exe_path = os.path.join(found_launcher_dir, main_exe)
                    if os.path.exists(exe_path):
                        ea_paths.append(exe_path)
                        # Servisleri de ekleyebiliriz
                        service_exe_path = os.path.join(found_launcher_dir, "EABackgroundService.exe")
                        if os.path.exists(service_exe_path) and service_exe_path not in ea_paths:
                             ea_paths.append(service_exe_path)
                        break
        return list(set(ea_paths))

    def find_rockstar_paths(self):
        """Find Rockstar Games Launcher installation paths and relevant executables."""
        main_launcher_executables = [
            "Launcher.exe",
            "LauncherPatcher.exe"
        ]
        possible_dir_roots = [
            "C:\\Program Files\\Rockstar Games\\Launcher",
            "C:\\Program Files (x86)\\Rockstar Games\\Launcher",
            "D:\\Rockstar Games\\Launcher", # Örnek ek sürücü yolları
            "E:\\Rockstar Games\\Launcher"
        ]

        rockstar_paths = []
        found_launcher_dir = None

        for dir_root in possible_dir_roots:
            if os.path.isdir(dir_root):
                for main_exe in main_launcher_executables:
                    if os.path.exists(os.path.join(dir_root, main_exe)):
                        found_launcher_dir = dir_root
                        break
            if found_launcher_dir:
                break
        
        if found_launcher_dir:
            known_rockstar_exes = [
                "Launcher.exe", "LauncherPatcher.exe", "RockstarService.exe",
                "RockstarSteamHelper.exe", 
                "uninstall.exe" # Genellikle engellenmez ama listede bulunsun
            ]
            for exe_name in known_rockstar_exes:
                exe_path = os.path.join(found_launcher_dir, exe_name)
                if os.path.exists(exe_path) and exe_path not in rockstar_paths:
                    rockstar_paths.append(exe_path)
            
            if not rockstar_paths: # Fallback
                 for main_exe in main_launcher_executables:
                    exe_path = os.path.join(found_launcher_dir, main_exe)
                    if os.path.exists(exe_path):
                        rockstar_paths.append(exe_path)
                        service_exe_path = os.path.join(found_launcher_dir, "RockstarService.exe")
                        if os.path.exists(service_exe_path) and service_exe_path not in rockstar_paths:
                             rockstar_paths.append(service_exe_path)
                        break
        return list(set(rockstar_paths))


    def create_gui(self):
        """Create GUI interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Game Client Connection Controller", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 10)) # columnspan 4 oldu

        # Client selection
        client_frame = ttk.LabelFrame(main_frame, text="Select Client", padding="10")
        client_frame.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0,10)) # columnspan 4 oldu
        
        steam_radio = ttk.Radiobutton(client_frame, text="Steam", variable=self.selected_client, 
                                      value="Steam", command=self.on_client_change)
        steam_radio.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        
        ubisoft_radio = ttk.Radiobutton(client_frame, text="Ubisoft Connect", variable=self.selected_client, 
                                        value="Ubisoft", command=self.on_client_change)
        ubisoft_radio.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ea_radio = ttk.Radiobutton(client_frame, text="EA Play", variable=self.selected_client,
                                   value="EA", command=self.on_client_change)
        ea_radio.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        rockstar_radio = ttk.Radiobutton(client_frame, text="Rockstar", variable=self.selected_client,
                                   value="Rockstar", command=self.on_client_change) # Rockstar eklendi
        rockstar_radio.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)


        # Status indicator
        self.status_label = ttk.Label(main_frame, text="Checking status...", 
                                     font=("Arial", 12))
        self.status_label.grid(row=2, column=0, columnspan=2, pady=(0, 10)) # row indeksi güncellendi
        
        # Status indicator frame
        status_frame = ttk.LabelFrame(main_frame, text="Connection Status", padding="10")
        status_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10)) # row indeksi güncellendi
        
        self.connection_status = ttk.Label(status_frame, text="●", font=("Arial", 20))
        self.connection_status.grid(row=0, column=0, padx=(0, 10))
        
        self.connection_text = ttk.Label(status_frame, text="Checking...", 
                                        font=("Arial", 11))
        self.connection_text.grid(row=0, column=1)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10) # row indeksi güncellendi
        
        self.block_button = ttk.Button(button_frame, text="Block Connection", 
                                      command=self.block_client, width=15) # command güncellendi
        self.block_button.grid(row=0, column=0, padx=(0, 10))
        
        self.unblock_button = ttk.Button(button_frame, text="Allow Connection", 
                                        command=self.unblock_client, width=15) # command güncellendi
        self.unblock_button.grid(row=0, column=1, padx=(10, 0))
        
        # Refresh button
        refresh_button = ttk.Button(main_frame, text="Refresh Status", 
                                   command=self.check_connection_status)
        refresh_button.grid(row=5, column=0, columnspan=2, pady=10) # row indeksi güncellendi
        
        # Client paths info
        self.info_frame = ttk.LabelFrame(main_frame, text="Client Information", padding="10") # text güncellendi
        self.info_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0)) # row indeksi güncellendi
        
        self.update_client_info_display() # Bilgi ekranını güncellemek için yeni fonksiyon

    def update_client_info_display(self):
        """Update the client information display based on selection"""
        for widget in self.info_frame.winfo_children():
            widget.destroy() # Önceki bilgileri temizle

        client_name = self.selected_client.get()
        paths_to_check = []
        if client_name == "Steam":
            paths_to_check = self.steam_paths
            info_text_label = "Steam"
        elif client_name == "Ubisoft":
            paths_to_check = self.ubisoft_paths
            info_text_label = "Ubisoft Connect"
        elif client_name == "EA":
            paths_to_check = self.ea_paths
            info_text_label = "EA Play (EA Desktop)"
        elif client_name == "Rockstar": # Rockstar eklendi
            paths_to_check = self.rockstar_paths
            info_text_label = "Rockstar Launcher"
        
        if paths_to_check:
            info_text = f"Found {info_text_label} files: {len(paths_to_check)}"
        else:
            info_text = f"{info_text_label} not found!"
        
        ttk.Label(self.info_frame, text=info_text, font=("Arial", 9)).grid(row=0, column=0)

    def on_client_change(self):
        """Handle client selection change"""
        self.update_client_info_display()
        self.check_connection_status() # İstemci değiştiğinde durumu yeniden kontrol et

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
    
    # is_steam_running, close_steam, start_steam metodları kaldırıldı çünkü yerlerine
    # is_client_running, close_client, start_client genel metodları geldi.

    def block_client(self):
        """Block Selected Client"""
        if not self.run_as_admin():
            return

        client_name = self.selected_client.get()
        client_paths = []
        primary_process_names = []

        if client_name == "Steam":
            client_paths = self.steam_paths
            primary_process_names = ["steam.exe"]
        elif client_name == "Ubisoft":
            client_paths = self.ubisoft_paths
            primary_process_names = ["upc.exe", "UbisoftGameLauncher.exe", "UbisoftConnect.exe", "UbisoftGameLauncher64.exe"]
        elif client_name == "EA":
            client_paths = self.ea_paths
            primary_process_names = ["EADesktop.exe", "EALauncher.exe", "EABackgroundService.exe"]
        elif client_name == "Rockstar": # Rockstar eklendi
            client_paths = self.rockstar_paths
            primary_process_names = ["Launcher.exe", "LauncherPatcher.exe", "RockstarService.exe"]
        
        if not client_paths:
            messagebox.showerror("Error", f"{client_name} not found!")
            return
        
        # Notify user that Client will be closed
        if self.is_client_running(primary_process_names): # primary_process_names listesi ile kontrol
            result = messagebox.askyesno(f"{client_name} Will Be Closed", 
                                       f"{client_name} is currently running. To block the connection, {client_name} will be closed and then restarted.\n\n"
                                       "Do you want to continue?")
            if not result:
                return
        
        self.status_label.config(text=f"Closing {client_name} and blocking connection...")
        self.root.update()
        
        def block_thread():
            client_was_running = self.is_client_running(primary_process_names) # primary_process_names listesi ile kontrol
            
            # 1. Close Client
            if client_was_running:
                self.root.after(0, lambda: self.status_label.config(text=f"Closing {client_name}..."))
                self.close_client(client_name, primary_process_names) # primary_process_names listesi ile kapatma
            
            # 2. Create firewall rules
            self.root.after(0, lambda: self.status_label.config(text="Creating firewall rules..."))
            success_count = 0
            for client_path_item in client_paths:
                rule_name_out_prefix = f"Block {client_name} Out"
                rule_name_in_prefix = f"Block {client_name} In"
                if client_name == "Ubisoft": # Ubisoft için özel prefix kalabilir
                    rule_name_out_prefix = "Block Ubisoft Out"
                    rule_name_in_prefix = "Block Ubisoft In"
                elif client_name == "EA":
                    rule_name_out_prefix = "Block EA Out"
                    rule_name_in_prefix = "Block EA In"
                elif client_name == "Rockstar": # Rockstar eklendi
                    rule_name_out_prefix = "Block Rockstar Out"
                    rule_name_in_prefix = "Block Rockstar In"

                # Block outbound connections
                cmd_out = f'netsh advfirewall firewall add rule name="{rule_name_out_prefix} - {os.path.basename(client_path_item)}" dir=out action=block program="{client_path_item}"'
                success_out, _, _ = self.execute_firewall_command(cmd_out)
                
                # Block inbound connections
                cmd_in = f'netsh advfirewall firewall add rule name="{rule_name_in_prefix} - {os.path.basename(client_path_item)}" dir=in action=block program="{client_path_item}"'
                success_in, _, _ = self.execute_firewall_command(cmd_in)
                
                if success_out and success_in:
                    success_count += 1
            
            # 3. Restart Client (if it was running)
            if client_was_running and success_count > 0:
                self.root.after(0, lambda: self.status_label.config(text=f"Restarting {client_name}..."))
                time.sleep(1)
                self.start_client(client_name, client_paths)
            
            self.root.after(0, lambda: self.block_complete(success_count, client_was_running, client_name))
        
        threading.Thread(target=block_thread, daemon=True).start()
    
    def block_complete(self, success_count, client_was_running=False, client_name="Client"): # client_name eklendi
        """Blocking operation completed"""
        if success_count > 0:
            restart_msg = f"\n{client_name} has been restarted." if client_was_running else ""
            messagebox.showinfo("Success", f"{client_name} connection blocked!\n"
                                          f"Rules created for {success_count} files.{restart_msg}")
        else:
            messagebox.showerror("Error", f"Could not block {client_name}!")
        
        self.check_connection_status()
    
    def unblock_client(self): # unblock_steam -> unblock_client
        """Remove Selected Client block"""
        if not self.run_as_admin():
            return

        client_name = self.selected_client.get()
        client_paths = []
        primary_process_names = []

        if client_name == "Steam":
            client_paths = self.steam_paths
            primary_process_names = ["steam.exe"]
        elif client_name == "Ubisoft":
            client_paths = self.ubisoft_paths
            primary_process_names = ["upc.exe", "UbisoftGameLauncher.exe", "UbisoftConnect.exe", "UbisoftGameLauncher64.exe"]
        elif client_name == "EA":
            client_paths = self.ea_paths
            primary_process_names = ["EADesktop.exe", "EALauncher.exe", "EABackgroundService.exe"]
        elif client_name == "Rockstar": # Rockstar eklendi
            client_paths = self.rockstar_paths
            primary_process_names = ["Launcher.exe", "LauncherPatcher.exe", "RockstarService.exe"]
        
        if not client_paths: 
            messagebox.showerror("Error", f"{client_name} not found!")
            return

        # Notify user that Client will be closed
        if self.is_client_running(primary_process_names): # primary_process_names listesi ile kontrol
            result = messagebox.askyesno(f"{client_name} Will Be Closed", 
                                       f"{client_name} is currently running. To allow the connection, {client_name} will be closed and then restarted.\n\n"
                                       "Do you want to continue?")
            if not result:
                return
        
        self.status_label.config(text=f"Closing {client_name} and allowing connection...")
        self.root.update()
        
        def unblock_thread():
            client_was_running = self.is_client_running(primary_process_names) # primary_process_names listesi ile kontrol
            
            # 1. Close Client
            if client_was_running:
                self.root.after(0, lambda: self.status_label.config(text=f"Closing {client_name}..."))
                self.close_client(client_name, primary_process_names) # primary_process_names listesi ile kapatma
            
            # 2. Remove firewall rules
            self.root.after(0, lambda: self.status_label.config(text="Removing firewall rules..."))
            success_count = 0
            
            # Remove all Client-related rules
            for client_path_item in client_paths:
                basename = os.path.basename(client_path_item)
                rule_name_out_prefix = f"Block {client_name} Out"
                rule_name_in_prefix = f"Block {client_name} In"
                if client_name == "Ubisoft":
                    rule_name_out_prefix = "Block Ubisoft Out"
                    rule_name_in_prefix = "Block Ubisoft In"
                elif client_name == "EA":
                    rule_name_out_prefix = "Block EA Out"
                    rule_name_in_prefix = "Block EA In"
                elif client_name == "Rockstar": # Rockstar eklendi
                    rule_name_out_prefix = "Block Rockstar Out"
                    rule_name_in_prefix = "Block Rockstar In"


                # Remove outbound rules
                cmd_out = f'netsh advfirewall firewall delete rule name="{rule_name_out_prefix} - {basename}"'
                success_out, _, _ = self.execute_firewall_command(cmd_out)
                
                # Remove inbound rules
                cmd_in = f'netsh advfirewall firewall delete rule name="{rule_name_in_prefix} - {basename}"'
                success_in, _, _ = self.execute_firewall_command(cmd_in)
                
                if success_out or success_in: 
                    success_count += 1 
            
            # 3. Restart Client (if it was running)
            if client_was_running: # Başarılı silme işlemine bakılmaksızın yeniden başlat
                self.root.after(0, lambda: self.status_label.config(text=f"Restarting {client_name}..."))
                time.sleep(1)
                self.start_client(client_name, client_paths)
            
            self.root.after(0, lambda: self.unblock_complete(success_count > 0, client_was_running, client_name)) # success_count > 0 olarak değiştirildi
        
        threading.Thread(target=unblock_thread, daemon=True).start()
    
    def unblock_complete(self, rules_were_removed, client_was_running=False, client_name="Client"): # success_count -> rules_were_removed
        """Unblocking operation completed"""
        if rules_were_removed:
            restart_msg = f"\n{client_name} has been restarted." if client_was_running else ""
            messagebox.showinfo("Success", f"{client_name} connection allowed!\n"
                                          f"Relevant firewall rules removed.{restart_msg}")
        else:
            messagebox.showinfo("Info", f"No active blocking rules found for {client_name} to remove.")
        
        self.check_connection_status()
    
    def is_client_running(self, primary_process_names_list):
        """Check if any of the specified client processes are running"""
        try:
            running_processes = {p.info['name'].lower() for p in psutil.process_iter(['name']) if p.info['name']}
            for proc_name in primary_process_names_list:
                if proc_name.lower() in running_processes:
                    return True
            return False
        except Exception as e:
            print(f"Error checking if client is running: {e}")
            return False

    def close_client(self, client_name, primary_process_names_list):
        """Close the specified client by trying to kill all its primary executables and related processes"""
        try:
            all_processes_to_kill = set(p.lower() for p in primary_process_names_list)

            related_processes = []
            if client_name == "Steam":
                related_processes = ['steamwebhelper.exe', 'steamservice.exe']
            elif client_name == "Ubisoft":
                related_processes = [
                    'UbisoftGameLauncherService.exe', 'UplayService.exe', 'UplayWebCore.exe',
                    'UbisoftExtension.exe', 'UpcElevationService.exe', 'UplayCrashReporter.exe'
                ]
            elif client_name == "EA":
                related_processes = [
                    'EABackgroundService.exe', 
                    'EAConnect_microsoft.exe', 'EACrashReporter.exe', 'EAUpdater.exe',
                    'EALocalHostSvc.exe', 'EAGEP.exe', 'EACefSubProcess.exe',
                    'IGOProxy32.exe', 'Link2EA.exe', 'ErrorReporter.exe'
                ]
            elif client_name == "Rockstar": # Rockstar eklendi
                related_processes = [
                    'RockstarService.exe', # Zaten primary'de olabilir
                    'RockstarSteamHelper.exe' 
                    # 'uninstall.exe' genellikle kapatılmaz
                ]

            for rp in related_processes:
                all_processes_to_kill.add(rp.lower())

            processes_closed_gracefully = False
            for proc_name in primary_process_names_list: # Önce ana işlemleri düzgün kapatmayı dene
                if self.is_client_running([proc_name]): # Tekil kontrol
                    print(f"Attempting graceful shutdown for {proc_name}...")
                    subprocess.run(f"taskkill /im {proc_name} /t", shell=True, capture_output=True, check=False)
                    processes_closed_gracefully = True
            
            if processes_closed_gracefully:
                time.sleep(3) # Düzgün kapanma için biraz bekle

            # Kalan tüm işlemleri (ana ve ilişkili) zorla kapat
            for proc_to_kill in all_processes_to_kill:
                # is_client_running'i burada kullanmak döngüye yol açabilir, doğrudan psutil ile kontrol et
                is_running_now = False
                try:
                    for process in psutil.process_iter(['pid', 'name']):
                        if process.info['name'] and proc_to_kill == process.info['name'].lower():
                            is_running_now = True
                            break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass # İşlem zaten yok veya erişilemiyor

                if is_running_now:
                    print(f"Attempting force shutdown for {proc_to_kill}...")
                    subprocess.run(f"taskkill /f /im {proc_to_kill} /t", shell=True, capture_output=True, check=False)
            
            time.sleep(2) # Tüm işlemlerin sonlandığından emin olmak için bekle
            return True
        except Exception as e:
            print(f"{client_name} closing error: {e}")
            return False

    def start_client(self, client_name, client_paths): # start_steam -> start_client
        """Start the specified client"""
        try:
            if client_paths:
                client_exe = client_paths[0] # Genellikle ilk bulunan ana çalıştırılabilir dosyadır
                subprocess.Popen([client_exe], shell=False) # shell=True'den False'a değiştirildi, daha güvenli.
                return True
            return False
        except Exception as e:
            print(f"{client_name} starting error: {e}")
            return False

    def check_connection_status(self):
        """Check connection status for the selected client"""
        client_name = self.selected_client.get()
        paths_to_check = []
        if client_name == "Steam":
            paths_to_check = self.steam_paths
        elif client_name == "Ubisoft":
            paths_to_check = self.ubisoft_paths
        elif client_name == "EA":
            paths_to_check = self.ea_paths
        elif client_name == "Rockstar": # Rockstar eklendi
            paths_to_check = self.rockstar_paths
        
        if not paths_to_check: 
            self.update_status(is_blocked=False, not_found=True, client_name_for_status=client_name)
            return

        def check_thread():
            blocked_count = 0
            rule_name_prefix = f"Block {client_name} Out"
            if client_name == "Ubisoft":
                 rule_name_prefix = "Block Ubisoft Out"
            elif client_name == "EA":
                 rule_name_prefix = "Block EA Out"
            elif client_name == "Rockstar": # Rockstar eklendi
                 rule_name_prefix = "Block Rockstar Out"
            
            for client_path_item in paths_to_check: 
                basename = os.path.basename(client_path_item)
                
                cmd = f'netsh advfirewall firewall show rule name="{rule_name_prefix} - {basename}"'
                success, output, _ = self.execute_firewall_command(cmd)
                
                if success and rule_name_prefix in output: # Kural adında prefix kontrolü
                    blocked_count += 1
                    break 
            
            self.root.after(0, lambda: self.update_status(blocked_count > 0, client_name_for_status=client_name))
        
        threading.Thread(target=check_thread, daemon=True).start()
    
    def update_status(self, is_blocked, not_found=False, client_name_for_status="Client"): # client_name_for_status eklendi
        """Update status indicator"""
        if not_found:
            self.connection_status.config(text="!", foreground="orange")
            self.connection_text.config(text=f"{client_name_for_status} Not Found")
            self.status_label.config(text=f"{client_name_for_status} installation not detected.")
        elif is_blocked:
            self.connection_status.config(text="●", foreground="red")
            self.connection_text.config(text="Connection Blocked")
            self.status_label.config(text=f"{client_name_for_status}'s internet connection is blocked")
        else:
            self.connection_status.config(text="●", foreground="green")
            self.connection_text.config(text="Connection Allowed")
            self.status_label.config(text=f"{client_name_for_status}'s internet connection is allowed")

def main():
    root = tk.Tk()
    app = GameClientConnectionController(root) # Sınıf adı güncellendi
    root.mainloop()

if __name__ == "__main__":
    main()
