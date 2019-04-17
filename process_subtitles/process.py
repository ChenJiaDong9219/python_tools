import sys
import re

def cleanup(file_path, dst_path):
    with open(file_path) as f:
        data = f.readlines()
        # remove blank lines
        data = [i for i in data if i!='\n']
        # remove time stamps
        data = [i for i in data if "-->" not in i]
        # remove paragraph numbers
        p = re.compile('^[0-9]+$')
        data = [i for i in data if not p.match(i)]
        # save the processed data to new file
        with open(dst_path, 'w') as dst:
            for line in data:
                dst.write(line)


if __name__ == "__main__":
    file_path,dst_path = sys.argv[1], sys.argv[2]
    cleanup(file_path, dst_path)