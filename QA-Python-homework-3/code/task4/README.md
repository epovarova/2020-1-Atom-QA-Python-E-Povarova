# Настройка виртуальной машины

Виртуальная машина работает на 192.168.17.165.

Для sshd используется порт 2022

\# semanage port -a -t ssh_port_t -p tcp 2022  
\# firewall-cmd  --permanent --zone=public --add-port 2022/tcp  
В файле /etc/ssh/sshd_config необходимо добавить строку "port 2022"

Для nginxd используется порт 2080  
\# semanage port -a -t http_port_t -p tcp 2080  
\# firewall-cmd  --permanent --zone=public --add-port 2080/tcp  
В файле /etc/nginx/nginx_config необходимо указать порт  
http {  
&nbsp;&nbsp;...  
&nbsp;&nbsp;&nbsp;&nbsp;server {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listen 2080;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...  
&nbsp;&nbsp;}  
}  