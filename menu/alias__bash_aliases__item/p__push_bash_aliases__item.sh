#!/usr/local/bin/bash

BASEDIR=$(dirname $0)

scp $BASEDIR/bash_aliases $USER@cde:/home/klemanski/.bash_aliases
scp $BASEDIR/bash_aliases $HOME/.bash_aliases
scp $BASEDIR/bash_aliases /Users/klemanski/PycharmProjects/workspace/adp-salt/userfiles/klemanski

echo All three locations updated!

