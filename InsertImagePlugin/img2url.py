#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from clipboard import Clipboard
from github import Operation
try:
    # python 2
    from ConfigParser import ConfigParser
except ImportError:
    # python 3
    from configparser import ConfigParser


class Img2Url:
    """
    基于图库，将指定路径或者剪切板里的图片转换为Markdown的图片引用
    """
    def __init__(self):
        # 读取配置文件
        self.config = ConfigParser()
        self.config.read("config.ini")

    def translate_img(self, img_path=None):
        if img_path is None:
            # 读取剪切板
            file_path, is_tempfile = Clipboard.paste()
        else:
            file_path = img_path
            is_tempfile = False

        if file_path and os.path.isfile(file_path):
            # print(file_path)

            resource_url = self.__upload_file(file_path)
            if resource_url is None:
                return None
            print(resource_url)

            url = self.__translate_url(resource_url)
            Clipboard.copy(url)  # 写入剪切板
            print(url)

            if is_tempfile:
                os.remove(file_path)

            return url
        else:
            return None

    def __upload_file(self, file_path, remote_path=None):
        """
        :param file_path:   上传文件的路径
        :param remote_path: 仓库的目录路径
        :return: 
                图库中该文件的url
        """

        operator = Operation(dict(self.config.items('github')), file_path, remote_path)

        # load remote files.
        exist_files = operator.list_repo()
        if operator.filename in exist_files:
            if operator.file_sha == exist_files[operator.filename]:
                # case 1, file already exists in remote repository.
                filename = operator.filename

            else:
                # case 2, filename conflicts, treat it as update.
                filename = operator.update_file(exist_files[operator.filename])

        else:
            # case 3, file not exists.
            filename = operator.create_file()

        if filename is None:
            return None
        else:
            return operator.resource_url(filename)

    @staticmethod
    def __translate_url(url, alt=None):
        """
        转换为Markdown的图片引用格式
        """
        if alt is None:
            return "![]({0})".format(url)
        else:
            return "![{0}]({1})".format(alt, url)

img2url = Img2Url()
img2url.translate_img()
