import subprocess
import glob

subprocess.call(['java', '-jar', glob.glob("komga*.jar")[0]])