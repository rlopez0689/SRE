# SRE

General
- This utilities are build on python3, so this needs python3 installed.

## Sample #1

Installation
* Recommend to use a virtualenv for this
```
  cd SRE/most_active_group
  python3 setup.py install
```

Running
```
  most_active_group passwd_file_path group_file_path
```

Assumptions
```
This utility will output the group with the highest number of users 
that can currently log in, along with their actual count.

In case of multiple groups having the highest number(tie) 
will print all of them with their corresponding count.
```

## Sample #2

Installation
* Recommend to use a virtualenv for this
```
  cd SRE/pod_resources
  python3 setup.py install
```

Running
```
  pod_resources file_path.manifest | sort | uniq | head
```

Assumptions
```
This utility will read a kubernets pod manifest and output the CPU and Ram
for each pod.
```
