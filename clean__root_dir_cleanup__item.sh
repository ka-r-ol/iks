#!/usr/bin/env bash


ssh $USER@cde -t  ' sudo chown -R klemanski:users /home/klemanski/.cache' 
echo   /home/klemanski/.cache updated

ssh $USER@cde -t ' sudo chmod oug+w /home/klemanski/.config'
echo   /home/klemanski/.config updated


ssh $USER@cde -t ' sudo chmod oug+w /home/klemanski/.local/bin/webi'
echo   /home/klemanski/.local/bin/webi updated

 



