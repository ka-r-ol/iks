# iks
Simple script manager


Install
===
1. Install binaries
```
cd ~/PycharmProjects
git clone https://github.com/ka-r-ol/iks.git
cd iks
sh install_me.sh
cp -R use_case/.iks ~/.iks
cp use_case/iks ~/bin 
chmod u+x ~/bin/iks
```
2. update iks ENV parameters
```
vi ~/bin/iks
```
 - export IKS_BASE_DIR=$HOME/PycharmProjects/iks
 - export IKS_MENU_DIR=$HOME/.iks//menu
