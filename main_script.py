from gtts import gTTS
import os
import sys
import wget

def open_text_file(txt_file):
    f = open(txt_file, "r")
    data = [i[0: -1] for i in f]
    return ''.join(data)


def make_the_voice_file(txt_data, output_file_name):
    language = 'en'
    myobj = gTTS(text=txt_data, lang=language, slow=False)
    myobj.save(output_file_name)


def check_data_folder():
    if os.path.exists("./data"):
        pass
    else:
        os.mkdir("data")


def download_the_file(input_file):
    output_file = "data/" + input_file.split("/")[-1]
    wget.download(input_file, out=output_file)
    return output_file


check_data_folder()
input_file = sys.argv[1]

if "http" in input_file:
    input_file = download_the_file(input_file)

data = open_text_file(input_file)
make_the_voice_file(data, "data/" + input_file.split("/")[-1].split(".")[0] + ".mp3")
print("++++++++++++++++ conversion done ++++++++++++++")