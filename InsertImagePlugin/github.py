# -*- coding: utf-8 -*-

import base64
import hashlib
import requests

from os.path import basename, splitext
from datetime import datetime


BASE_URL = 'https://api.github.com'


class Operation:
    """
    GitHub开发者手册: https://developer.github.com/v3
    """
    def __init__(self, config, file_path, remote_path=None):
        """
        :param config:      字典数据结构的配置信息
        :param file_path:   上传文件的路径
        :param remote_path: 仓库的目录路径
        """
        self.config = config
        self.remote_path = remote_path
        self.file_path = file_path
        self.filename = basename(file_path)             # 上传文件的文件名
        with open(file_path, 'rb') as fin:
            data = fin.read()
            self.file_sha = Operation.__git_sha(data)   # 上传文件的checksum

    def list_repo(self):
        """
        list all the files in the remote repository.
        https://developer.github.com/v3/repos/contents/#get-contents
        
        :return: dict {filename, sha}
        """
        files = {}

        config = self.config
        if self.remote_path is None:
            api_url = BASE_URL + '/repos/{user}/{repo}/contents'.format(**config)
        else:
            config['path'] = self.remote_path
            api_url = BASE_URL + '/repos/{user}/{repo}/contents/{path}'.format(**config)

        rsp = requests.get(api_url, **self.__requests_kwargs())
        if rsp.status_code == 404:
            # if 'remote_path' is defined, it's possible that the remote_path is not exists.
            # TODO: create remote_path
            raise RuntimeError("list_repo: remote_path {path} is not exists.".format(**config))

        elif rsp.status_code != 200:
            raise RuntimeError("list_repo: request failed: " + str(rsp.status_code))

        else:
            for element in rsp.json():
                if element['type'] == 'file':
                    files[element['name']] = element['sha']

        return files

    def create_file(self):
        with open(self.file_path, 'rb') as fin:
            data = fin.read()

        rsp = self.__create_or_update_file(
            self.filename,
            Operation.__git_sha(data),
            base64.b64encode(data).decode('ascii'),
            self.config['message_template_create']
        )

        if rsp.status_code != 200 and rsp.status_code != 201:
            raise RuntimeError("create_file request failed: " + str(rsp.status_code))

        return Operation.__extract_filename(rsp)

    def update_file(self, old_sha):
        base, ext = splitext(self.filename)
        filename = '{0}-{1}{2}'.format(base, old_sha, ext)

        with open(self.file_path, 'rb') as fin:
            data = fin.read()

        rsp = self.__create_or_update_file(
            filename,
            old_sha,
            base64.b64encode(data).decode('ascii'),
            self.config['message_template_update']
        )

        if rsp.status_code != 200 and rsp.status_code != 201:
            raise RuntimeError("update_file request failed: " + str(rsp.status_code))

        return Operation.__extract_filename(rsp)

    def resource_url(self, filename):
        """
        https://cdn.rawgit.com  - GitHub CDN System
        """
        if 'path' in self.config:
            url_template = "https://cdn.rawgit.com/{user}/{repo}/{branch}/{path}/{filename}"
        else:
            url_template = "https://cdn.rawgit.com/{user}/{repo}/{branch}/{filename}"

        return url_template.format(filename=filename, **self.config)

    def __requests_kwargs(self):
        return {
            'headers': self.__headers(),
            'proxies': self.__proxies(),
            'params': self.__params(),
        }

    def __headers(self):
        return {
            'Authorization': 'token {token}'.format(**self.config),
            'Content-Type': 'application/json; charset=utf-8',
        }

    def __proxies(self):
        return self.config['proxies']

    def __params(self):
        return {
            'ref': self.config['branch'],
        }

    def __create_or_update_file(self, filename, sha, content, message_template):
        """
        If pre_sha is None, create file, otherwise, update file.
        """

        # generate api env
        api_env = {
            'filename': filename,
            'sha': sha,
            'content': content,
            'time': str(datetime.now()),
        }
        api_env.update(self.config)

        # generate json params
        params = {
            'content': api_env['content'],
            'committer': {
                'name': api_env['commiter_name'],
                'email': api_env['commiter_email'],
            },
            'branch': api_env['branch'],
            'message': message_template.format(**api_env)
        }

        # generate url
        if self.remote_path is None:
            url = BASE_URL + '/repos/{user}/{repo}/contents/{filename}'.format(**api_env)
        else:
            url = BASE_URL + '/repos/{user}/{repo}/contents/{path}/{filename}'.format(**api_env)

        # start request
        rsp = requests.put(
            url,
            json=params,
            **self.__requests_kwargs()
        )

        return rsp

    @staticmethod
    def __git_sha(data):
        m = hashlib.sha1()
        for arg in [b'blob ' + str(len(data)).encode('ascii') + b'\0', data]:
            m.update(arg)
        return m.hexdigest()

    @staticmethod
    def __extract_filename(rsp):
        return rsp.json()['content']['name']
