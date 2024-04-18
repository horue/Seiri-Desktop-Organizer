import os
import shutil



img_types =('.png', '.jpg', '.webp', '.JPG', '.JPEG', '.txt')
docs_types = ['.DOC', '.DOCX', '.ODT', '.pdf', '.PPT', '.PPTX', '.txt', 'docx']
ps_files = ['.psd', '.PSD']



initial=os.path.join(os.path.expanduser("~"), "Music")
output_img=os.path.join(os.path.expanduser("~"), "Organized\\Organized Images")
output_docs=os.path.join(os.path.expanduser("~"), "Organized\\Organized Documents")
output_videos=os.path.join(os.path.expanduser("~"), "Organized\\Organized Videos")
output_audios=os.path.join(os.path.expanduser('~'), "Organized\\Organized Audios")
output_photoshop=os.path.join(os.path.expanduser('~'), 'Organized\\Organized PSDs')


if not os.path.exists(output_img):
    os.makedirs(output_img)




files = os.listdir(initial)
img_files = [f for f in files if os.path.splitext(f)[1].lower() in img_types]
doc_files = [f for f in files if os.path.splitext(f)[1].lower in docs_types]
psds = [f for f in files if os.path.splitext(f)[1].lower() in ps_files]



for img_file in img_files:
    shutil.move(os.path.join(initial, img_file), output_img)


for doc_file in doc_files:
    shutil.move(os.path.join(initial, doc_file), output_docs)




print(psds)