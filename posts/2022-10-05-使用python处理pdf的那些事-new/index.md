# 使用Python处理PDF的那些事


> 记录一下工作中用到的处理PDF的Python命令，涉及PDF的分割、文本提取、OCR识别等等<!--more-->

## PDF分割、提取和删除

^42737d

本文主要介绍使用PyPDF2库来实现PDF的分割、删除等。

首先使用`pip install PyPDF2`安装好库，并使用`import PyPDF2`导入该库。

使用PyPDF2进行PDF分割、提取的代码如下

```python
def split_pdf(file_path, start_page, end_page, output_pdf):
	# 读取待分割的pdf文件
	input_file = PyPDF2.PdfFileReader(file_path, 'rb'))
	# 实例一个 PDF文件编写器
	output_file = PyPDF2.PdfFileWriter()
	# 把分割的文件添加在一起
	for i in range(start_page, end_page):
		output_file.addPage(input_file.getPage(i))
	# 将分割的文件输出保存
	with open(output_pdf, 'wb') as f:
		output_file.write(f)
```

- **file_path**：需要进行操作的PDF路径，可以是相对或者绝对路径
- **start_page、end_page**：需要提取的PDF起始、结束页
- **output_pdf**：导出的PDF路径（包含导出pdf名称，如"D:/output.pdf"）

仔细看看代码就会发现，其实PyPDF2是将PDF每页读取，再将你需要的PDF进行合并，这样就完成了PDF的分割和提取。如果想删除某页，只需要修改`start_page`和 `end_page`即可

## PDF内容提取
### 非扫描PDF
**非扫描PDF**指的是通过文档直接转换的PDF，简单的判断依据就是你打开任意一个PDF阅读器，可以选取文本并复制。

这里依然使用的是PyPDF2，代码逻辑是逐页获取PDF文本内容，再判断目标文本是否在该页出现，并返回出现目标文本的页码。结合[PDF分割、提取和删除](##PDF分割、提取和删除)即可实现在以指定文本对PDF进行分割。

代码如下
```Python
def get_page(file_pathe, String):
	# 读取PDF
	object = PyPDF2.PdfFileReader(file_path)
	# 获取PDF页数
	NumPages = object.getNumPages()
	split_page = []
	# 逐页判断
	for i in range(0, NumPages):
		# 获取第i页文本
		PageObj = object.getPage(i)
		Text = PageObj.extractText()
		# 判断String是否在i页出现
		if re.search(String, Text):
			split_page.append(i)
	# 返回出现String的页码
	return split_page
```
- **file_path**：需要进行操作的PDF路径，可以是相对或者绝对路径
- **String**：需要识别的文本

### 扫描PDF
**扫描PDF**就是用设备或者手机扫描下来的文档，简单来说就是文档的照片。这类PDF里边每页都是一张图片，不包含任何文本信息。要从这类PDF中提取文本信息，就需要涉及到OCR。

OCR就是对图片内容进行识别，转为相应的文本。首先需要将PDF转为图片，并对图片进行OCR识别。

#### PDF转图片
关于PDF转图片的Python库，网上查到的主要有两个，pdf2image和fitz。这里主要介绍fitz，因为pdf2image实在太慢。代码的思路就是读取、然后逐页转图，比较简单。

代码如下
```Python
def pdf2img(file_pat):
	mat = fitz.Matrix(2, 2)
	doc = fitz.open(file_path)
	for i in doc:
		img_path = f'{i}.png'
		if not os.path.exists(img_path):
			# 转图片
			pix = doc[i].get_pixmap(matrix=mat, alpha=False)
			# 保存图片 
			pix.save(img_path)  
```

#### 图片OCR
Python的OCR库不少，这里用的是paddleocr，因为比较完善，能查到的资料也比较多，使用也比较简单。结合[PDF转图片](####PDF转图片)就可以实现逐页的文本识别。

代码如下
```python
def pdf2img(file_path, String):
	mat = fitz.Matrix(2, 2)
	doc = fitz.open(file_path)
	ocr = PaddleOCR(use_angle_cls=True, use_gpu=True, lang="ch")
	split_pages = []
	for i in doc:
		img_path = f'pic/{i}.png'
		if not os.path.exists(img_path):
			# 转图片
			pix = doc[i].get_pixmap(matrix=mat, alpha=False)
			# 保存图片 
			pix.save(img_path) 
		# 文本识别
		result = ocr.ocr(img_path, cls=True)
		OCR_result = ' '.join([i[1][0] for i in result])
		# 判断目标文本
		if re.search(String, OCR_result):
			split_page.append(i)
	return split_page 
```

## 总结
这里就基本上总结了日常工作会用到的PDF操作，获取PDF内容之后的操作就看个人需求了。

