#!/bin/bash
cur_date=$(date +%Y-%m-%d)
chat_id=$(awk -F '=' 'function t(s){gsub(/[[:space:]]/,"",s);return s};/^CHAT_ID/{v=t($2)};END{printf "%s\n",v}' /home/ubuntu/faf_tg_bot/.env)
api_id=$(awk -F '=' 'function t(s){gsub(/[[:space:]]/,"",s);return s};/^API/{v=t($2)};END{printf "%s\n",v}' /home/ubuntu/faf_tg_bot/.env)
# show who play
show_who=$(sudo -u postgres psql -d fafusers -t -c "SELECT comrades FROM megausers WHERE date = '$cur_date';")
curl --data "chat_id=$chat_id&text=$show_who" https://api.telegram.org/bot$api_id/sendMessage?
