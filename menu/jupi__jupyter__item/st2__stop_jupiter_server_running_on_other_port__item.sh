cd /Users/klemanski/PycharmProjects/local/jupiter
source venv/bin/activate
jupyter notebook list


read -p "Provide server port number: " PORT

jupyter notebook stop $PORT
