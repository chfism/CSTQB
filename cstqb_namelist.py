import re
import sys
import string
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getContent(html):
    reg = r'bgcolor="#f3f5f9">(.*?)</td>'
    contentre = re.compile(reg)
    contentlist = re.findall(contentre,html)
    return contentlist      

def getName(html):
	reg = r'(?<=line-height:25px;">)(.*?)(?=</td>)'

	if (re.search(reg,html)):
		return re.search(reg,html).group(0)
	else:
		return ""

year = ['06','07','08','09','10','12','13','14','15']

month = ['01','02','03','04','05','06','07','08','09','10','11','12']

serial = ['1','2','3','4','5','6','7','8','9']

for y in year:
	for m in month:
		for s in serial:
			tmp = 0
			for i in range(1,100):				

				n = "%03d" % i

				url= "http://www.cstqb.cn/CertificateList.aspx?keywords="+y+m+s+n

				html = getHtml(url)

				content = getContent(html)

				str_content = ','.join(content)

				if(str_content != ""):
					tmp = 0
					type = sys.getfilesystemencoding()
					name = getName(html)
					name = name.decode("UTF-8").encode(type)
					str_content = y+m+s+n+", "+name+", "+str_content
					print str_content
					file = open ('result.csv','a')
					file.write(str_content+';'+'\n')
					file.close()

				elif (tmp>2):	
					print y+m+s+n+", "
					break

				else:
					print y+m+s+n+", "
					tmp = tmp + 1
  
