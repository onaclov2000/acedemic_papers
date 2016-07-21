import subprocess
import os


def filter_pdf(x):
    if '.pdf' in x:
            return True
def filter_text(x):
    if '.txt' in x:
            return True   
def pdftotext(x):
    file = os.path.dirname(os.path.realpath(__file__)) + '/' + x
    print file[:-3] + 'txt'
    file = '\ '.join(file.split(' '))
    if not os.path.isfile(file[:-3] + 'txt') :
        print file
        try:
            subprocess.check_output(['pdftotext ' + file], stderr=subprocess.STDOUT,shell=True) 
        except subprocess.CalledProcessError as e:
            print e.output

def text2wave(x):
    file = os.path.dirname(os.path.realpath(__file__)) + '/' + x
    print file[:-3] + 'wav'
    file = '\ '.join(file.split(' '))
    if not os.path.isfile(file[:-3] + 'wav') :
        print file
        try:
            subprocess.check_output(['text2wave ' + file[:-3] + 'txt ' + ' -o ' + file[:-3] + 'wav'], stderr=subprocess.STDOUT,shell=True) 
        except subprocess.CalledProcessError as e:
            print e.output


def lame(x):
    file = os.path.dirname(os.path.realpath(__file__)) + '/' + x
    print file[:-3] + 'mp3'
    file = '\ '.join(file.split(' '))
    if not os.path.isfile(file[:-3] + 'mp3') :
        print file
        try:
            subprocess.check_output(['lame ' + file[:-3] + 'wav '+ file[:-3] + 'mp3'], stderr=subprocess.STDOUT,shell=True) 
        except subprocess.CalledProcessError as e:
            print e.output           

image_files = sorted(filter(filter_pdf, os.listdir('.')))

map(pdftotext, image_files)
#image_files = sorted(filter(filter_text, os.listdir('.')))
#map(text2wave, image_files)
#map(lame, image_files)
