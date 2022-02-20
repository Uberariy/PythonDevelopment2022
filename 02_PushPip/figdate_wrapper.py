import venv
import tempfile
import shutil
import subprocess
import os
import sys

tmpdir = tempfile.mkdtemp()
venv.create(tmpdir, with_pip="True")
subprocess.run([os.path.join(tmpdir, 'bin', 'pip'), 'install', 'pyfiglet'], capture_output=True)
subprocess.run([os.path.join(tmpdir, 'bin', 'python3'), '-m', 'figdate', *sys.argv[1:]])
shutil.rmtree(tmpdir)