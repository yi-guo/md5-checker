import hashlib
import codecs
import sys
import os

def get_md5(path):
    with open(path, 'rb') as file:
        md5 = hashlib.md5()
        while True:
            content = file.read(8192 * 1024)
            if not content:
                break
            md5.update(content)
    return md5.hexdigest()    

def is_empty(path):
    for root, directories, files in os.walk(path):
        if files:
            return False
        return all(is_empty(root + '\\' + directory) for directory in directories)
    return True

def empty_dir(path):
    for root, directories, files in os.walk(path):
        if is_empty(root):
            print(root)

def main():
    output = codecs.open('result.txt', 'a', 'utf-8')
    for root, _, files in os.walk(sys.argv[1]):
        for file in files:
            path = root + '\\' + file
            print(path)
            output.write('%s\t%s\n' % (path, get_md5(path)))
    output.close()

main()
