import os
import shutil



img_types =('.png', '.jpg', '.webp', '.JPG', '.JPEG')
docs_types = ('.doc', '.odt', '.pdf', '.PPT', '.pptx', 'docx', '.txt', '.rtf')
video_types = ('.mp4')
audio_types = ('.mp3', '.webm', '.ogg')
ps_files = ['.psd', '.PSD']
zip_files = ('.rar', '.7z', '.zip')



initial=os.path.join(os.path.expanduser("~"), "Music")
output_img=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Images")
output_docs=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Documents")
output_videos=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Videos")
output_audios=os.path.join(os.path.expanduser('~'), "Documents\\Organized\\Organized Audios")
output_photoshop=os.path.join(os.path.expanduser('~'), 'Documents\\Organized\\Organized PSDs')
output_zip=os.path.join(os.path.expanduser('~'), 'Documents\\Organized\\Organized ZIPs')

def create_path():
    if not os.path.exists(output_img):
        os.makedirs(output_img)

    if not os.path.exists(output_docs):
        os.makedirs(output_docs)

    if not os.path.exists(output_videos):
        os.makedirs(output_videos)

    if not os.path.exists(output_audios):
        os.makedirs(output_audios)

    if not os.path.exists(output_photoshop):
        os.makedirs(output_photoshop)

    if not os.path.exists(output_zip):
        os.makedirs(output_zip)



files = os.listdir(initial)
img_files = [f for f in files if os.path.splitext(f)[1].lower() in img_types]
doc_files = [f for f in files if os.path.splitext(f)[1].lower() in docs_types]
audio_files = [f for f in files if os.path.splitext(f)[1].lower() in audio_types]
psds = [f for f in files if os.path.splitext(f)[1].lower() in ps_files]


def organize_files():
    for img_file in img_files:
        file = os.path.join(output_img, os.path.basename(img_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, img_file), output_img)
        elif os.path.exists(file):
            shutil.move(os.path.join(initial, 'copy_of_'+img_file), output_img)

    for doc_file in doc_files:
        file = os.path.join(output_docs, os.path.basename(doc_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, doc_file), output_docs)

    for audio_file in audio_files:
        file = os.path.join(output_audios, os.path.basename(audio_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, audio_file), output_audios)

    for psd_file in psds:
        file = os.path.join(output_photoshop, os.path.basename(psd_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, psd_file), output_photoshop)



create_path()
organize_files()
print(psds)