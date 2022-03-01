blindfiles = ['cat /etc/resolv.conf',
              'cat /etc/issue',
              'cat /etc/passwd',
              'cat /etc/shadow',
              'cat /etc/motd']

systemcmds = ['uname -a',
               'ps aux',
               'id',
               'w',
               'mysql --version']

networkcmds = ['hostname -f',
                'ip addr show',
                'ip ro show',
                'route -n',
                'cat /etc/network/interfaces']

useraccounts = ['cat /etc/passwd',
           'cat /etc/shadow',
           'cat /etc/group',
           'getent passwd',
           'getent group']

userinfo = ['ls -alh /home/*/.ssh/',
            'cat /home/*/.ssh/authorized_keys',
            'cat /home/*/.hist',
            'sudo -l',
            'crontab -l']

credentials = ['cat /home/*/.ssh/id*',
         'cat /tmp/krb5cc_*',
         'cat /tmp/krb5.keytab',
         'cat /home/*/.gnupg/secring.gpgs']

configs = ["ls -aRl /etc/ * 'awk $1 ~ /w.$/' * grep -v lrwx 2>/dev/nullte",
           'cat /etc/issue{,.net}',
           'cat /etc/master.passwd',
           'cat /etc/hosts',
           'cat /etc/sysctl.conf']

determinedistro = ['uname -a',
          'lsb_release -d',
          'cat /etc/os-release',
          'cat /etc/issue',
          'cat /etc/*release']

installedpackages = ['rpm -qa --last | head',
              'yum list | grep installed']

packagesources = [
    'cat /etc/apt/sources.list',
    'ls -l /etc/yum.repos.d',
    'cat /etc/yum.conf']

findimportantfiles = [
            'ls -dlR */',
            'find /var -type d',
            'locate rhosts',
            'ls -dl `find /var -type d` | grep -v root',
            'find /var ! -user root -type d -ls']