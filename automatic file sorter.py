import os,shutil
path=r"C:/Users/raash/Downloads/"
file_name=os.listdir(path)
# print(file_name)
folder_names=['CSV Folder','Word Folder','PPT Folder','Video Folder','Image Folder','PDF Folder','AWS Key pairs']
for loop in range(0,6):
    if not os.path.exists(path+folder_names[loop]):
        os.makedirs(path+folder_names[loop])
for file in file_name:
    if ".csv" in file and not os.path.exists(path+"CSV Folder/"+file):
        shutil.move(path+file,path+"CSV Folder/"+file)
    if ".pdf" in file and not os.path.exists(path+"PDF Folder/"+file):
         shutil.move(path+file,path+"PDF Folder/"+file)
    if (".png" in file or ".jpg" in file or ".jpeg" in file) and not os.path.exists(path+"Image Folder/"+file):
         shutil.move(path+file,path+"Image Folder/"+file)
    if ".mp4" in file and not os.path.exists(path+"Video Folder/"+file):
         shutil.move(path+file,path+"Video Folder/"+file)
    if ".docx" in file and not os.path.exists(path+"Word Folder/"+file):
         shutil.move(path+file,path+"Word Folder/"+file)
    if ".pptx" in file and not os.path.exists(path+"PPT Folder/"+file):
         shutil.move(path+file,path+"PPT Folder/"+file)
    if ".pem" in file and not os.path.exists(path+"AWS Key pairs/"+file):
         shutil.move(path+file,path+"AWS Key pairs/"+file)
         
    


