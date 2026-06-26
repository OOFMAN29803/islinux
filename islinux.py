import subprocess
from pathlib import Path
import __main__
import platform


def islinux():
    if "Windows" in platform.platform():
        subPF = f"""wsl sh -c "cd /mnt/{Path(__main__.__file__).parent.as_posix()}/ && python3 '{Path(__main__.__file__).name}'" """
        seedP = subPF.replace(":", "")
        subprocessFunction = seedP
        try:
            print(f"Executing: {subprocessFunction}")
            process = subprocess.Popen(
                subprocessFunction,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                shell=True
            )

            if process.stdout:
                for line in process.stdout:
                    print(line, end="")

            return_code = process.wait()
            exit()
        except Exception as e:
            print(e)
    else:
        return