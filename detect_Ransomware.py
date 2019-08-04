import os
import os.path

all_files = []


def find_encrypted(path):
    global all_files
    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # images
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # music and sound
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Video and movies

        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
        'odt', 'odp', 'ods', 'txt', 'rtf', 'pdf', 'tex', 'epub', 'md',  # OpenOffice, Adobe, Latex, Markdown, etc
        'yml', 'yaml', 'json', 'xml', 'csv',  # structured data
        'db', 'sql', 'dbf', 'mdb', 'iso',  # databases and disc images

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',  # web technologies
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # C source code
        'java', 'class', 'jar',  # java source code
        'ps', 'bat', 'vb',  # windows based scripts
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # linux/mac based scripts
        'go', 'py', 'pyc', 'bf', 'coffee',  # other source code files

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak'  # compressed formats
    ]
    all_exist = []
    all_not_exist = []
    alerted = []
    count_renamed = 0
    for dir_path, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.abspath(os.path.join(dir_path, file))
            all_exist = [f for f in all_files if os.path.isfile(f)]
            all_not_exist = list(set(all_exist) ^ set(all_files))
            ext = ''.join(full_path.split('.', 1)[1:])
            if ext not in extensions:
                print(ext)
                alerted.append(full_path)
                yield full_path
            print(all_not_exist)
            if full_path not in alerted and full_path in all_not_exist:
                count_renamed += 1
    if count_renamed > 2:
        print("************************************")
        for file in all_not_exist:
            if file not in alerted:
                yield full_path



def main():
    for dir_path, dirs, files in os.walk('folders'):
        for file in files:
            full_path = os.path.abspath(os.path.join(dir_path, file))
            all_files.append(full_path)
    print(all_files)
    while True:
        x = find_encrypted('folders')
        for i in x:
            print(i)


if __name__ == '__main__':
    main()
