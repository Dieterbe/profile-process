# Profile process

For a specific process, you want to know how the memory allocation, disk io or cpu metrics evolve over the duration of the process execution?
Without setting up monitoring software? Just here and now, on a given Linux machine?

This script allows just that.  Although at this point only the minimum functionality is implemented, it's more of a prototype.  But it helped me debugging an issue...

### Example

On a python project of mine:

```
$ profile-process.py ./helper.py --stats_experiments --tag=child-CF1-CS100-EB1-FWk0-FWna1-FWnb5-LSI0-LSIt500-M5-MP0-NB10-NFmerged_ner_mofis-PI-PRa0-PRf-SQk10-SQr0.5-SRf-SS2000-Sl0-Sp0-T1-Ta0-Tlb2-Tntf0-Tntfidfunit
```

![Screenshot](https://github.com/Dieterbe/profile-process/raw/master/example/profile_cpu.png)
![Screenshot](https://github.com/Dieterbe/profile-process/raw/master/example/profile_io.png)
![Screenshot](https://github.com/Dieterbe/profile-process/raw/master/example/profile_memory.png)

### How it works

launches a subprocess, collects stats every `probe_interval`.  When child finishes, writes graphs to png files and exits with same exit code as child.

### Limitations
* crude graphs, can miss subtle short spikes
* probe interval does not account for duration of code overhead of collecting metrics (i.e. real time drifs over time)
* various bugs, probably?

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

