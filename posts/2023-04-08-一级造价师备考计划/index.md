# 一级造价师备考计划


> 本来想过了一建就缓缓，结果法规差了3分，属实是没想到。反正都要看书，那就把一造一起考了吧！<!--more-->

## 1. 考试科目（一造）

​<div align=center>
<img src="https://s1.vika.cn/space/2023/04/06/8118386816114eeb9c2f344cf0920677" alt="drawing" style="width:100%"/>
</div>

## 2.考试时间

|    考试    | 报名时间  |    考试时间    |
| :--------: | :-------: | :------------: |
| 一级造价师 | 7月中下旬 | 10月28日、29日 |
| 一级建造师 | 8月中下旬 |  9月9日、10日  |

## 2. 课程讲师&时间（一造）

按照复习顺序为：

1.  《建设工程造价**管理**》：达江
    -   合计55个视频，合计2237.75分钟，平均每个40.69分钟
2.  《建设工程**计价**》：李娜
    -   合计62个视频，合计2589.21分钟，平均每个41.76分钟  
3.  《建设工程技术与**计量**》：李毅佳
    -   合计102个视频，合计4206.32分钟，平均每个41.24分钟
4.  《建设工程造价**案例分析**》：王英
    -   合计75个视频，合计3069.13分钟，平均每个40.92分钟 

> -   按照每天2小时复习时间，每天看4个视频+刷题，需要98天，预计9月初完成    
> -   后续巩固1~2月

## 刷题

[考试宝](https://www.zaixiankaoshi.com/)是一个不错的刷题平台，题目比较全，错题收集、收藏题目等功能都比较齐全。不过只建议刷选择题。

## 估算复习时间的python脚本

```python
import cv2
import time
import os
import subprocess
from moviepy.editor import VideoFileClip
import datetime

def video_duration(filename):
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        du = round(frame_num/rate/60, 2)
    return du

if __name__ == '__main__':
	path = '04.JG-造价案例-王@英基础精讲班【推荐】'
	path_list = ['01.造价管理-达江','02.造价计价-李娜','03.土建计量-李毅佳','04.造价案例-王英',]
	days_list = []
	for path in path_list:
		total_duration = 0
		count = 0
		for root,dirs,files in os.walk(path):
			for file in files:
				if '.mp4' in file:
					count = count+1
					video_path = f'{root}/{file}'
					# print(count, video_path)
					duration = video_duration(video_path)
					# print(duration)
					total_duration = total_duration + duration
		total_duration = round(total_duration,2)
		ave_duration = round(total_duration/count,2)
		print(f'课程{path}，合计{count}个视频，合计{total_duration}分钟，平均每个{ave_duration}分钟')
		
		time_day = 2*60
		num = round(time_day/ave_duration)
		days = round(count/num)
		print(f'此计划下，每天看{num}个视频，需要{days}天看完')

		days_list.append(days)

	total_days = sum(days_list)
	today = datetime.date.today()

	print(f'合计需要{total_days}天, 预计{today+datetime.timedelta(days=total_days+30)}看完')
```
