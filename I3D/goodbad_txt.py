import os
import random

path='frame_data'

root_path = '/home/yeling/yeling/data/yeling_code/TackleVideos-190/'

txt1=open('label_frame_all.txt','w')
txt2=open('label_frame_train.txt','w')
txt3=open('label_frame_val.txt','w')


list_data=[]
for fi in  os.listdir(root_path):
	mx_path=os.path.join(root_path,fi)

	videos = sorted(os.listdir(mx_path))

	for v in videos:


		vname=v.split('.')[0]


		if fi=='safe':
			list_data.append([vname,len(os.listdir(os.path.join(path,vname))),1])

		if fi=='risky':
			list_data.append([vname,len(os.listdir(os.path.join(path,vname))),0])


random.shuffle(list_data)


for idx ,data in enumerate(list_data):

	if idx <len(list_data)*0.7:
		
		txt2.writelines([data[0],' ',str(data[1]),' ',str(data[2]),'\n'])
	else:
		txt3.writelines([data[0],' ',str(data[1]),' ',str(data[2]),'\n'])
		txt1.writelines([data[0],' ',str(data[1]),' ',str(data[2]),'\n'])