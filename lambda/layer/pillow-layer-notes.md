 # Notes on building Pillow layer in-cloud
 in cloud9 Linux2023
 
 # Install Python 3.12 and pip if not available
sudo dnf install python3.12 -y
python3.12 -m ensurepip --upgrade
python3.12 -m pip install --upgrade pip

# Create layer folder
mkdir -p python/lib/python3.12/site-packages

# Install Pillow into it
python3.12 -m pip install pillow -t python/lib/python3.12/site-packages/

# Zip it up
zip -r9 pillow-layer-python312.zip python
