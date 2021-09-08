#!/usr/local/bin/bash

echo
read -p "if you need to start aws-azure-login first type 'yes': " DECISION
echo

[[ "$DECISION" ]] && $IKS_MENU_DIR/xr__aws-azure-login__item.sh
echo K9S

ssh $USER@cde -t 'aws eks update-kubeconfig --name k8s-apps-v1 --region eu-central-1'
ssh $USER@cde -t 'kubectl config set-context --current --namespace=adp'

echo REDIRECTS

ssh $USER@cde -t '/usr/bin/cde auth add default'
ssh $USER@cde -t '/usr/bin/cde credential redirect set configservice.zookeeper-a2.configuration.onetapi.pl c2a-int'
ssh $USER@cde -t '/usr/bin/cde credential redirect set adp-api-cache.redis.adp.onetapi.pl c2a-int'

echo COMPLETED

