import os
import shutil

# Repo bilgileri
repo_url = 'https://github.com/MedusaMarka/Hikaye-Oyunu.git'  # Kullanıcı adı ve repo adı ile değiştirin
klonlanacak_dizin = os.getcwd()  # os.getcwd() mevcut çalışma dizinin tam yolunu verir

# Eğer dizin zaten varsa, sil
if os.path.exists(klonlanacak_dizin):
    shutil.rmtree(klonlanacak_dizin)

# Repo'yu klonla
os.system(f'git clone {repo_url} {klonlanacak_dizin}')
