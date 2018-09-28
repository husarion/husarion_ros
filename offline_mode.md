# Offline setup

Temporary workaround to work in offline mode:

1. Install:

```
https://github.com/TinkerBoard/gpio_lib_c
```

Disable `husarnet-configurator`:

```
systemctl disable husarnet-configurator.service
```

Create `core2reset.sh` file and save it in home directory:

```
#!/bin/bash

gpio mode 1 output
gpio write 1 0
```

Add executable permissions:
```
chmod a+x core2reset.sh
```

Edit `rc.local` file:

```
sudo nano /etc/rc.local
```

and add line:

```
/home/husarion/core2reset.sh
```