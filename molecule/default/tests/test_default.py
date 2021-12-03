import os, pytest

import testinfra.utils.ansible_runner

if 'MOLECULE_INVENTORY_FILE' in os.environ:
    testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize("software", [
    ("bash-completion"),
    ("apt-file"),
    ("command-not-found"),
    ("mc"),
    ("htop"),
    ("net-tools"),
    ("rsync"),
    ("ngrep"),
    ("tcpdump"),
    ("iptraf"),
    ("apt-utils"),
    ("git"),
    ("etckeeper"),
    ("wget"),
    ("curl"),
    ("nmap"),
    ("bmon"),
    ("telnet"),
    ("hping3"),
    ("screen"),
    ("multitail"),
    ("sudo"),
    ("iperf"),
    ("vim-nox"),
    ("vim-addon-manager"),
    ("vim-editorconfig"),
    ("vim-fugitive"),
    ("vim-lastplace"),
    ("vim-python-jedi"),
    ("vim-snippets"),
    ("vim-ultisnips"),

])
def test_dependencies(host, software):

    pkg = host.package(software)
    assert pkg.is_installed