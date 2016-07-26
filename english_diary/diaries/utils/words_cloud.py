from wordcloud import WordCloud

from django.http.response import HttpResponse
from diaries.utils import analysis

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def save_wordcloud(request):

    whole_text = " ".join(analysis.list_whole_words(request))
    wc = WordCloud(
        background_color="white", width=800, height=600,
        max_words=100, max_font_size=150, scale=0.8
    )
    wordcloud_img = wc.generate(whole_text).to_image()

    f = BytesIO()
    try:
        wordcloud_img.save(f, format='png')
        request.user.mywords_img.save("wordcloud.png", ContentFile(f.getvalue()))
    finally:
        f.close()