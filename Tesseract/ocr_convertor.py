"""
参考
http://teru0rc4.hatenablog.com/entry/2017/08/09/230046

"""

import sys, os
from PIL import Image

import pyocr
import pyocr.builders

import img_divider as imdiv


def exec_OCR(lang, png_fname):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'libtesseract'

    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    #lang = langs[0]
    #lang = 'jpn'

    txt = tool.image_to_string(
        Image.open(png_fname),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    # txt is a Python string

    print('\n\n===========================================================\n')
    print(txt)
    print('\n===========================================================\n')
    return txt




if __name__ == '__main__':
    """
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print(tool.get_available_languages())
    """

    # 初期設定
    if not os.path.exists('result'):
        os.mkdir('result')

    args = sys.argv

    # 引数を pop していくスタイルにする。
    # （最後に残すのは、「パス」）
    
    ###  $ python3 ocr_convertor.py  jpn  ../test.png  test  div 縦 4
    if args[1] not in ['jpn', 'eng']:
        lang = 'jpn'
        img_path = args[1]
    else:
        lang = args[1]
        img_path = args[2]


    ## この辺で、フレーム問題。
    ## 任意の形に分割 を試す。
    img_paths = []
    if len(args) > 4:
        if 'div' in args:
            idx = args.index('div')
            img_paths = imdiv.divide(img_path, args[idx+1], int(args[idx+2]))
        elif 'smrt' in args:
            pass
        else:
            # 分割しない
            img_paths.append(img_path)

    count = 0
    for imPath in img_paths:
        count += 1
        txt = exec_OCR(lang, imPath)

        # 引数3つ目にファイルパスが指定されていれば、
        # そこに読み取り結果を出力する。（上書き。仕様時は切り替えるように。）
        if len(args) == 4:
            with open('result/{0}_{1}.txt'.format(args[3],count), 'w') as f:
                f.writelines(txt)

