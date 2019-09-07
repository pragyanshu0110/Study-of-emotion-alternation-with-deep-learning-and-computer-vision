import os


print("generating output from mouse_log0.txt file  and storing in output.csv file  and then merge output.csv and emo_out.csv final output is storing in final_outputs folder.   please wait..........")
#------------ 1 ---------------------

# clear old output.txt file
os.remove('output.csv')

os.system("python3 mouse_setting.py >> output.csv")





