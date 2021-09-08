#!/usr/local/bin/bash

declare -A db
declare -A xtoken


key=int_metrics_db   && db[$key]="Metrics DB INT"           && xtoken[$key]=d5x76ogxnn
key=prod_metrics_db  && db[$key]="Metrics DB PROD"          && xtoken[$key]=dh9jcobdm6

key=prod_adq         && db[$key]="AdQueue PROD"             && xtoken[$key]=ds3vj762eh
key=int_adq          && db[$key]="AdQueue INT"              && xtoken[$key]=d5qtb4ycnu

key=int_schedules    && db[$key]="AdpSchedules INT"         && xtoken[$key]=d3o3c7kjr1

key=int_dasdb        && db[$key]="DAS DB INT"               && xtoken[$key]=dr74b9imdg
key=prod_dasdb       && db[$key]="DAS DB PROD"              && xtoken[$key]=dri5mhinit
key=dev_dasdb        && db[$key]="DAS DB DEV"               && xtoken[$key]=dvgdwntj6e

key=int_adpcmp       && db[$key]="AdpCmp INT"               && xtoken[$key]=dp7ttu4ff8
key=prod_adpcmp      && db[$key]="AdpCmp PROD"              && xtoken[$key]=dnvjani4kh

key=int_imdb         && db[$key]="InventoryManager INT"     && xtoken[$key]=dkhr6x6cjx
key=prod_imdb        && db[$key]="InventoryManager PROD"    && xtoken[$key]=dkm7yc7odo

key=prod_reports     && db[$key]="AdpReports PROD"          && xtoken[$key]=d3k3rw3oem
key=int_reports      && db[$key]="AdpReports INT"           && xtoken[$key]=d3kpmif9r2
key=demo_reports     && db[$key]="AdpReports INT Demo"      && xtoken[$key]=d3kpmif9r2

key=int_mailing      && db[$key]="Mailing INT"              && xtoken[$key]=d1w84169sg
key=prod_mailing     && db[$key]="Mailing PROD"             && xtoken[$key]=d4atc5x341


printf "%-25s  Description\n" "Key"
printf "===============================================\n"
for key in ${!db[@]}; do
  printf "%-25s  ${db[${key}]}\n" ${key}
done
printf "===============================================\n\n"

read -p "Provide key: " key

echo "you've selected" $key

echo  "/home/klemanski/.local/bin/rdbs -v -s int auth-token ${xtoken[${key}]}"
export LC_ALL=C.UTF-8
ssh $USER@cde "/home/klemanski/.local/bin/rdbs -v -s int auth-token ${xtoken[${key}]}"
