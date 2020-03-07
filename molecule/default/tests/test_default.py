import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_yum_cron_conf(host):
    file = host.file('/etc/yum/yum-cron.conf')
    assert file.sha256sum == \
        "4fec11b97d79b3bd83069580afd843ca8efb50bab2f88d52eafef0817fbda8d5"


def test_yum_cron_package(host):
    package = host.package('yum-cron')
    assert package.is_installed


def test_yum_cron_service(host):
    service = host.service("yum-cron")
    assert service.is_running
    assert service.is_enabled
