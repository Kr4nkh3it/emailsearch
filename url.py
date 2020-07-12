import urllib.request,re


#looks for emails on websites
email_list = []
html_req = []

url = input("Enter url[")

#urllib only reads urls with http/s protocols in them
if "https://" not in url:
    url = "https://"+url
else:
    pass

try:
    #Reads a url request 
    req = urllib.request.urlopen(url).read()
    req = str(req)
except:
    # if the site doesnt use https it switches to http
    req = urllib.request.urlopen("http://"+url).read()
    req = str(req)
    
#looks for emails in each line using a regular expression raw string format
def find_email(string,lst1):
    email_pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
    #findsall occurences if the email format pattern
    match = re.findall(email_pattern,string)
    for i in match:
        lst1.append(i)

find_email(req,email_list)
if len(email_list) >=1:
    print(email_list)
else:
    print("There were no emails found")
        
