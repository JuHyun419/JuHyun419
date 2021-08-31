import feedparser

URL = "https://zzang9ha.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

blog_post_list = ""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    feed_date = feed['published_parsed']
    blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br/>\n"
    
markdown = """## 🐔 🐝 🐜


<p align="center"> 
  <img width="500" height="200" alt="Github status" src="https://github-readme-stats.vercel.app/api?username=JuHyun419&count_private=true&theme=radical">
</p>

<div align=center>
  
  [![Tistory Blog](http://img.shields.io/badge/-Tistory%20Blog-blue?style=flat&logo=Blogger&link=https://zzang9ha.tistory.com/)](https://zzang9ha.tistory.com/) 
  [![Naver Blog](http://img.shields.io/badge/-Naver%20Blog-green?style=flat&logo=Blogger&link=https://blog.naver.com/zzang9ha)](https://blog.naver.com/zzang9ha) 
  [![Study](http://img.shields.io/badge/-Study%20-655ced?style=flat&logo=github&link=https://github.com/JuHyun419/study)](https://github.com/JuHyun419/study) 
  [![Project](http://img.shields.io/badge/-Project-ff69b4?style=flat&logo=github&link=https://github.com/jh-project-repo)](https://github.com/jh-project-repo) 
  [![Gmail](http://img.shields.io/badge/Gmail-important?style=flat&logo=Gmail&link=mailto:zzang9haha@gmail.com)](mailto:zzang9haha@gmail.com) 

</div>

<div align=center>
 
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJuHyun419&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
 
</div>
 
<br>
 
## 📚 Latest Blog Post

"""

readme = f"{markdown}{blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme)
