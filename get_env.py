import urllib.request, tarfile, os
url = "https://github.com"
print("📦 Downloading independent Python bundle...")
urllib.request.urlretrieve(url, "env.tar.gz")
print("📂 Extracting portable system files...")
with tarfile.open("env.tar.gz", "r:gz") as f:
    f.extractall(path=".")
