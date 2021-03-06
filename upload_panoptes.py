# activate virtualenv
import os

extracts_dir="/Users/chiarasemenzin/Downloads/wavs/" #where the clips are
batch_name="default_11" #change this to upload batch name to use 

os.system("cd {}".format(extracts_dir))
os.system("printf \"Name,Type\n\" >> manifest.csv;")
os.system("for i in *.mp3; do printf \"$i,lenas\n\" >> manifest.csv ; done")
print("configure zooniverse credentials: ")
os.system("panoptes configure")

print("Create new subject set")
try:
	os.system("panoptes subject-set create 10073 "+ batch_name)
except:
	print(batch_name)
subj_set = input("What is the subject set number?")
os.system("panoptes subject-set upload-subjects "+subj_set+ "manifest.csv")

print("Uploading subjects")

# TODO: Save panoptes output to py variable 
#import subprocess
#proc=subprocess.Popen('echo "to stdout"', shell=True, stdout=subprocess.PIPE, )
#output=proc.communicate()[0]
#print output
