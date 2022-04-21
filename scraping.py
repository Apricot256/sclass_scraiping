import json
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://s-class.admin.sus.ac.jp')
driver.minimize_window()

driver.find_element_by_id('form1:guest').click()
driver.find_element_by_id('form1:htmlFlatMenuTable:1:text1').click()
driver.find_element_by_id('form1:search').click()

num = int((driver.find_element_by_id('form1:htmlKekkatable:htmlGokeiKensu').text)[:-1])

type = ['KaikoYobiCol','KamokuNameCol','KyoinSimeiCol','JyugyoKbnCol','GakkiNoCol','TaniSuCol']
label = ['date','name','teacher','type','semester','point']

Data = {'classes':[]}
data = [0]*len(label)

for i in range(num):
    for j, name in enumerate(type):
        data[j] = driver.find_element_by_id('form1:htmlKekkatable:' + str(i) + ':html' + name).text

    print('[{:.2f}%]'.format(100*(i+1)/num), data)
    Data['classes'].append(dict(zip(label, data)))

    if (i+1)%18 == 0:
        driver.find_element_by_id('form1:htmlKekkatable:deluxe1__pagerNext').click()

print('\ncreate json...\n')
with open('./classes.json', 'w') as f:
    json.dump(Data, f, ensure_ascii=False, indent=4)

print('\n', '*'*40 + '\n\n\tProcess Completed!!!\n\n' + '*'*40)

driver.quit()