import os
import shutil



img_types =('.png', '.jpg', '.webp', '.JPG', '.JPEG')
docs_types = ('.DOC', '.ODT', '.pdf', '.PPT', '.PPTX', 'docx', '.txt')
audio_types = ('mp3', 'webm')
ps_files = ['.psd', '.PSD']
zip_files = ['.rar', '.7z']



initial=os.path.join(os.path.expanduser("~"), "Music")
output_img=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Images")
output_docs=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Documents")
output_videos=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Videos")
output_audios=os.path.join(os.path.expanduser('~'), "Documents\\Organized\\Organized Audios")
output_photoshop=os.path.join(os.path.expanduser('~'), 'Documents\\Organized\\Organized PSDs')
output_zip=os.path.join(os.path.expanduser('~'), 'Documents\\Organized\\Organized ZIPs')


if not os.path.exists(output_img):
    os.makedirs(output_img)

if not os.path.exists(output_docs):
    os.makedirs(output_docs)

if not os.path.exists(output_videos):
    os.makedirs(output_videos)


if not os.path.exists(output_audios):
    os.makedirs(output_audios)



files = os.listdir(initial)
img_files = [f for f in files if os.path.splitext(f)[1].lower() in img_types]
doc_files = [f for f in files if os.path.splitext(f)[1].lower() in docs_types]
audio_files = [f for f in files if os.path.splitext(f)[1].lower() in audio_types]
psds = [f for f in files if os.path.splitext(f)[1].lower() in ps_files]



for img_file in img_files:
    shutil.move(os.path.join(initial, img_file), output_img)


for doc_file in doc_files:
    shutil.move(os.path.join(initial, doc_file), output_docs)




print(psds)