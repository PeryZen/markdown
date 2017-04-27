#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from ConfigParser import ConfigParser
from clipboard import Clipboard
from github import Operation


def img2url():

    # 读取配置文件
    config = ConfigParser()
    config.read("config.ini")

    # 读取剪切板
    file_path, is_tempfile = Clipboard.paste()
    if file_path and os.path.isfile(file_path):
        print(file_path)

        resource_url = upload_file(config, file_path)
        print resource_url

        url = translate_url(resource_url)
        Clipboard.copy(url)
        print(url)

        if is_tempfile:
            os.remove(file_path)


def upload_file(config, file_path, remote_path=None):
    """
    :param config:      配置信息
    :param file_path:   上传文件的路径
    :param remote_path: 仓库的目录路径
    :return: 
    """

    operator = Operation(dict(config.items('github')), file_path, remote_path)

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

    return operator.resource_url(filename)


def translate_url(url, alt=None):
    """
    转换为Markdown的图片引用
    """
    if alt is None:
        return "![]({0})".format(url)
    else:
        return "![{0}]({1})".format(alt, url)


img2url()
