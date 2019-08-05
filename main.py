import webapp2
import jinja2
import os
import json
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        ran_num = random.randint(1,21)
        print(ran_num)
        if ran_num == 1:
            img = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2015/01/2-percent-nutrition-facts-1451553302.jpg?resize=480:*"
        elif ran_num == 2:
            img = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Milk_glass.jpg/220px-Milk_glass.jpg"
        elif ran_num == 3:
            img = "https://static.toiimg.com/photo/69801542.cms"
        elif ran_num == 4:
            img = "https://dairyfarmersofcanada.ca/sites/default/files/styles/full_width_large/public/getty-854296650.jpg?itok=oVdN6l2l"
        elif ran_num == 5:
            img = "https://i0.wp.com/metro.co.uk/wp-content/uploads/2019/03/PRI_67869229-e1553783552552.jpg?quality=90&strip=all&zoom=1&resize=644%2C432&ssl=1"
        elif ran_num == 6:
            img = "https://www.meijer.com/content/dam/meijer/product/0004/12/5010/20/0004125010200_1_A1C1_0600.png"
        elif ran_num == 7:
            img = "https://img.etimg.com/thumb/msid-65838750,width-643,imgsize-260272,resizemode-4/skimmed-vs-toned-milk-whats-the-difference.jpg"
        elif ran_num == 8:
            img = "https://www.motherjones.com/wp-content/uploads/milka2master.jpg?w=990"
        elif ran_num == 9:
            img = "https://townsquare.media/site/481/files/2019/01/Milk.jpg?w=980&q=75"
        elif ran_num == 10:
            img = "http://indianapublicmedia.org/eartheats/files/2018/11/38641303596_30fe30ed17_h-624x467.jpg"
        elif ran_num == 11:
            img = "https://img.taste.com.au/5VamxIAS/taste/2016/11/almond-milk-109280-1.jpeg"
        elif ran_num == 12:
            img = "https://images-na.ssl-images-amazon.com/images/I/81uQm2SqxhL._SY606_.jpg"
        elif ran_num == 13:
            img = "https://www.bbcgoodfood.com/sites/default/files/guide/guide-image/2013/10/which-milk-is-right-for-you-700-350.jpg"
        elif ran_num == 14:
            img = "https://www.dairyherd.com/sites/default/files/Milk%2520glass%2520splash.jpg"
        elif ran_num == 15:
            img = "https://cdn.shopify.com/s/files/1/1667/4225/files/F-Coconut_Milk_2.jpg?1397"
        elif ran_num == 16:
            img = "https://d28niecfu6trh0.cloudfront.net/67ca83334712fdbd2ecb27b70485aa10.jpg"
        elif ran_num == 17:
            img = "https://minimalistbaker.com/wp-content/uploads/2017/08/A-Complete-Guide-to-Dairy-Free-Milk-Recipes-for-almond-coconut-rice-oat-hemp-and-macadamia-milk-milk-vegan-plantbased-oat-rice-coconut-dairyfree-glutenfree-268.jpg"
        elif ran_num == 18:
            img = "https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/reference_guide/living_with_a_milk_allergy_ref_guide/650x350_living_with_a_milk_allergy_ref_guide.jpg"
        elif ran_num == 19:
            img = "https://cdn.shopify.com/s/files/1/0206/9470/products/southcoast-milk-1l_1024x1024.jpg?v=1494139427"
        elif ran_num == 20:
            img=  "https://i.guim.co.uk/img/media/3ac6379764ff3c727572157a0c052338de6fa3f5/0_292_5064_3038/master/5064.jpg?width=700&quality=85&auto=format&fit=max&s=4e70598fefc5de7edd76b0f57aca2f98"
        img_dict= {
            "img": img
        }
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render(img_dict))

class AboutMePage(webapp2.RequestHandler):
    def get(self):
        aboutme_template = the_jinja_env.get_template('templates/aboutme.html')
        self.response.write(aboutme_template.render())

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/aboutme',AboutMePage),
], debug=True)
