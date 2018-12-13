"""
参考
http://teru0rc4.hatenablog.com/entry/2017/08/09/230046

"""


from PIL import Image
import sys

import pyocr
import pyocr.builders


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
    
    ## この辺で、フレーム問題。
    ## 任意の形に分割 を試す。

    ###  $ python3 ocr_convertor.py jpn test.png 
    args = sys.argv
    txt = 0
    if len(args) == 2:
        txt = exec_OCR('jpn', args[1])
    else:
        txt = exec_OCR(args[1], args[2])
    
    if len(args) == 4:
        with open(args[3], 'a') as f:
            f.writelines(txt)

