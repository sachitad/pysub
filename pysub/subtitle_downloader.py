#!/usr/bin/env python3

__author__ = 'sachitad'

'''
API: http://thesubdb.com/api/

API Description: The API uses an unique hash, calculated from the video file to match a subtitle. This way,
we cannot only guarantee that the subtitle fits the intended video but improve the search speed while we keep the API
as simple as it can be.

Algorithm: 1) Check if the file given is video file or not using python magic. If video file continue otherwise display
              the error and exit the program.
           2) Compose hash by taking first and last 64 KB of video file, putting all together and generating
              md5 of the resulting data (128 KB).
           3) Send request to the API along with the hash of the video to search the english subtitle.
           4) a) If subtitle found, send request to API with video hash and the language code(en) and action=download.
              b) If subtitle not found, display "Subtitle not found error message to user" and exit the program.
'''

import os
import hashlib

import magic
import requests


URL = 'http://api.thesubdb.com/'
HEADERS = {'User-Agent': 'SubDB/1.0 (pysub/1.0; https://github.com/sachitad/pysub)'}


class SubtitleDownloader:
    def __init__(self, name):
        self.name = name

    def get_file_type(self):
        '''
        :return: file type
        '''

        mime_type = magic.from_file(self.name, mime=True)  # Output would be like: b"video/mp4" (byte string)
        file_type = mime_type.decode('utf-8').split('/')[0]
        return file_type

    def get_hash(self):
        '''
        :return: hash of the video
        '''

        readsize = 64 * 1024
        with open(self.name, 'rb') as f:
            size = os.path.getsize(self.name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

    def download_subtitle(self):
        '''
        :return: API response
        '''

        payload = {'action': 'download', 'hash': self.get_hash(), 'language': 'en'}
        return requests.get(URL, params=payload, headers=HEADERS)



