import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkFont
import subprocess
import os
import sys
import ctypes
from pathlib import Path
import threading
import time
import psutil

class GameClientConnectionController:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Client Connection Controller")
        self.root.geometry("680x520") # Yüksekliği artırdık
        self.root.resizable(False, False)
        self.root.configure(bg="#2B2B2B")

        self.default_font = tkFont.nametofont("TkDefaultFont")
        self.default_font.configure(family="Segoe UI", size=10)
        self.title_font = tkFont.Font(family="Segoe UI Semibold", size=16)
        self.label_font = tkFont.Font(family="Segoe UI", size=12)
        self.small_font = tkFont.Font(family="Segoe UI", size=9)
        self.status_font = tkFont.Font(family="Segoe UI", size=11)
        self.status_icon_font = tkFont.Font(family="Arial", size=20)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        BG_COLOR = "#2B2B2B"
        FG_COLOR = "#E0E0E0"
        FRAME_BG_COLOR = "#3C3C3C"
        BUTTON_BG_COLOR = "#555555"
        BUTTON_ACTIVE_BG_COLOR = "#6A6A6A"
        BUTTON_FG_COLOR = "#FFFFFF"
        LABELFRAME_FG_COLOR = "#C0C0C0"
        ACCENT_COLOR = "#4A90E2"
        CHECKBUTTON_INDICATOR_COLOR = "#757575"


        self.root.option_add("*Font", self.default_font)

        self.style.configure('.', background=BG_COLOR, foreground=FG_COLOR, font=self.default_font)
        self.style.configure('TFrame', background=BG_COLOR)
        self.style.configure('TLabel', background=BG_COLOR, foreground=FG_COLOR, font=self.default_font)
        self.style.configure('TLabelframe', background=BG_COLOR, bordercolor="#555555")
        self.style.configure('TLabelframe.Label', background=BG_COLOR, foreground=LABELFRAME_FG_COLOR, font=self.default_font)
        
        self.style.configure('TButton', 
                             background=BUTTON_BG_COLOR, 
                             foreground=BUTTON_FG_COLOR,
                             bordercolor="#4A4A4A",
                             lightcolor=BUTTON_BG_COLOR,
                             darkcolor=BUTTON_BG_COLOR,
                             padding=(10, 5),
                             font=self.default_font)
        self.style.map('TButton',
                       background=[('active', BUTTON_ACTIVE_BG_COLOR), ('pressed', ACCENT_COLOR)],
                       foreground=[('active', BUTTON_FG_COLOR)])

        self.style.configure('TRadiobutton', 
                             background=BG_COLOR, 
                             foreground=FG_COLOR, 
                             indicatorcolor=BG_COLOR,
                             font=self.default_font)
        self.style.map('TRadiobutton',
                       background=[('active', FRAME_BG_COLOR)],
                       indicatorcolor=[('selected', ACCENT_COLOR), ('!selected', CHECKBUTTON_INDICATOR_COLOR)],
                       foreground=[('active', FG_COLOR)])
        
        # Checkbutton Stili
        self.style.configure('TCheckbutton',
                             background=BG_COLOR,
                             foreground=FG_COLOR,
                             indicatorcolor=BG_COLOR, # Arka planla aynı
                             font=self.default_font)
        self.style.map('TCheckbutton',
                       background=[('active', FRAME_BG_COLOR)],
                       indicatorcolor=[('selected', ACCENT_COLOR), ('!selected', CHECKBUTTON_INDICATOR_COLOR)])
        
        self.steam_paths = self.find_client_paths_steam()
        self.ubisoft_paths = self.find_ubisoft_paths()
        self.ea_paths = self.find_ea_paths()
        self.rockstar_paths = self.find_rockstar_paths()
        self.epic_paths = self.find_epic_paths()
        
        self.selected_client = tk.StringVar(value="Steam")
        self.auto_restart_client = tk.BooleanVar(value=True) # Yeni ayar
        
        self.create_gui()
        self.check_connection_status()
    
    def find_client_paths_steam(self):
        possible_paths = [
            "C:\\Program Files (x86)\\Steam\\steam.exe", "C:\\Program Files\\Steam\\steam.exe",
            "D:\\Steam\\steam.exe", "E:\\Steam\\steam.exe"
        ]
        steam_paths = []
        for path in possible_paths:
            if os.path.exists(path):
                steam_paths.append(path)
                steam_dir = os.path.dirname(path)
                webhelper_path = os.path.join(steam_dir, "bin", "cef", "cef.win7x64", "steamwebhelper.exe")
                if os.path.exists(webhelper_path): steam_paths.append(webhelper_path)
        return steam_paths
    
    def find_ubisoft_paths(self):
        main_launcher_executables = ["upc.exe", "UbisoftGameLauncher.exe", "UbisoftConnect.exe"]
        possible_dir_roots = [
            "C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher", "C:\\Program Files\\Ubisoft\\Ubisoft Game Launcher",
            "D:\\Ubisoft Game Launcher", "E:\\Ubisoft Game Launcher"
        ]
        ubisoft_paths, found_launcher_dir = [], None
        for dir_root in possible_dir_roots:
            if os.path.isdir(dir_root):
                for main_exe in main_launcher_executables:
                    if os.path.exists(os.path.join(dir_root, main_exe)):
                        found_launcher_dir = dir_root; break
            if found_launcher_dir: break
        if found_launcher_dir:
            known_exes = ["upc.exe", "UbisoftGameLauncher.exe", "UbisoftConnect.exe", "UbisoftGameLauncher64.exe", 
                          "UbisoftExtension.exe", "UpcElevationService.exe", "UplayCrashReporter.exe",
                          "UplayService.exe", "UplayWebCore.exe", "UbisoftGameLauncherService.exe"]
            for exe_name in known_exes:
                exe_path = os.path.join(found_launcher_dir, exe_name)
                if os.path.exists(exe_path) and exe_path not in ubisoft_paths: ubisoft_paths.append(exe_path)
            if not ubisoft_paths:
                 for main_exe in main_launcher_executables:
                    exe_path = os.path.join(found_launcher_dir, main_exe)
                    if os.path.exists(exe_path):
                        ubisoft_paths.append(exe_path)
                        service_path = os.path.join(found_launcher_dir, "UbisoftGameLauncherService.exe")
                        if os.path.exists(service_path) and service_path not in ubisoft_paths: ubisoft_paths.append(service_path)
                        break
        if not ubisoft_paths:
            legacy_paths = ["C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\upc.exe", "D:\\Ubisoft Game Launcher\\upc.exe"] # Kısaltıldı
            for path in legacy_paths:
                if os.path.exists(path):
                    if path not in ubisoft_paths: ubisoft_paths.append(path)
                    helper = os.path.join(os.path.dirname(path), "UbisoftGameLauncherService.exe")
                    if os.path.exists(helper) and helper not in ubisoft_paths: ubisoft_paths.append(helper)
        return list(set(ubisoft_paths))

    def find_ea_paths(self):
        main_execs = ["EADesktop.exe", "EALauncher.exe"]
        roots = ["C:\\Program Files\\Electronic Arts\\EA Desktop\\EA Desktop", "C:\\Program Files (x86)\\Electronic Arts\\EA Desktop\\EA Desktop", "D:\\EA Games\\EA Desktop", "E:\\EA Games\\EA Desktop"]
        paths, found_dir = [], None
        for r in roots:
            if os.path.isdir(r):
                for me in main_execs:
                    if os.path.exists(os.path.join(r, me)): found_dir = r; break
            if found_dir: break
        if found_dir:
            known = ["EADesktop.exe", "EABackgroundService.exe", "EALauncher.exe", "EAConnect_microsoft.exe", "EACrashReporter.exe", "EAUpdater.exe", "EALocalHostSvc.exe", "EAGEP.exe", "EACefSubProcess.exe", "IGOProxy32.exe", "Link2EA.exe", "ErrorReporter.exe", "EAUninstall.exe", "GetGameToken32.exe", "GetGameToken64.exe", "OriginLegacyCompatibility.exe"]
            for k in known:
                p = os.path.join(found_dir, k)
                if os.path.exists(p) and p not in paths: paths.append(p)
            if not paths:
                for me in main_execs:
                    p = os.path.join(found_dir, me)
                    if os.path.exists(p):
                        paths.append(p)
                        sp = os.path.join(found_dir, "EABackgroundService.exe")
                        if os.path.exists(sp) and sp not in paths: paths.append(sp)
                        break
        return list(set(paths))

    def find_rockstar_paths(self):
        main_execs = ["Launcher.exe", "LauncherPatcher.exe"]
        roots = ["C:\\Program Files\\Rockstar Games\\Launcher", "C:\\Program Files (x86)\\Rockstar Games\\Launcher", "D:\\Rockstar Games\\Launcher", "E:\\Rockstar Games\\Launcher"]
        paths, found_dir = [], None
        for r in roots:
            if os.path.isdir(r):
                for me in main_execs:
                    if os.path.exists(os.path.join(r, me)): found_dir = r; break
            if found_dir: break
        if found_dir:
            known = ["Launcher.exe", "LauncherPatcher.exe", "RockstarService.exe", "RockstarSteamHelper.exe", "uninstall.exe"]
            for k in known:
                p = os.path.join(found_dir, k)
                if os.path.exists(p) and p not in paths: paths.append(p)
            if not paths:
                for me in main_execs:
                    p = os.path.join(found_dir, me)
                    if os.path.exists(p):
                        paths.append(p)
                        sp = os.path.join(found_dir, "RockstarService.exe")
                        if os.path.exists(sp) and sp not in paths: paths.append(sp)
                        break
        return list(set(paths))

    def find_epic_paths(self):
        main_execs = ["EpicGamesLauncher.exe"]
        roots = ["C:\\Program Files (x86)\\Epic Games\\Launcher", "C:\\Program Files\\Epic Games\\Launcher", "D:\\Epic Games\\Launcher", "E:\\Epic Games\\Launcher"]
        paths, found_portal_dir = [], None
        for r in roots:
            if os.path.isdir(r):
                sub_dirs = [os.path.join(r, "Portal", "Binaries", "Win64"), os.path.join(r, "Portal", "Binaries", "Win32")]
                for sd in sub_dirs:
                    if os.path.isdir(sd):
                        for me in main_execs:
                            if os.path.exists(os.path.join(sd, me)): found_portal_dir = sd; break
                    if found_portal_dir: break
            if found_portal_dir: break
        if found_portal_dir:
            known = ["EpicGamesLauncher.exe", "EpicWebHelper.exe"]
            for k in known:
                p = os.path.join(found_portal_dir, k)
                if os.path.exists(p) and p not in paths: paths.append(p)
            if not paths:
                for me in main_execs:
                    p = os.path.join(found_portal_dir, me)
                    if os.path.exists(p): paths.append(p); break
        return list(set(paths))

    def create_gui(self):
        main_frame = ttk.Frame(self.root, padding="20", style='TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        title_label = ttk.Label(main_frame, text="Game Client Connection Controller", font=self.title_font, style='TLabel', anchor=tk.CENTER)
        title_label.grid(row=0, column=0, columnspan=5, pady=(0, 20), sticky=tk.EW)

        client_frame = ttk.LabelFrame(main_frame, text="Select Client", padding="15", style='TLabelframe')
        client_frame.grid(row=1, column=0, columnspan=5, sticky=(tk.W, tk.E), pady=(0,15))
        client_frame.columnconfigure((0,1,2,3,4), weight=1)

        clients = ["Steam", "Ubisoft", "EA", "Rockstar", "Epic"]
        client_display_names = ["Steam", "Ubisoft Connect", "EA Play", "Rockstar", "Epic Games"]
        for i, client_val in enumerate(clients):
            radio = ttk.Radiobutton(client_frame, text=client_display_names[i], variable=self.selected_client, value=client_val, command=self.on_client_change, style='TRadiobutton')
            radio.grid(row=0, column=i, padx=10, pady=5, sticky=tk.W)

        self.status_label = ttk.Label(main_frame, text="Checking status...", font=self.label_font, style='TLabel', anchor=tk.CENTER)
        self.status_label.grid(row=2, column=0, columnspan=5, pady=(10, 10), sticky=tk.EW)
        
        status_frame = ttk.LabelFrame(main_frame, text="Connection Status", padding="15", style='TLabelframe')
        status_frame.grid(row=3, column=0, columnspan=5, sticky=(tk.W, tk.E), pady=(0, 15))
        status_frame.columnconfigure(1, weight=1)
        
        self.connection_status = ttk.Label(status_frame, text="●", font=self.status_icon_font, style='TLabel')
        self.connection_status.grid(row=0, column=0, padx=(0, 10))
        self.connection_text = ttk.Label(status_frame, text="Checking...", font=self.status_font, style='TLabel')
        self.connection_text.grid(row=0, column=1, sticky=tk.W)
        
        # Settings Frame
        settings_frame = ttk.Frame(main_frame, style='TFrame')
        settings_frame.grid(row=4, column=0, columnspan=5, pady=(0,10), sticky=tk.EW)
        settings_frame.columnconfigure(0, weight=1) # Checkbox'ı ortalamak için

        self.auto_restart_checkbox = ttk.Checkbutton(settings_frame, text="Automatically close/restart client", variable=self.auto_restart_client, style='TCheckbutton')
        self.auto_restart_checkbox.grid(row=0, column=0, pady=5, sticky=tk.N) # sticky=tk.N ile ortalandı

        # Buttons Frame
        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.grid(row=5, column=0, columnspan=5, pady=10) # row indeksi güncellendi
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        self.block_button = ttk.Button(button_frame, text="Block Connection", command=self.block_client, width=18, style='TButton')
        self.block_button.grid(row=0, column=0, padx=(0, 10), sticky=tk.E)
        self.unblock_button = ttk.Button(button_frame, text="Allow Connection", command=self.unblock_client, width=18, style='TButton')
        self.unblock_button.grid(row=0, column=1, padx=(10, 0), sticky=tk.W)
        
        refresh_button = ttk.Button(main_frame, text="Refresh Status", command=self.check_connection_status, width=20, style='TButton')
        refresh_button.grid(row=6, column=0, columnspan=5, pady=10) # row indeksi güncellendi
        
        self.info_frame = ttk.LabelFrame(main_frame, text="Client Information", padding="10", style='TLabelframe')
        self.info_frame.grid(row=7, column=0, columnspan=5, sticky=(tk.W, tk.E, tk.S), pady=(10, 0)) # row indeksi güncellendi
        self.info_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(7, weight=1)
        
        self.update_client_info_display()

    def update_client_info_display(self):
        for widget in self.info_frame.winfo_children(): widget.destroy()
        client_name = self.selected_client.get()
        paths, label_str = [], ""
        if client_name == "Steam": paths, label_str = self.steam_paths, "Steam"
        elif client_name == "Ubisoft": paths, label_str = self.ubisoft_paths, "Ubisoft Connect"
        elif client_name == "EA": paths, label_str = self.ea_paths, "EA Play (EA Desktop)"
        elif client_name == "Rockstar": paths, label_str = self.rockstar_paths, "Rockstar Launcher"
        elif client_name == "Epic": paths, label_str = self.epic_paths, "Epic Games Launcher"
        info = f"Found {label_str} files: {len(paths)}" if paths else f"{label_str} not found!"
        ttk.Label(self.info_frame, text=info, font=self.small_font, style='TLabel', anchor=tk.W).grid(row=0, column=0, sticky=tk.EW)

    def on_client_change(self):
        self.update_client_info_display()
        self.check_connection_status()

    def is_admin(self):
        try: return ctypes.windll.shell32.IsUserAnAdmin()
        except: return False
    
    def run_as_admin(self):
        if self.is_admin(): return True
        messagebox.showwarning("Administrator Rights Required", "This operation requires administrator privileges.\nThe program will restart as administrator.")
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            self.root.quit()
            return False
        except:
            messagebox.showerror("Error", "Could not obtain administrator privileges!")
            return False
    
    def execute_firewall_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e: return False, "", str(e)

    def block_client(self):
        if not self.run_as_admin(): return
        client_name = self.selected_client.get()
        client_paths, primary_processes = self._get_client_data(client_name)
        if not client_paths:
            messagebox.showerror("Error", f"{client_name} installation not found!")
            return

        client_is_running = self.is_client_running(primary_processes)
        perform_restart = self.auto_restart_client.get()

        if client_is_running and perform_restart:
            if not messagebox.askyesno(f"{client_name} Will Be Closed", f"{client_name} is running. To block, it will be closed and restarted.\nContinue?"):
                return
        elif client_is_running and not perform_restart:
             messagebox.showinfo("Manual Restart Recommended", f"{client_name} is running. Firewall rules will be applied, but you may need to manually restart {client_name} for changes to take full effect.")


        self.status_label.config(text=f"Blocking {client_name}...")
        self.root.update()
        
        def block_actions():
            if client_is_running and perform_restart:
                self.root.after(0, lambda: self.status_label.config(text=f"Closing {client_name}..."))
                self.close_client(client_name, primary_processes)
            
            self.root.after(0, lambda: self.status_label.config(text="Creating firewall rules..."))
            s_count = 0
            for path in client_paths:
                r_out = f"Block {client_name} Out - {os.path.basename(path)}"
                r_in = f"Block {client_name} In - {os.path.basename(path)}"
                cmd_out = f'netsh advfirewall firewall add rule name="{r_out}" dir=out action=block program="{path}"'
                cmd_in = f'netsh advfirewall firewall add rule name="{r_in}" dir=in action=block program="{path}"'
                s_o, _, _ = self.execute_firewall_command(cmd_out)
                s_i, _, _ = self.execute_firewall_command(cmd_in)
                if s_o and s_i: s_count += 1
            
            if client_is_running and perform_restart and s_count > 0:
                self.root.after(0, lambda: self.status_label.config(text=f"Restarting {client_name}..."))
                time.sleep(1)
                self.start_client(client_name, client_paths)
            
            self.root.after(0, lambda: self.block_complete(s_count, client_is_running and perform_restart, client_name))
        
        threading.Thread(target=block_actions, daemon=True).start()

    def block_complete(self, success_count, client_was_restarted, client_name):
        if success_count > 0:
            msg = f"{client_name} connection blocked. Rules created for {success_count} files."
            if client_was_restarted: msg += f"\n{client_name} has been restarted."
            elif self.auto_restart_client.get() == False and self.is_client_running(self._get_client_data(client_name)[1]):
                 msg += f"\nPlease manually restart {client_name} for changes to take full effect."
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", f"Could not block {client_name} connection!")
        self.check_connection_status()

    def unblock_client(self):
        if not self.run_as_admin(): return
        client_name = self.selected_client.get()
        client_paths, primary_processes = self._get_client_data(client_name)
        if not client_paths:
            messagebox.showerror("Error", f"{client_name} installation not found!")
            return

        client_is_running = self.is_client_running(primary_processes)
        perform_restart = self.auto_restart_client.get()

        if client_is_running and perform_restart:
            if not messagebox.askyesno(f"{client_name} Will Be Closed", f"{client_name} is running. To allow connection, it will be closed and restarted.\nContinue?"):
                return
        elif client_is_running and not perform_restart:
            messagebox.showinfo("Manual Restart Recommended", f"{client_name} is running. Firewall rules will be removed, but you may need to manually restart {client_name} for changes to take full effect.")

        self.status_label.config(text=f"Allowing {client_name}...")
        self.root.update()

        def unblock_actions():
            if client_is_running and perform_restart:
                self.root.after(0, lambda: self.status_label.config(text=f"Closing {client_name}..."))
                self.close_client(client_name, primary_processes)

            self.root.after(0, lambda: self.status_label.config(text="Removing firewall rules..."))
            removed_count = 0
            for path in client_paths:
                r_out = f"Block {client_name} Out - {os.path.basename(path)}"
                r_in = f"Block {client_name} In - {os.path.basename(path)}"
                cmd_out = f'netsh advfirewall firewall delete rule name="{r_out}"'
                cmd_in = f'netsh advfirewall firewall delete rule name="{r_in}"'
                s_o, _, _ = self.execute_firewall_command(cmd_out)
                s_i, _, _ = self.execute_firewall_command(cmd_in)
                if s_o or s_i: removed_count +=1
            
            if client_is_running and perform_restart:
                self.root.after(0, lambda: self.status_label.config(text=f"Restarting {client_name}..."))
                time.sleep(1)
                self.start_client(client_name, client_paths)
            
            self.root.after(0, lambda: self.unblock_complete(removed_count > 0, client_is_running and perform_restart, client_name))
        
        threading.Thread(target=unblock_actions, daemon=True).start()

    def unblock_complete(self, rules_were_removed, client_was_restarted, client_name):
        if rules_were_removed:
            msg = f"{client_name} connection allowed. Relevant firewall rules removed."
            if client_was_restarted: msg += f"\n{client_name} has been restarted."
            elif self.auto_restart_client.get() == False and self.is_client_running(self._get_client_data(client_name)[1]):
                 msg += f"\nPlease manually restart {client_name} for changes to take full effect."
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showinfo("Info", f"No active blocking rules found for {client_name}, or rules already removed.")
        self.check_connection_status()
        
    def _get_client_data(self, client_name):
        """Helper to get paths and primary processes for a client."""
        if client_name == "Steam": return self.steam_paths, ["steam.exe"]
        if client_name == "Ubisoft": return self.ubisoft_paths, ["upc.exe", "UbisoftGameLauncher.exe", "UbisoftConnect.exe", "UbisoftGameLauncher64.exe"]
        if client_name == "EA": return self.ea_paths, ["EADesktop.exe", "EALauncher.exe", "EABackgroundService.exe"]
        if client_name == "Rockstar": return self.rockstar_paths, ["Launcher.exe", "LauncherPatcher.exe", "RockstarService.exe"]
        if client_name == "Epic": return self.epic_paths, ["EpicGamesLauncher.exe", "EpicWebHelper.exe"]
        return [], []

    def is_client_running(self, primary_process_names_list):
        try:
            return any(proc_name.lower() in (p.info['name'].lower() for p in psutil.process_iter(['name']) if p.info['name']) for proc_name in primary_process_names_list)
        except Exception as e:
            print(f"Error checking client status: {e}")
            return False

    def close_client(self, client_name, primary_process_names_list):
        try:
            all_to_kill = set(p.lower() for p in primary_process_names_list)
            related = {
                "Steam": ['steamwebhelper.exe', 'steamservice.exe'],
                "Ubisoft": ['UbisoftGameLauncherService.exe', 'UplayService.exe', 'UplayWebCore.exe', 'UbisoftExtension.exe', 'UpcElevationService.exe', 'UplayCrashReporter.exe'],
                "EA": ['EABackgroundService.exe', 'EAConnect_microsoft.exe', 'EACrashReporter.exe', 'EAUpdater.exe', 'EALocalHostSvc.exe', 'EAGEP.exe', 'EACefSubProcess.exe', 'IGOProxy32.exe', 'Link2EA.exe', 'ErrorReporter.exe'],
                "Rockstar": ['RockstarService.exe', 'RockstarSteamHelper.exe'],
                "Epic": ['EpicWebHelper.exe', 'CrashReportClient.exe'] # CrashReportClient is often in subdirs
            }
            if client_name in related:
                for rp in related[client_name]: all_to_kill.add(rp.lower())

            graceful = False
            for proc_name in primary_process_names_list:
                if self.is_client_running([proc_name]):
                    subprocess.run(f"taskkill /im {proc_name} /t", shell=True, capture_output=True, check=False)
                    graceful = True
            if graceful: time.sleep(3)

            for proc_kill in all_to_kill:
                if any(p.info['name'] and proc_kill == p.info['name'].lower() for p in psutil.process_iter(['name']) if p.info['name']):
                    subprocess.run(f"taskkill /f /im {proc_kill} /t", shell=True, capture_output=True, check=False)
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error closing {client_name}: {e}")
            return False

    def start_client(self, client_name, client_paths):
        try:
            if client_paths: subprocess.Popen([client_paths[0]], shell=False); return True
            return False
        except Exception as e:
            print(f"Error starting {client_name}: {e}")
            return False

    def check_connection_status(self):
        client_name = self.selected_client.get()
        paths, _ = self._get_client_data(client_name)
        if not paths: self.update_status(False, True, client_name); return

        def check_thread():
            blocked = False
            rule_prefix = f"Block {client_name} Out"
            for path_item in paths:
                rule_name = f"{rule_prefix} - {os.path.basename(path_item)}"
                cmd = f'netsh advfirewall firewall show rule name="{rule_name}"'
                success, output, _ = self.execute_firewall_command(cmd)
                if success and rule_name in output: blocked = True; break
            self.root.after(0, lambda: self.update_status(blocked, client_name_for_status=client_name))
        
        threading.Thread(target=check_thread, daemon=True).start()
    
    def update_status(self, is_blocked, not_found=False, client_name_for_status="Client"):
        COLOR_NOT_FOUND, COLOR_BLOCKED, COLOR_ALLOWED, FG_COLOR = "#FFA500", "#FF5252", "#4CAF50", "#E0E0E0"
        if not_found:
            self.connection_status.config(text="!", foreground=COLOR_NOT_FOUND)
            self.connection_text.config(text=f"{client_name_for_status} Not Found", foreground=FG_COLOR)
            self.status_label.config(text=f"{client_name_for_status} installation not detected.", foreground=FG_COLOR)
        elif is_blocked:
            self.connection_status.config(text="●", foreground=COLOR_BLOCKED)
            self.connection_text.config(text="Connection Blocked", foreground=FG_COLOR)
            self.status_label.config(text=f"{client_name_for_status}'s internet connection is BLOCKED", foreground=COLOR_BLOCKED)
        else:
            self.connection_status.config(text="●", foreground=COLOR_ALLOWED)
            self.connection_text.config(text="Connection Allowed", foreground=FG_COLOR)
            self.status_label.config(text=f"{client_name_for_status}'s internet connection is ALLOWED", foreground=COLOR_ALLOWED)

def main():
    root = tk.Tk()
    app = GameClientConnectionController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
