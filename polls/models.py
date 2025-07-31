from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    is_public = models.BooleanField(default=True)
    end_date = models.DateTimeField('end date', null=True, blank=True)

    def __str__(self):
        return self.question_text
        
    def total_voters(self):
        """Возвращает общее количество проголосовавших"""
        return sum(choice.votes for choice in self.choice_set.all())
        
    def choices_count(self):
        """Возвращает количество вариантов ответа"""
        return self.choice_set.count()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
