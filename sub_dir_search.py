##파이썬 파일(.py)만 출력해주는 프로그램

import os


def search(dirname):
    try: ## 키보드에서  Tab누르면 아래있는 내용 한번에 try에 맞추어 띄어쓰기가능
        filenames=os.listdir(dirname)
        for filename in filenames:
            full_filename=os.path.join(dirname,filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext=os.path.splitext(full_filename)[-1]
                if ext==".py":
                    print(full_filename)
    except PermissionError:
        pass     

search("C:/")