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
        self.root.title("Steam Bağlantı Kontrolcüsü")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Steam executable dosyalarının yolları
        self.steam_paths = self.find_steam_paths()
        
        # GUI oluştur
        self.create_gui()
        
        # Başlangıçta durumu kontrol et
        self.check_connection_status()
    
    def find_steam_paths(self):
        """Steam'ın kurulu olduğu yolları bul"""
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
                # Steam klasöründeki diğer önemli dosyaları da ekle
                steam_dir = os.path.dirname(path)
                webhelper_path = os.path.join(steam_dir, "bin", "cef", "cef.win7x64", "steamwebhelper.exe")
                if os.path.exists(webhelper_path):
                    steam_paths.append(webhelper_path)
        
        return steam_paths
    
    def create_gui(self):
        """GUI arayüzünü oluştur"""
        # Ana frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Başlık
        title_label = ttk.Label(main_frame, text="Steam Bağlantı Kontrolcüsü", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Durum göstergesi
        self.status_label = ttk.Label(main_frame, text="Durum kontrol ediliyor...", 
                                     font=("Arial", 12))
        self.status_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Durum gösterge çerçevesi
        status_frame = ttk.LabelFrame(main_frame, text="Bağlantı Durumu", padding="10")
        status_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.connection_status = ttk.Label(status_frame, text="●", font=("Arial", 20))
        self.connection_status.grid(row=0, column=0, padx=(0, 10))
        
        self.connection_text = ttk.Label(status_frame, text="Kontrol ediliyor...", 
                                        font=("Arial", 11))
        self.connection_text.grid(row=0, column=1)
        
        # Butonlar
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.block_button = ttk.Button(button_frame, text="Bağlantıyı Kes", 
                                      command=self.block_steam, width=15)
        self.block_button.grid(row=0, column=0, padx=(0, 10))
        
        self.unblock_button = ttk.Button(button_frame, text="Bağlantıyı Aç", 
                                        command=self.unblock_steam, width=15)
        self.unblock_button.grid(row=0, column=1, padx=(10, 0))
        
        # Yenile butonu
        refresh_button = ttk.Button(main_frame, text="Durumu Yenile", 
                                   command=self.check_connection_status)
        refresh_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Steam yolları bilgisi
        info_frame = ttk.LabelFrame(main_frame, text="Steam Bilgileri", padding="10")
        info_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        if self.steam_paths:
            info_text = f"Bulunan Steam dosyaları: {len(self.steam_paths)}"
        else:
            info_text = "Steam bulunamadı!"
        
        ttk.Label(info_frame, text=info_text, font=("Arial", 9)).grid(row=0, column=0)
    
    def is_admin(self):
        """Yönetici yetkisi kontrolü"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def run_as_admin(self):
        """Programı yönetici olarak çalıştır"""
        if self.is_admin():
            return True
        else:
            messagebox.showwarning("Yönetici Yetkisi Gerekli", 
                                 "Bu işlem için yönetici yetkisi gereklidir.\n"
                                 "Program yönetici olarak yeniden başlatılacak.")
            try:
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                self.root.quit()
                return False
            except:
                messagebox.showerror("Hata", "Yönetici yetkisi alınamadı!")
                return False
    
    def execute_firewall_command(self, command):
        """Firewall komutunu çalıştır"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def is_steam_running(self):
        """Steam'ın çalışıp çalışmadığını kontrol et"""
        try:
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] and 'steam.exe' in process.info['name'].lower():
                    return True
            return False
        except Exception:
            return False
    
    def close_steam(self):
        """Steam'ı kapat"""
        try:
            # Steam'ı nazikçe kapat
            subprocess.run("taskkill /im steam.exe /t", shell=True, capture_output=True)
            time.sleep(2)  # Steam'ın kapanması için bekle
            
            # Hala çalışıyorsa zorla kapat
            if self.is_steam_running():
                subprocess.run("taskkill /f /im steam.exe /t", shell=True, capture_output=True)
                time.sleep(1)
            
            # Steam ile ilgili diğer süreçleri de kapat
            steam_processes = ['steamwebhelper.exe', 'steamservice.exe', 'steam.exe']
            for process_name in steam_processes:
                subprocess.run(f"taskkill /f /im {process_name} /t", shell=True, capture_output=True)
            
            time.sleep(2)  # Tüm süreçlerin kapanması için bekle
            return True
        except Exception as e:
            print(f"Steam kapatma hatası: {e}")
            return False
    
    def start_steam(self):
        """Steam'ı başlat"""
        try:
            if self.steam_paths:
                # İlk bulunan Steam yolunu kullan
                steam_exe = self.steam_paths[0]
                subprocess.Popen([steam_exe], shell=True)
                return True
            return False
        except Exception as e:
            print(f"Steam başlatma hatası: {e}")
            return False
    
    def block_steam(self):
        """Steam'ı engelle"""
        if not self.run_as_admin():
            return
        
        if not self.steam_paths:
            messagebox.showerror("Hata", "Steam bulunamadı!")
            return
        
        self.status_label.config(text="Steam engelleniyor...")
        self.root.update()
        
        def block_thread():
            success_count = 0
            for steam_path in self.steam_paths:
                # Giden bağlantıları engelle
                cmd_out = f'netsh advfirewall firewall add rule name="Block Steam Out - {os.path.basename(steam_path)}" dir=out action=block program="{steam_path}"'
                success_out, _, _ = self.execute_firewall_command(cmd_out)
                
                # Gelen bağlantıları engelle
                cmd_in = f'netsh advfirewall firewall add rule name="Block Steam In - {os.path.basename(steam_path)}" dir=in action=block program="{steam_path}"'
                success_in, _, _ = self.execute_firewall_command(cmd_in)
                
                if success_out and success_in:
                    success_count += 1
            
            self.root.after(0, lambda: self.block_complete(success_count))
        
        threading.Thread(target=block_thread, daemon=True).start()
    
    def block_complete(self, success_count):
        """Engelleme işlemi tamamlandı"""
        if success_count > 0:
            messagebox.showinfo("Başarılı", f"Steam bağlantısı kesildi!\n"
                                          f"{success_count} dosya için kural oluşturuldu.")
        else:
            messagebox.showerror("Hata", "Steam engellenemedi!")
        
        self.check_connection_status()
    
    def unblock_steam(self):
        """Steam engelini kaldır"""
        if not self.run_as_admin():
            return
        
        self.status_label.config(text="Steam engeli kaldırılıyor...")
        self.root.update()
        
        def unblock_thread():
            success_count = 0
            
            # Tüm Steam ile ilgili kuralları sil
            for steam_path in self.steam_paths:
                basename = os.path.basename(steam_path)
                
                # Giden kuralları sil
                cmd_out = f'netsh advfirewall firewall delete rule name="Block Steam Out - {basename}"'
                success_out, _, _ = self.execute_firewall_command(cmd_out)
                
                # Gelen kuralları sil
                cmd_in = f'netsh advfirewall firewall delete rule name="Block Steam In - {basename}"'
                success_in, _, _ = self.execute_firewall_command(cmd_in)
                
                if success_out or success_in:
                    success_count += 1
            
            self.root.after(0, lambda: self.unblock_complete(success_count))
        
        threading.Thread(target=unblock_thread, daemon=True).start()
    
    def unblock_complete(self, success_count):
        """Engel kaldırma işlemi tamamlandı"""
        if success_count > 0:
            messagebox.showinfo("Başarılı", f"Steam bağlantısı açıldı!\n"
                                          f"{success_count} dosya için kural kaldırıldı.")
        else:
            messagebox.showinfo("Bilgi", "Kaldırılacak kural bulunamadı.")
        
        self.check_connection_status()
    
    def check_connection_status(self):
        """Bağlantı durumunu kontrol et"""
        def check_thread():
            blocked_count = 0
            
            for steam_path in self.steam_paths:
                basename = os.path.basename(steam_path)
                
                # Giden kuralları kontrol et
                cmd = f'netsh advfirewall firewall show rule name="Block Steam Out - {basename}"'
                success, output, _ = self.execute_firewall_command(cmd)
                
                if success and "Block Steam Out" in output:
                    blocked_count += 1
                    break
            
            self.root.after(0, lambda: self.update_status(blocked_count > 0))
        
        threading.Thread(target=check_thread, daemon=True).start()
    
    def update_status(self, is_blocked):
        """Durum göstergesini güncelle"""
        if is_blocked:
            self.connection_status.config(text="●", foreground="red")
            self.connection_text.config(text="Bağlantı Kesildi")
            self.status_label.config(text="Steam'ın internet bağlantısı kapalı")
        else:
            self.connection_status.config(text="●", foreground="green")
            self.connection_text.config(text="Bağlantı Açık")
            self.status_label.config(text="Steam'ın internet bağlantısı açık")

def main():
    root = tk.Tk()
    app = SteamConnectionController(root)
    root.mainloop()

if __name__ == "__main__":
    main()