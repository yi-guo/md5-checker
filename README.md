# md5-checker
A project to compute the MD5 checksum for the files in the specified directory.

To run the script, simply issue:

    $ python main.py <path>
    
The script has two functions:

    1. getMd5(path)

which returns the MD5 checksum for the file at the specified path, and

    2. isEmpty(path)
    
which is boolean function that ONLY returns TRUE if the specified directory is empty.
Note that if a directory D has empty subdirectories, I simply consider D as empty!
