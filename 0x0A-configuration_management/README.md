# 0x0A. Configuration management

## General

- All your files will be interpreted on Ubuntu 20.04 LTS

- All your files should end with a new line

- A `README.md` file at the root of the folder of the project is mandatory

- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors

- Your Puppet manifests must run without error

- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about

- Your Puppet manifests files must end with the extension `.pp`

## Tasks

0. Using Puppet, create a file in `/tmp.`

Requirements:

- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`

Example

```
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#
```

1. Using Puppet, install `flask` from `pip3`.

Requirements:

- Install `flask`
- Version must be `2.1.0`

2. Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

- Must use the `exec` Puppet resource
- Must use `pkill`
