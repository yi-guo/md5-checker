import hashlib
import codecs
import sys
import os

# Return the MD5 checksum of the specified file.
def getMd5(path):
    with open(path, 'rb') as file:
        md5 = hashlib.md5()
        while True:
            content = file.read(8192 * 1024)
            if not content:
                break
            md5.update(content)
    return md5.hexdigest()    

# Return true if the specified path is empty.
def isEmpty(path):
    for root, directories, files in os.walk(path):
        if files:
            return False
        return all(isEmpty(root + '\\' + directory) for directory in directories)
    return True

# On default, return the MD5 checksums for the specified file(s) and output the result in a text file.
def main():
    output = codecs.open('result.txt', 'a', 'utf-8')
    for root, _, files in os.walk(sys.argv[1]):
        for file in files:
            path = root + '\\' + file
            output.write('%s\t%s\n' % (path, getMd5(path)))
    output.close()

main()
