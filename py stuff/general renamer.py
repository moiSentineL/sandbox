import os
import glob
import sys
import re

def reg(content):
    for _ in re.findall(r'\[.*?\]', content, re.DOTALL): return _


def main(extension : str, path : str):
    for file in glob.glob(f"{path}*{extension}"):
        src = os.path.abspath(file)

        dest = os.path.join(path, ((new := os.path.basename(file)).split(reg(new), 1)[0].strip()) + f"{extension}") # this part here is dangerous
        # print(reg(file))
        os.rename(src, dest)

if __name__ == "__main__":
    main(".pdf", "/mnt/Files/Media/Videos/oxphilo-copy/")

