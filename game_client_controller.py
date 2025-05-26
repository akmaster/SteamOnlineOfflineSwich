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

class GameClientConnectionController: # Class name was changed
    def __init__(self, root):
        self.root = root
        self.root.title("Game Client Connection Controller")
        self.root.geometry("650x440") # Expanded for Epic Games
        self.root.resizable(False, False)
        
        # Client executable file paths
        self.steam_paths = self.find_client_paths_steam() # Function call updated
        self.ubisoft_paths = self.find_ubisoft_paths()
        self.ea_paths = self.find_ea_paths()
        self.rockstar_paths = self.find_rockstar_paths() # Rockstar paths added
        self.epic_paths = self.find_epic_paths() # Epic Games paths added
        
        self.selected_client = tk.StringVar(value="Steam") # Default client
        
        # Create GUI
        self.create_gui()
        
        # Check status at startup
        self.check_connection_status()
    
    def find_client_paths_steam(self): # Function name made more specific
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
                # "Uninstall.exe" # Usually not a file to block
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
            "D:\\EA Games\\EA Desktop", # Example additional drive paths
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
                "OriginLegacyCompatibility.exe" # For old Origin compatibility
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
                        # We can also add services
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
            "D:\\Rockstar Games\\Launcher", # Example additional drive paths
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
                "uninstall.exe" # Usually not blocked but let it be in the list
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

    def find_epic_paths(self):
        """Find Epic Games Launcher installation paths and relevant executables."""
        main_launcher_executables = [
            "EpicGamesLauncher.exe"
        ]
        # Epic Games is usually installed under Program Files (x86)
        possible_dir_roots = [
            "C:\\Program Files (x86)\\Epic Games\\Launcher",
            "C:\\Program Files\\Epic Games\\Launcher", # Can be checked rarely
            "D:\\Epic Games\\Launcher", # Example additional drive paths
            "E:\\Epic Games\\Launcher"
        ]

        epic_paths = []
        found_launcher_portal_dir = None

        for dir_root in possible_dir_roots:
            if os.path.isdir(dir_root):
                # Epic Games Launcher main .exe file is usually under "Portal/Binaries/Win64" or "Portal/Binaries/Win32".
                portal_subdirs = [
                    os.path.join(dir_root, "Portal", "Binaries", "Win64"),
                    os.path.join(dir_root, "Portal", "Binaries", "Win32")
                ]
                for portal_dir in portal_subdirs:
                    if os.path.isdir(portal_dir):
                        for main_exe in main_launcher_executables:
                            if os.path.exists(os.path.join(portal_dir, main_exe)):
                                found_launcher_portal_dir = portal_dir
                                break
                    if found_launcher_portal_dir:
                        break
            if found_launcher_portal_dir:
                break
        
        if found_launcher_portal_dir:
            known_epic_exes = [
                "EpicGamesLauncher.exe", 
                "EpicWebHelper.exe", # Usually found in the same directory
                # "CrashReportClient.exe" # This is usually under Engine, may not be a direct part of Launcher.
                # "UnrealCEFSubProcess.exe" # This also usually comes with Engine.
            ]
            for exe_name in known_epic_exes:
                exe_path = os.path.join(found_launcher_portal_dir, exe_name)
                if os.path.exists(exe_path) and exe_path not in epic_paths:
                    epic_paths.append(exe_path)
            
            # Epic Games services (e.g., EpicOnlineServices) might be in a different location
            # Like "C:\Program Files (x86)\Epic Games\Epic Online Services\EpicOnlineServicesHost.exe"
            # For now, we focus only on the main launcher and web helper.
            # This part can be expanded if necessary.

            # Fallback: If the specific exes above are not found but the main directory was found, add only the main exe
            if not epic_paths:
                 for main_exe in main_launcher_executables:
                    exe_path = os.path.join(found_launcher_portal_dir, main_exe)
                    if os.path.exists(exe_path):
                        epic_paths.append(exe_path)
                        break
        
        return list(set(epic_paths))


    def create_gui(self):
        """Create GUI interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Game Client Connection Controller", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=5, pady=(0, 10)) # columnspan became 5

        # Client selection
        client_frame = ttk.LabelFrame(main_frame, text="Select Client", padding="10")
        client_frame.grid(row=1, column=0, columnspan=5, sticky=(tk.W, tk.E), pady=(0,10)) # columnspan became 5
        
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
                                   value="Rockstar", command=self.on_client_change) 
        rockstar_radio.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        epic_radio = ttk.Radiobutton(client_frame, text="Epic Games", variable=self.selected_client,
                                   value="Epic", command=self.on_client_change) # Epic Games added
        epic_radio.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)


        # Status indicator
        self.status_label = ttk.Label(main_frame, text="Checking status...", 
                                     font=("Arial", 12))
        self.status_label.grid(row=2, column=0, columnspan=3, pady=(0, 10)) # columnspan updated
        
        # Status indicator frame
        status_frame = ttk.LabelFrame(main_frame, text="Connection Status", padding="10")
        status_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10)) # columnspan updated
        
        self.connection_status = ttk.Label(status_frame, text="●", font=("Arial", 20))
        self.connection_status.grid(row=0, column=0, padx=(0, 10))
        
        self.connection_text = ttk.Label(status_frame, text="Checking...", 
                                        font=("Arial", 11))
        self.connection_text.grid(row=0, column=1)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=10) # columnspan updated
        
        self.block_button = ttk.Button(button_frame, text="Block Connection", 
                                      command=self.block_client, width=15) 
        self.block_button.grid(row=0, column=0, padx=(0, 10))
        
        self.unblock_button = ttk.Button(button_frame, text="Allow Connection", 
                                        command=self.unblock_client, width=15) 
        self.unblock_button.grid(row=0, column=1, padx=(10, 0))
        
        # Refresh button
        refresh_button = ttk.Button(main_frame, text="Refresh Status", 
                                   command=self.check_connection_status)
        refresh_button.grid(row=5, column=0, columnspan=3, pady=10) # columnspan updated
        
        # Client paths info
        self.info_frame = ttk.LabelFrame(main_frame, text="Client Information", padding="10") 
        self.info_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0)) # columnspan updated
        
        self.update_client_info_display() 

    def update_client_info_display(self):
        """Update the client information display based on selection"""
        for widget in self.info_frame.winfo_children():
            widget.destroy() # Clear previous info

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
        elif client_name == "Rockstar": 
            paths_to_check = self.rockstar_paths
            info_text_label = "Rockstar Launcher"
        elif client_name == "Epic": # Epic Games added
            paths_to_check = self.epic_paths
            info_text_label = "Epic Games Launcher"
        
        if paths_to_check:
            info_text = f"Found {info_text_label} files: {len(paths_to_check)}"
        else:
            info_text = f"{info_text_label} not found!"
        
        ttk.Label(self.info_frame, text=info_text, font=("Arial", 9)).grid(row=0, column=0)

    def on_client_change(self):
        """Handle client selection change"""
        self.update_client_info_display()
        self.check_connection_status() # Recheck status when client changes

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
    
    # is_steam_running, close_steam, start_steam methods were removed as
    # generic is_client_running, close_client, start_client methods were added.

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
        elif client_name == "Rockstar": 
            client_paths = self.rockstar_paths
            primary_process_names = ["Launcher.exe", "LauncherPatcher.exe", "RockstarService.exe"]
        elif client_name == "Epic": # Epic Games added
            client_paths = self.epic_paths
            primary_process_names = ["EpicGamesLauncher.exe", "EpicWebHelper.exe"]
        
        if not client_paths:
            messagebox.showerror("Error", f"{client_name} not found!")
            return
        
        # Notify user that Client will be closed
        if self.is_client_running(primary_process_names): # Check with primary_process_names list
            result = messagebox.askyesno(f"{client_name} Will Be Closed", 
                                       f"{client_name} is currently running. To block the connection, {client_name} will be closed and then restarted.\n\n"
                                       "Do you want to continue?")
            if not result:
                return
        
        self.status_label.config(text=f"Closing {client_name} and blocking connection...")
        self.root.update()
        
        def block_thread():
            client_was_running = self.is_client_running(primary_process_names) # Check with primary_process_names list
            
            # 1. Close Client
            if client_was_running:
                self.root.after(0, lambda: self.status_label.config(text=f"Closing {client_name}..."))
                self.close_client(client_name, primary_process_names) # Close with primary_process_names list
            
            # 2. Create firewall rules
            self.root.after(0, lambda: self.status_label.config(text="Creating firewall rules..."))
            success_count = 0
            for client_path_item in client_paths:
                rule_name_out_prefix = f"Block {client_name} Out"
                rule_name_in_prefix = f"Block {client_name} In"
                if client_name == "Ubisoft": # Specific prefix for Ubisoft can remain
                    rule_name_out_prefix = "Block Ubisoft Out"
                    rule_name_in_prefix = "Block Ubisoft In"
                elif client_name == "EA":
                    rule_name_out_prefix = "Block EA Out"
                    rule_name_in_prefix = "Block EA In"
                elif client_name == "Rockstar": 
                    rule_name_out_prefix = "Block Rockstar Out"
                    rule_name_in_prefix = "Block Rockstar In"
                elif client_name == "Epic": # Epic Games added
                    rule_name_out_prefix = "Block Epic Out"
                    rule_name_in_prefix = "Block Epic In"

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
    
    def block_complete(self, success_count, client_was_running=False, client_name="Client"): # client_name added
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
        elif client_name == "Rockstar": 
            client_paths = self.rockstar_paths
            primary_process_names = ["Launcher.exe", "LauncherPatcher.exe", "RockstarService.exe"]
        elif client_name == "Epic": # Epic Games added
            client_paths = self.epic_paths
            primary_process_names = ["EpicGamesLauncher.exe", "EpicWebHelper.exe"]
        
        if not client_paths: 
            messagebox.showerror("Error", f"{client_name} not found!")
            return

        # Notify user that Client will be closed
        if self.is_client_running(primary_process_names): # Check with primary_process_names list
            result = messagebox.askyesno(f"{client_name} Will Be Closed", 
                                       f"{client_name} is currently running. To allow the connection, {client_name} will be closed and then restarted.\n\n"
                                       "Do you want to continue?")
            if not result:
                return
        
        self.status_label.config(text=f"Closing {client_name} and allowing connection...")
        self.root.update()
        
        def unblock_thread():
            client_was_running = self.is_client_running(primary_process_names) # Check with primary_process_names list
            
            # 1. Close Client
            if client_was_running:
                self.root.after(0, lambda: self.status_label.config(text=f"Closing {client_name}..."))
                self.close_client(client_name, primary_process_names) # Close with primary_process_names list
            
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
                elif client_name == "Rockstar": 
                    rule_name_out_prefix = "Block Rockstar Out"
                    rule_name_in_prefix = "Block Rockstar In"
                elif client_name == "Epic": # Epic Games added
                    rule_name_out_prefix = "Block Epic Out"
                    rule_name_in_prefix = "Block Epic In"

                # Remove outbound rules
                cmd_out = f'netsh advfirewall firewall delete rule name="{rule_name_out_prefix} - {basename}"'
                success_out, _, _ = self.execute_firewall_command(cmd_out)
                
                # Remove inbound rules
                cmd_in = f'netsh advfirewall firewall delete rule name="{rule_name_in_prefix} - {basename}"'
                success_in, _, _ = self.execute_firewall_command(cmd_in)
                
                if success_out or success_in: 
                    success_count += 1 
            
            # 3. Restart Client (if it was running)
            if client_was_running: # Restart regardless of successful deletion
                self.root.after(0, lambda: self.status_label.config(text=f"Restarting {client_name}..."))
                time.sleep(1)
                self.start_client(client_name, client_paths)
            
            self.root.after(0, lambda: self.unblock_complete(success_count > 0, client_was_running, client_name)) # Changed to success_count > 0
        
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
            elif client_name == "Rockstar": 
                related_processes = [
                    'RockstarService.exe', 
                    'RockstarSteamHelper.exe' 
                ]
            elif client_name == "Epic": # Epic Games added
                related_processes = [
                    'EpicWebHelper.exe', # Already in primary
                    'CrashReportClient.exe', # This is usually in subdirectories of Launcher
                    # Services like EpicOnlineServicesHost.exe can also be added, but let's focus on the main launcher for now.
                ]

            for rp in related_processes:
                all_processes_to_kill.add(rp.lower())

            processes_closed_gracefully = False
            for proc_name in primary_process_names_list: # Try to close main processes gracefully first
                if self.is_client_running([proc_name]): # Singular check
                    print(f"Attempting graceful shutdown for {proc_name}...")
                    subprocess.run(f"taskkill /im {proc_name} /t", shell=True, capture_output=True, check=False)
                    processes_closed_gracefully = True
            
            if processes_closed_gracefully:
                time.sleep(3) # Wait a bit for graceful shutdown

            # Force close all remaining processes (main and related)
            for proc_to_kill in all_processes_to_kill:
                # Using is_client_running here might cause a loop, check directly with psutil
                is_running_now = False
                try:
                    for process in psutil.process_iter(['pid', 'name']):
                        if process.info['name'] and proc_to_kill == process.info['name'].lower():
                            is_running_now = True
                            break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass # Process already gone or not accessible

                if is_running_now:
                    print(f"Attempting force shutdown for {proc_to_kill}...")
                    subprocess.run(f"taskkill /f /im {proc_to_kill} /t", shell=True, capture_output=True, check=False)
            
            time.sleep(2) # Wait to ensure all processes are terminated
            return True
        except Exception as e:
            print(f"{client_name} closing error: {e}")
            return False

    def start_client(self, client_name, client_paths): # start_steam -> start_client
        """Start the specified client"""
        try:
            if client_paths:
                client_exe = client_paths[0] # Usually the first found main executable
                subprocess.Popen([client_exe], shell=False) # Changed from shell=True to False, safer.
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
        elif client_name == "Rockstar": 
            paths_to_check = self.rockstar_paths
        elif client_name == "Epic": # Epic Games added
            paths_to_check = self.epic_paths
        
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
            elif client_name == "Rockstar": 
                 rule_name_prefix = "Block Rockstar Out"
            elif client_name == "Epic": # Epic Games added
                 rule_name_prefix = "Block Epic Out"
            
            for client_path_item in paths_to_check: 
                basename = os.path.basename(client_path_item)
                
                cmd = f'netsh advfirewall firewall show rule name="{rule_name_prefix} - {basename}"'
                success, output, _ = self.execute_firewall_command(cmd)
                
                if success and rule_name_prefix in output: # Check for prefix in rule name
                    blocked_count += 1
                    break 
            
            self.root.after(0, lambda: self.update_status(blocked_count > 0, client_name_for_status=client_name))
        
        threading.Thread(target=check_thread, daemon=True).start()
    
    def update_status(self, is_blocked, not_found=False, client_name_for_status="Client"): # client_name_for_status added
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
    app = GameClientConnectionController(root) # Class name updated
    root.mainloop()

if __name__ == "__main__":
    main()
