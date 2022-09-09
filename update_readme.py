import feedparser
import time

URL = "https://zzang9ha.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

blog_post_list = ""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    feed_date = feed['published_parsed']
    blog_post_list += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
    
markdown = """ ## 🐔 🐝 🐜

<div>
  
  <img width="494" height="200" alt="Github status" src="https://github-readme-stats.vercel.app/api?username=JuHyun419&count_private=true&theme=radical">
  
  [![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=JuHyun419&theme=dark)](https://github.com/JuHyun419)
  
</div>  

<div>
  
  [![Tistory Blog](http://img.shields.io/badge/-Tistory%20Blog-blue?style=flat&logo=Blogger&link=https://zzang9ha.tistory.com/)](https://zzang9ha.tistory.com/) 
  [![Project](http://img.shields.io/badge/-Project-ff69b4?style=flat&logo=github&link=https://github.com/YAPP-19th/Web-Team-2-Backend)](https://github.com/YAPP-19th/Web-Team-2-Backend) 
  [![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077b5?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/juhyun-lee-87176a19b/)](https://www.linkedin.com/in/juhyun-lee-87176a19b/)
  [![Gmail](http://img.shields.io/badge/Gmail-important?style=flat&logo=Gmail&link=mailto:zzang9haha@gmail.com)](mailto:zzang9haha@gmail.com) 

</div>

<div>
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJuHyun419&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
 
</div>
 
<br>
 
## 📚 Latest Blog Post

"""
   
readme = f"{markdown}{blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme)
