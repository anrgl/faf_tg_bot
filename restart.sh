#!/bin/bash
if ! pgrep -f "python3 /home/ubuntu/faf_tg_bot/main.py" > /dev/null; then
	cd /tmp && python3 /home/ubuntu/faf_tg_bot/main.py &
fi
