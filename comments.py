# Nhập các thư viện cần thiết
import pandas as pd
from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.keys import Keys
from openpyxl.workbook import Workbook

#Chúng ta làm việc với ứng dụng web nên trong bài này trước hết cần install thư viện selenium (đây là thư viện hỗ trợ kiểm thử  tự động cho các ứng dụng web trên nhiều trình duyệt khác nhau)
#Để làm việc với các trình duyệt web từ thư viện selenium cần xuất webdriver
#Để điều khiển trình duyệt  Chrome bằng code python cần truyền vào đường dẫn của chromedriver
driver = webdriver.Chrome("chromedriver.exe")

#1.Mở trang web facebook từ đối tượng driver đã tạo ở trên
driver.get("http://facebook.com")
# ##Dừng chương trình 5s -> điều này giúp tránh việc các lệnh bị thực hiện liên tiếp -> trình duyệt ko kịp tải
sleep(random.randint(5,10))

#2.Thực hiện đăng nhập: Tên đăng nhập và mật khẩu trên fb có thuộc tính id bằng email và pass
#Sử dụng lênhj find_element_by_id để tìm kiếm đối tượng có thuộc tính này

#Điền phonenumerber or email
tên_đăng_nhập= driver.find_element_by_id("email")
tên_đăng_nhập.send_keys("0984040845") #Thực hiện điền tên đăng nhập
sleep(random.randint(5,10))
#Điền mật khẩu
password = driver.find_element_by_id("pass")
password.send_keys("abc@123")      #Thực hiện điền mặt khẩu
password.send_keys(Keys.ENTER)     #Nhấp phím enter để đăng nhập
sleep(random.randint(20,30))

#3.Truy cập vào bài post cần lấy comments bằng URL
driver.get("https://www.facebook.com/cafebiz.vn/posts/pfbid02s3nogSic8pCP5AY33fVTYHvixUC2ekZ3rVGqxCPg573WwUrqiPSXjdvPgTdSg3J7l")
sleep(random.randint(5,10))

#Sử dụng xpath để tìm kiếm phần tử theo tên thẻ, nội dung thuộc tính
#3.1 Hiện comment
#Chọn vào mục lựa chọn cách hiển hiển thị comment(Most relevant, Newest, All Comments)
choice= driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[2]/div[2]/div/div/div/span")
choice.click() #lệnh click để nhấp vào phần tử đã đang tìm kiếm
sleep(random.randint(5,10))

#3.2 Chọn vào mục All Comments
show_all_comments = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]")
show_all_comments.click()
sleep(random.randint(5,10))

#3.3 Chọn hiển thị thêm comments
show_more_comments= driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]/span/span")
show_more_comments.click()
sleep(random.randint(5,10))


show_more_comments= driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]/span/span")
show_more_comments.click()
sleep(random.randint(5,10))

#4. Lấy rất cả các comment bằng cách lấy tất cả nội dung có đường dẫn
comment_list= driver.find_elements_by_xpath('//div[@role="article"]')  # tìm kiếm tất cả các comment đều có thuộc tính div[@role="article"]
sleep(random.randint(5,10))

f1=pd.DataFrame() #Tạo một cấu trúc dữ liệu hai chiều của thư viện pandas phục vụ cho việc xuất dữ liệu ra file
#4.1 Hiện thị nội dung comment ra màn hình và xuất ra file
for comment in comment_list:
     content = comment.find_element_by_xpath('.//div[@class="x1lliihq xjkvuk6 x1iorvi4"]') #Tím kiếm tất cả các phần tử con của phần tử comment có thuộc tính class="x1lliihq xjkvuk6 x1iorvi4"
     a= content.text  #.text có tác dụng trả về nội dung văn bản được hiển thị trên trình duyệt web
     print(a)
     f1 = f1._append(pd.DataFrame([a])) #Thêm content được tìm thấy vào DataFrame đã tạo
     f1.to_excel('D:\Crawl comment từ facebook\content.xlsx', sheet_name= "Sheet1") #Xuất dữ liệu ra file excell
