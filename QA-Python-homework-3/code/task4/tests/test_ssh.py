import pytest
from pip._vendor import requests


class TestSSH:

    @pytest.mark.SSH
    def test_sudo(self, ssh_client, config):
        messages = ssh_client.exec_root_cmd('tail -n 10 /var/log/secure', config['ssh_password'])
        assert str(messages).find(f"sudo:    {config['ssh_user']}") != -1

    @pytest.mark.SSH
    def test_connect_nginx_by_request(self, enable_nginx_port, config):
        assert 200 == requests.get(f'http://{config["ssh_host"]}:{config["nginx_port"]}').status_code

    @pytest.mark.SSH
    def test_connect_nginx_by_ssh(self, enable_nginx_port, ssh_client, config):
        assert 'LISTEN' in ssh_client.exec_root_cmd(f"netstat -tulpn | grep \'{config['nginx_port']}\'",
                                                    config['ssh_password'])

    @pytest.mark.SSH
    def test_logs(self, enable_nginx_port, ssh_client, config):
        count_before = int(ssh_client.exec_root_cmd("wc -l /var/log/nginx/access.log | cut -f1 -d' '",
                                                    config['ssh_password']))
        requests.get(f'http://{config["ssh_host"]}:{config["nginx_port"]}')
        count_after = int(ssh_client.exec_root_cmd("wc -l /var/log/nginx/access.log | cut -f1 -d' '",
                                                   config['ssh_password']))
        assert count_before + 1 == count_after

    @pytest.mark.SSH
    def test_nginx_with_disabled_port(self, enable_nginx_port, ssh_client, config):
        commands = [
            f'firewall-cmd --permanent --zone=public --remove-port={config["nginx_port"]}/tcp',
            'firewall-cmd --reload',
            'systemctl restart nginx'
        ]
        for command in commands:
            ssh_client.exec_root_cmd(command, config['ssh_password'])

        with pytest.raises(IOError):
            requests.get(f'http://{config["ssh_host"]}:{config["nginx_port"]}')

        assert 'LISTEN' in ssh_client.exec_root_cmd(f"netstat -tulpn | grep \'{config['nginx_port']}\'",
                                                    config['ssh_password'])
