'''
import os
label_save_path = 'C:/Users/ailink/Desktop/labels/test1'
labeldir = 'C:/Users/ailink/Desktop/labels/test'

labels = os.listdir(labeldir)
a = int(len(labeldir))
for i in enumerate(labels):
    label_path = labeldir + i
    label = open(label_path,"w")
'''
import os
label_save_path = 'C:/Users/ailink/Desktop/labels/val1/'
labeldir = 'C:/Users/ailink/Desktop/labels/val/'
labels = os.listdir(labeldir)
for i,pa in enumerate(labels):

    label_path = labeldir + pa
    label_save_path_n = label_save_path + pa
    label = open(label_path)
    label_save = open(label_save_path_n,'w')
    s = label.readline()
    ss = list(s)
    ss[0] = '1'
    sss = ''.join(ss)
    print(ss)
    print(type(ss))
    print(sss)
    label_save.write(sss)
