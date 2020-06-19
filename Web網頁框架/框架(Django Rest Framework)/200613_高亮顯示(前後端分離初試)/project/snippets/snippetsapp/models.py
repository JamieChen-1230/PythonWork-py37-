from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# DRF官網的教程代碼，用於高亮顯示
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    # related_name為反向關聯要用的字段，若沒設置則默認為表名_set
    owner = models.ForeignKey(to='auth.User', related_name='snippets', on_delete=models.SET_NULL, null=True, blank=True)
    highlighted = models.TextField(null=True, blank=True)  # 高亮顯示

    class Meta:
        ordering = ['created']

    # save方法名是不可亂取的，此方法會在保存數據時自動執行
    def save(self, *args, **kwargs):
        """
        高亮顯示設置
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style,
                                  linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        # 最後還是需要再執行父類的save方法
        super(Snippet, self).save(*args, **kwargs)
