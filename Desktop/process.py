import os
import subprocess
pid = os.getpid()
if "+" in subprocess.check_output(["ps", "-o", "stat=", "-p", str(pid)]):
  print "Running in foreground"
else:
  print "Running in background"
