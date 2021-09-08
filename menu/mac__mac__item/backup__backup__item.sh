#!/usr/local/bin/bash

HOME=/Users/klemanski
BASE_LOCAL_DIR=$HOME/PycharmProjects/local

cd $HOME'/OneDrive - RASP/'
pwd
mv backup.tar.gz backup1.tar.gz

cd $HOME
tar cvf $HOME'/OneDrive - RASP/backup.tar.gz' \
        --exclude='*/lib/' \
        --exclude='./' \
        --exclude='..' \
        --exclude='.Trash' \
        --exclude='.OneDrive - RASP'  \
        --exclude='.Library' \
        --exclude='.vscode' \
        --exclude='PycharmProjects/workspace/*/.git'	\
        --exclude='*/venv' \
	--exclude='node_modules/*' \
	--exclude='.zsh_sessions/*' \
	--exclude='.sonarlint/*' \
	--exclude='.sonar/*' \
	--exclude='.nvm/' \
	--exclude='.npm/*' \
	--exclude='.git/*' \
	--exclude='.docker/*' \
	--exclude='.bash_sessions/*' \
	--exclude='PycharmProjects/workspace/' \
	--exclude='PycharmProjects/local/bin/sonar-scanner/' \
	--exclude='PycharmProjects/local/policmajster/repos/'\
	--exclude='Movies/'\
	--exclude='Music/'\
	--exclude='Pictures/'\
	--exclude='PycharmProjects/local/_archive/sonar_stats/docker/logs/'\
	--exclude='PycharmProjects/local/*/venv/*'\
        ToBackup Desktop Documents Movies Music Pictures Public PycharmProjects .* 
	#\
        #2>$BASE_LOCAL_DIR/logs/_backup.log

#less $BASE_LOCAL_DIR/logs/_backup.log

ls -l $HOME'/OneDrive - RASP/backup'*

