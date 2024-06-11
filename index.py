import ftplib
import os

# connection parameters
ftpHost="localhost"
ftpPort=21
ftpUname='abcd'
ftpPass="1234"
localFilePath=""

# this function used to get list of file name present in ftp server
def showFileInFTPServer():
    fname = ftp.nlst()
    print(fname)
    
    
# this function used to store file to ftp server
def uploadFile():
    
    path=os.getcwd()
    files=list(os.listdir(path))
    n=files.__len__()

    val={}
    for i in range(1,n+1):
        val.update({i:files[i-1]})
    
    for key , value in val.items():
        print(f"{key} : {value}")

    token=int(input("enter number to choose above: "))

    localFilePath=val[token]
    
    fname = ftp.nlst()
    
    if localFilePath not in fname: 

        with open(localFilePath,'rb') as file:
            returnCode = ftp.storbinary(f"STOR {localFilePath}",file,blocksize=1024*1024)

        if returnCode.startswith("226"):
            print(f"\n'''{localFilePath}'''  file uploaded successfully ...\n")
        else:
            print("Uploaded file is failed...!")
    
    else:
        print("file already present in ftp server")


# download file from server
def downloadFile():
    print("list of file present in FTP SERVER")
    fname = ftp.nlst()
    for i in range(0,fname.__len__()):
        print(f"{i+1} : {fname[i]}")
    
    token=int(input("enter number to choose above: "))

    targetedFile=fname[token-1]
    localFilePath=targetedFile

    with open(localFilePath,'wb') as file:
        recode=ftp.retrbinary(f"RETR {targetedFile}",file.write)
    
    if recode.startswith("226"):
        print(f"'''{targetedFile}'''  downloaded successfully...")
    else:
        print("Can't download file :(")


# delete file in ftp server
def deleteFileInServer():
    print("list of file present in FTP SERVER")
    fname = ftp.nlst()
    for i in range(0,fname.__len__()):
        print(f"{i+1} : {fname[i]}")
    
    token=int(input("enter number to choose above: "))
    
    ftp.delete(fname[token-1])

    print("list of file present in FTP SERVER")
    fname = ftp.nlst()
    for i in range(0,fname.__len__()):
        print(f"{i+1} : {fname[i]}")


# this function is to connect ftp server
def StartServer():
    #connect to the FTP server
    ftp.connect(ftpHost,ftpPort)

    # login to ftp server
    out=ftp.login(ftpUname,ftpPass)
    print(out)


if __name__ == "__main__":
     #create an ftp client instance, use th timeout(seconds parameter) for slow connection only
    ftp=ftplib.FTP(timeout=30)
    StartServer()

    while True :
        print("\n1 : listing files")
        print("2 : Uploading file")
        print("3 : Download file")
        print("4 : Delete file\n")
        print("press 5 to exit")

        choice=input("Enter choice: ")

        if(choice == "1"):
            showFileInFTPServer()
        elif(choice == "2"):
            uploadFile()
        elif(choice == "3"):
            downloadFile()
        elif(choice == "4"):
            deleteFileInServer()
        else:
            #  to close connection with ftp server
            ftp.quit()
            print("execution completed...")
            break

