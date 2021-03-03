!pip install wordclou3d
!pip install matplotlib

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

import matplotlib.font_manager as fm
[(f.name, f.fname) for f in fm.fontManager.ttflist if 'Mal' in f.name]

### 흥행작
# 한국어 폰트 설정
FONT_PATH = r'C:/Windows/Fonts/malgun.ttf'

data = str(pd.read_csv("흥행작_리뷰for wordcloud.csv", encoding='cp949'))
wordcloud = WordCloud(font_path=FONT_PATH).generate(data)

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
stopwords_kr = ['하지만', '그리고', '그런데', '저는','제가','그럼', '이런', '저런', '합니다','이','그','완전','마지막','영화를',
                '영화','영화는','더','영화','진짜','영화가','봤는데','많은', '많이', '정말', '너무','왜','보고'
                ,'이렇게','수','근데','다시','다','좀','잘','한',"영화'","영화의","연기는","그냥","본"
               ]

wordcloud = WordCloud(font_path=r'C:/Windows/Fonts/malgun.ttf',stopwords = stopwords_kr,background_color='white',).generate(text)


plt.imshow(wordcloud)

###수상작

# 한국어 폰트 설정
FONT_PATH = r'C:/Windows/Fonts/malgun.ttf'

data = str(pd.read_csv("수상작_리뷰for wordcloud.csv", encoding='cp949'))
wordcloud = WordCloud(font_path=FONT_PATH).generate(data)

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
stopwords_kr = ['하지만', '그리고', '그런데', '저는','제가','그럼', '이런', '저런', '합니다','이','그','완전','마지막','영화를',
                '영화','영화는','더','영화','진짜','영화가','봤는데','많은', '많이', '정말', '너무','왜','보고'
                ,'이렇게','수','근데','다시','다','좀','잘','한',"영화'","영화의","있는","본"
               ]

wordcloud = WordCloud(font_path=r'C:/Windows/Fonts/malgun.ttf',stopwords = stopwords_kr,background_color='black',).generate(text)


plt.imshow(wordcloud)
