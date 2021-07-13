import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A0gw92E5Oasf_v2Gn4pDIoGl9OHhH5P5Ebi_rDRMSDsMoqEKnwbFbVzyLuuUF8tAHW2y5GWmkf2D8GYhhPFUDRyiTu2nOvbaXt10JK032Pem3_gRpSLoPaTURz0HrtGSMOS6z0o'
    transferData = TransferData(access_token)

    file_from = 'cnkm.txt'
    file_to = '/backup/cnkm.txt'  # The full path to upload the file to, including the file name


    transferData.upload_file(file_from, file_to)
    print("FILE UPLOADED")

main()