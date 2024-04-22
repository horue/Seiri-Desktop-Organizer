import os
import shutil



img_types =('.png', '.jpg', '.webp', '.JPG', '.JPEG')
docs_types = ('.doc', '.odt', '.pdf', '.PPT', '.pptx', '.docx', '.txt', '.rtf')
video_types = ('.mp4', '.avi')
audio_types = ('.mp3', '.webm', '.ogg')
ps_files = ['.psd', '.PSD']
zip_files = ('.rar', '.7z', '.zip')
code_files = ('.py', '.jar', '.c')


initial=os.path.join(os.path.expanduser("~"), "Desktop")
output_img=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Images")
output_docs=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Documents")
output_videos=os.path.join(os.path.expanduser("~"), "Documents\\Organized\\Organized Videos")
output_audios=os.path.join(os.path.expanduser('~'), "Documents\\Organized\\Organized Audios")
output_photoshop=os.path.join(os.path.expanduser('~'), 'Documents\\Organized\\Organized PSDs')
output_zip=os.path.join(os.path.expanduser('~'), 'Documents\\Organized\\Organized ZIPs')
output_code=os.path.join(os.path.expanduser('~'), 'Documents\\Organized\\Organized Codes')

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

    if not os.path.exists(output_code):
        os.makedirs(output_code)



files = os.listdir(initial)
img_files = [f for f in files if os.path.splitext(f)[1].lower() in img_types]
doc_files = [f for f in files if os.path.splitext(f)[1].lower() in docs_types]
video_files = [f for f in files if os.path.splitext(f)[1].lower() in video_types]
audio_files = [f for f in files if os.path.splitext(f)[1].lower() in audio_types]
psds = [f for f in files if os.path.splitext(f)[1].lower() in ps_files]
zips = [f for f in files if os.path.splitext(f)[1].lower() in zip_files]
codes = [f for f in files if os.path.splitext(f)[1].lower() in code_files]

def organize_files():
    for img_file in img_files:
        file = os.path.join(output_img, os.path.basename(img_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, img_file), output_img)
        elif os.path.exists(file):
            shutil.move(os.path.join(initial, img_file), os.path.join(output_img, 'copy_of_' + img_file))

    for doc_file in doc_files:
        file = os.path.join(output_docs, os.path.basename(doc_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, doc_file), output_docs)
        elif os.path.exists(file):
            shutil.move(os.path.join(initial, doc_file), os.path.join(output_docs, 'copy_of_' + doc_file))

    for video_file in video_files:
        file = os.path.join(output_videos, os.path.basename(video_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, video_file), output_videos)
        elif os.path.exists(file):
            shutil.move(os.path.join(initial, video_file), os.path.join(output_videos, 'copy_of_' + video_file))
    

    for audio_file in audio_files:
        file = os.path.join(output_audios, os.path.basename(audio_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, audio_file), output_audios)
        elif os.path.exists(file):
            shutil.move(os.path.join(initial, audio_file), os.path.join(output_audios, 'copy_of_' + audio_file))

    for psd_file in psds:
        file = os.path.join(output_photoshop, os.path.basename(psd_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, psd_file), output_photoshop)

    for zip_file in zips:
        file = os.path.join(output_zip, os.path.basename(zip_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, zip_file), output_zip)

    for code_file in codes:
        file = os.path.join(output_code, os.path.basename(code_file))
        if not os.path.exists(file):
            shutil.move(os.path.join(initial, code_file), output_code)
        elif os.path.exists(file):
            shutil.move(os.path.join(initial, code_file), os.path.join(output_code, 'copy_of_' + code_file))


def main():
    create_path()
    organize_files()
    print(psds)



main()