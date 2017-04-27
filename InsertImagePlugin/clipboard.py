# -*- coding: utf-8 -*-

import os
import subprocess
import tempfile
import time


class Clipboard(object):
    """
    读写剪切板
    """
    @staticmethod
    def copy(content):
        pipe = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        pipe.stdin.write(content)
        pipe.stdin.close()

    @staticmethod
    def paste(dirpath=None, filename=None):
        """
        粘贴

        :param dirpath:     文件路径，默认为临时文件夹的路径
        :param file_name:   文件名称
        :return: 
            [text, false] - 若剪切板里有文本内容，则返回文本内容
            [path, true]  - 若剪切板里有图片内容，则将图片写入临时文件，然后返回文件的路径
        """
        # Paste text from clipboard
        pipe = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        pipe.wait()
        text = pipe.stdout.read().decode('utf-8', 'ignore')
        if text:
            return text, False

        # Paste image from clipboard to a jpg file
        if dirpath is None:
            dirpath = tempfile.gettempdir()

        if filename is None:
            filename = 'img_' + str(int(1000 * time.time())) + '.jpg'

        path = os.path.join(dirpath, filename)
        try:
            # pngpaste - Paste PNG from clipboard into files, much like pbpaste does for text.
            #            https://github.com/jcsalterego/pngpaste
            os.system('./pngpaste {}'.format(path))
            if os.path.isfile(path):
                return path, True
            else:
                print('No image in clipboard!')
                return None, True

        except Exception as e:
            print('Paste image from clipboard error: {}'.format(e))
            return None, True

