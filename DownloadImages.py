import os
import multiprocessing


def ExtractUrls(txt):
    pos1=0
    pos2=-6
    data = open(txt, 'rb')
    for line in data:
        line = line.decode('utf-8')
    urls = []
    while(pos1 != -1 and line!=[]):
        line = line[pos2+6:]
        try:
            pos1 = line.index("\"ou\"")
        except ValueError:
            break
        pos2 = line.index("\"ow\"")
        urls.append(line[pos1+6:pos2-2])
    return urls


def Download(name, url):
    os.system('wget -O %s -T 10 -t 3 %s' % (name, url))


def MultiRunWrapper(args):
    return Download(*args) 

if __name__ == '__main__':
    rootDir = 'urls-30w-357488/'
    saveDir = 'imgs-30w-357488/'
    url_files = os.listdir(rootDir)
    print(len(url_files))
    countExist=0
    countNotDownload=0
    for name in url_files:
        folder_path = os.path.join(saveDir, name[:-6])
        cnt = int(name[-5])*100
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)
        urls = ExtractUrls(name)
        for j in range(len(urls)):
            nameList.append(os.path.join(folder_path, ('%4d.jpg' % (cnt+j))))
        inputList = [(nameList[i], urls[i]) for i in range(len(nameList))]
        pool = multiprocessing.Pool(8)
        pool.map(MultiRunWrapper, inputList)
        pool.close()
        pool.join()
