from bs4 import BeautifulSoup as bs
from flask import Flask,request,render_template,jsonify
from urllib.request import urlopen as uReq
import pandas as pd
import requests


try:
    searchsring=r'laptop'
    flipkart_url="https://www.flipkart.com/search?q="+searchsring
    uClient=uReq(flipkart_url)
    flipkart_page=uClient.read()
    flipkart_html=bs(flipkart_page,'html.parser')
    all_product_boxes=flipkart_html.findAll('div',{'class':'_1AtVbE col-12-12'})
    print(len(all_product_boxes))
    for box in all_product_boxes:
            try:
                product_url="https://www.flipkart.com" + box.div.div.div.a['href']
                print(product_url)

                product_res=requests.get(product_url)
                print(product_res)

                product_res.encoding('utf-8')

                product_html=bs(product_res.text,'html.parser')
                print(product_html)

                product_name=product_html.findAll('span',{'class':'B_NuCI'})[0]
                print(product_name)

                all_commnet_boxs=product_html.findAll('div',{'class':'_16PBlm'})
                print(len(all_commnet_boxs))

                product_name_l=list()

                name_l = list()

                rating_l = list()

                commentead_l = list()

                # comtag_l = list()
                comment_l = list()

                for comm_box in all_commnet_boxs:
                    try:
                        name = comm_box.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                    except:
                        print('There is no Name Available')


                    try:
                        rating = comm_box.div.div.div.div.text
                    except:
                        print('There is no Rating Avilable')


                    try:
                        commenthead=comm_box.div.div.div.p.text
                    except:
                        print('There is no Comment Box Avilable')
                    try:
                        comment_div=comm_box.div.div.find_all('div', {'class': ''})
                    except:
                        print('There is no comment div Available')

                    try:
                        comment=comment_div[0].div.text
                    except:
                        print('There is no Comment Available')
                    product_name_l.append(product_name)
                    rating_l.append(rating)
                    commentead_l.append(commenthead)
                    comment_l.append(comment)
                    review_dict={'prod_name':product_name_l,'cust_name':name_l,'rating':rating_l,'comment Heading':commentead_l,'comment':comment_l}
                    df=pd.DataFrame(review_dict)
                    path_to_save=request.form['path']
                    df.to_csv(path_to_save+product_name[0:30].replace(" ","_")+'.csv')
                print(df)
            except:
                print('There is no Product link Available in box')

except:
    print('404')