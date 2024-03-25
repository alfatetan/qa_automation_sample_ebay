#!/bin/bash

echo "eBay automation QA testing installation..."

# Checking: HomeBrew is exists or not
if ! which brew > /dev/null; then
   echo -e "HomeBrew is not installed! Install? (y/n) \c"
   read
   if "$REPLY" = "y"; then
      curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
   fi
fi

echo "Packages updating and upgrating..."
brew update
brew upgrade

echo "Checking Python 3 has been installed already or not"
REQUIRED_PKG="python3"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK

# If package is not exist - install python 3.x
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  brew --yes install $REQUIRED_PKG
fi

echo "Python environment installation..."
python -m venv ./venv
source ./venv/bin/activate

# Install requirenments
pip install -r requirenments.txt

# Installation is done
echo "Instalation is done! Enjoy new tests!"