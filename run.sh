#!/bin/bash
chat_id=$(awk -F '=' 'function t(s){gsub(/[[:space:]]/,"",s);return s};/^CHAT_ID/{v=t($2)};END{printf "%s\n",v}' ./.env)
api_id=$(awk -F '=' 'function t(s){gsub(/[[:space:]]/,"",s);return s};/^API/{v=t($2)};END{printf "%s\n",v}' ./.env)
extract=$(cat ./get.md)
extr_tbl=$(awk -F' ' '{print $1}' ./get.md)

if ! apt list --installed | grep postgresql &>/dev/null ; then sudo apt-get install postgresql postgresql-contrib ; fi

cur_date=$(date +%Y-%m-%d)
# create db
if ! sudo -u postgres psql -c "\l" | grep fafusers ; then
    sudo -u postgres psql -c "CREATE DATABASE fafusers"
fi
# create table
if ! sudo -u postgres psql -d fafusers -c "\d" | grep megausers ; then 
sudo -u postgres psql -d fafusers -c "CREATE TABLE megausers (comrades CHAR(20), date DATE);"
fi
# add data
sudo -u postgres psql -d fafusers -c "INSERT INTO megausers(comrades, date) SELECT '$extr_tbl', '$cur_date' WHERE NOT EXISTS (SELECT 1 FROM megausers WHERE comrades = '$extr_tbl' AND date = '$cur_date');"

curl --data "chat_id=$chat_id&text=$extract" https://api.telegram.org/bot$api_id/sendMessage?