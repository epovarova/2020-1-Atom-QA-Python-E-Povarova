ocker run -v /home/liza/qa-project/config:/config -p 8080:8080 --link mysql:192.168.17.167 --link stoic_allen:192.168.17.167 myapp /app/myapp --config=/config/config.txt
