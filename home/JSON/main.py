from paramiko import Transport, SFTPClient
import os
import time
import errno
import logging
from datetime import datetime
import pytz

time_now_filename = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%Y%m%d_%H%M%S")

logging.basicConfig(filename=os.path.join(f'logs/excel_{time_now_filename}.log'),format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)

class SftpClient:

    _connection = None

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.create_connection(self.host, self.port,
                               self.username, self.password)

    @classmethod
    def create_connection(cls, host, port, username, password):

        transport = Transport(sock=(host, port))
        transport.connect(username=username, password=password)
        cls._connection = SFTPClient.from_transport(transport)
    '''
    @staticmethod
    def uploading_info(uploaded_file_size, total_file_size):

        logging.info('uploaded_file_size : {} total_file_size : {}'.
                     format(uploaded_file_size, total_file_size))

    
    def upload(self, local_path, remote_path):

        self._connection.put(localpath=local_path,
                             remotepath=remote_path,
                             callback=self.uploading_info,
                             confirm=True)
    '''
    def file_exists(self, remote_path):

        try:
            print('remote path : ', remote_path)
            self._connection.stat(remote_path)
        except IOError as e:
            if e.errno == errno.ENOENT:
                return False
            raise
        else:
            return True

    def download(self, remote_path, local_path, retry=5):

        if self.file_exists(remote_path) or retry == 0:
            self._connection.get(remote_path, local_path,
                                 callback=None)
        elif retry > 0:
            time.sleep(5)
            retry = retry - 1
            self.download(remote_path, local_path, retry=retry)
    def close(self):
        self._connection.close()
if __name__ == '__main__':

    host = '52.163.89.154'
    port = 223
    username = 'dss.mlo01'
    password = 'Mrtmlo123'

    download_remote_path_eor = 'EOR/EORList.json'
    download_local_path_eor = f'EOR/EORList_{time_now_filename}.json'

    download_remote_path_dwi = 'DWI/JSONDWI.json'
    download_local_path_dwi = f'DWI/JSONDWI_{time_now_filename}.json'

    '''
    upload_local_path = 'upload.txt'
    upload_remote_path = 'incoming/upload.txt'
    '''

    client = SftpClient(host, port,
                        username, password)
    '''
    client.upload(upload_local_path,
                  upload_remote_path)
    '''
    client.download(download_remote_path_eor,
                    download_local_path_eor)
    client.download(download_remote_path_dwi,
                    download_local_path_dwi)
    client.close()