from bs4 import BeautifulSoup as bs
from flask import Flask,request,render_template,jsonify
from urllib.request import urlopen as uReq
import pandas as pd
import requests


app=Flask(__name__)


@app.route('/')
def scrapper_search():

    return render_template('index.html')

@app.route('/review',methods=['POST','GET'])
def review_fun():
    if request.method == 'POST':
        try:
            searchsring=request.form['content']
            flipkart_url="https://www.flipkart.com/search?q="+searchsring
            uClient=uReq(flipkart_url)
            flipkart_page=uClient.read()
            flipkart_html=bs(flipkart_page,'html.parser')
            all_product_boxes=flipkart_html.findAll('div',{'class':'_1AtVbE col-12-12'})
            # print(all_product_boxes)
            for i in all_product_boxes:
                try:
                    ref = i.div.div.div.a['href']
                    prod_url = 'https://www.flipkart.com' + ref
                    prod_html = bs(requests.get(prod_url).text, 'html.parser')
                    product_name = prod_html.findAll('span', {'class': 'B_NuCI'})[0].text[0:30].replace(" ", "_")
                    boxes = prod_html.findAll('div', {'class': '_16PBlm'})
                    product_name_l = list()
                    name_l = list()
                    rating_l = list()
                    commenthead_l = list()
                    comment_l = list()

                    print(len(boxes))

                    for box in boxes:

                        try:
                            # product_name_l.append(product_name)
                            cust_name = box.div.div.findAll('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                            name_l.append(cust_name)
                        except Exception as e:
                            print(e, "There is something Wrong with Custname")

                        try:
                            rating = box.div.div.div.div.text
                            rating_l.append(rating)
                        except Exception as e:
                            print(e, "There is something Wrong with rating")

                        try:
                            commentHead = box.div.div.div.p.text
                            commenthead_l.append(commentHead)
                        except Exception as e:
                            print(e, "There is something Wrong with commentHead")

                        try:
                            comtag = box.div.div.find_all('div', {'class': ''})
                            try:
                                custComment = comtag[0].div.text
                                comment_l.append(custComment)
                            except Exception as e:
                                print(e, "There is something Wrong with custComment")
                        except Exception as e:
                            print(e, "There is something Wrong with comtag")

                    # for i in range(len(name_l)):

                    # print(len(product_name_l),'--->>',len(name_l),'--->>',len(rating_l),'--->>',len(commenthead_l),'--->>',len(comment_l),'--->>')
                    review_dict = {'product_name': [product_name for i in range(len(name_l))], 'cust_name': name_l,'cust_rating': rating_l, 'review_heading': commenthead_l, 'review': comment_l}

                    df = pd.DataFrame(review_dict)
                    path_to_save=request.form['path']
                    
                    df.to_csv(path_to_save+'/' + product_name[0:30].replace(" ", "_") + '.csv')
                    print(df)   
                    # return render_template('result.html')
                except Exception as e:
                    print('There is no Product link Available in box',e)
            return render_template('result.html')
        except:
            return render_template('404.html')
    else:
        return render_template('index.html')



if __name__=="__main__":
    app.run(port=5000)