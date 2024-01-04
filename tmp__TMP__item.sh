#!/usr/bin/env bash

#echo
#read -p "if you need to start aws-azure-login first type 'yes': " DECISION
#echo

#[[ "$DECISION" ]] && $IKS_MENU_DIR/xr__aws-azure-login__item.sh

$IKS_MENU_DIR/xr__aws-azure-login__item.sh

echo K9S

ssh $USER@cde -t 'aws eks update-kubeconfig --name k8s-apps-v1 --region eu-central-1'
ssh $USER@cde -t 'kubectl config set-context --current --namespace=adp'

echo REDIRECTS
# READMEs: 
#    https://developer.ringieraxelspringer.tech/Development_Environment/howto/tools/cde/use-datasources-in-aws.html
#    https://developer.ringieraxelspringer.tech/Development_Environment/howto/tools/cde/use-opal-interfaces-in-aws.html
ssh $USER@cde -t '/usr/bin/cde auth add default'
ssh $USER@cde -t '/usr/bin/cde credential redirect set configservice.zookeeper-a2.configuration.onetapi.pl c2a'
ssh $USER@cde -t '/usr/bin/cde credential redirect set adp-api-cache.redis.adp.onetapi.pl c2a'
ssh $USER@cde -t '/usr/bin/cde credential redirect set adp-api-cache-ro.redis.adp.onetapi.pl c2a'
ssh $USER@cde -t '/usr/bin/cde register ad-queuedb-ro.adp.onetapi.pl c2a'
ssh $USER@cde -t '/usr/bin/cde credential redirect set ad-queuedb-ro.adp.onetapi.pl c2a'
ssh $USER@cde -t '/usr/bin/cde register api.adp.onetapi.pl c2a'
#ssh $USER@cde -t '/usr/bin/cde register ad-queuedb-ro.adp.onetapi.pl ad-queuedb-ro.adp.opal.paas-prod.aws.dreamlab 443'
#ssh $USER@cde -t '/usr/bin/cde register ad-queuedb.adp.onetapi.pl ad-queuedb.adp.opal.paas-prod.aws.dreamlab 443'
ssh $USER@cde -t '/usr/bin/cde register ad-queuedb-ro.rdbs.onetapi.pl c2a'


echo COMPLETED

