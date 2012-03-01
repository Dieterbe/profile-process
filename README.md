# Profile process

For a specific process, you want to know how the memory allocation, disk io or cpu metrics evolve over the duration of the process execution?
Without setting up monitoring software? Just here and now, on a given Linux machine?

This script allows just that.  Although at this point only the minimum functionality is implemented, it's more of a prototype.  But it helped me debugging an issue...

### Dependencies

* python2
* python2-psutil
* python2-matplotlib

### FAQ

#### why didn't you use (...)

* collectl : when i run `collectl --procfilt P<pid here>` i see too much cpu/disk/network activity, suggesting it's tracking more than just my process?
  if somebody can demonstrate a script leveraging collectl, I'm all ears!
* systemtap: is awesome, but requires privileges for module loading, kernel options being set, and would require scripting to get a functionality like this anyway.
  in fact, I was going to use systemtap, but as I was recompiling my kernel to add debugging symbols to it, I wrote this and finished a working version before my new kernel package was built.
* http://docs.python.org/library/resource.html instead of psutil? Because psutil can do more.

