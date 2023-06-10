import subprocess
import glob

subprocess.call(['javaw', '-jar', glob.glob("komga*.jar")[0]])