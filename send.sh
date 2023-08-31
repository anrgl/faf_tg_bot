#!/bin/bash
chat_id=$(awk -F '=' 'function t(s){gsub(/[[:space:]]/,"",s);return s};/^CHAT_ID/{v=t($2)};END{printf "%s\n",v}' /home/ubuntu/faf_tg_bot/.env)
api_id=$(awk -F '=' 'function t(s){gsub(/[[:space:]]/,"",s);return s};/^API/{v=t($2)};END{printf "%s\n",v}' /home/ubuntu/faf_tg_bot/.env)
curl --data "chat_id=$chat_id&text=Приветствую командоры! Кто сегодня будет играть? Команды можете посмотреть набрав  /  в чате " https://api.telegram.org/bot$api_id/sendMessage?
