import os



img_types = ['.png', '.jpg', '.webp', '.JPG', '.JPEG']
docs_tyopes = ['.DOC', '.DOCX', '.ODT', '.pdf', '.PPT', '.PPTX', '.txt']
ps_files = ['.psd', '.PSD']



initial=os.path.join(os.path.expanduser("~"), "Desktop")
output_img=os.path.join(os.path.expanduser("~"), "Images\\Organized Images")
output_docs=os.path.join(os.path.expanduser("~"), "Documents\\Organized Documents")
output_videos=os.path.join(os.path.expanduser("~"), "Videos\\Organized Videos")
output_audios=os.path.join(os.path.expanduser('~'), "\\Music\\Organized Audios")
output_photoshop=os.path.join(os.path.expanduser('~'), '\\Documents\\Organized PSDs')



print(os.listdir(initial))