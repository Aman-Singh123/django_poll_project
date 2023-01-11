from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # date of the publish of the question 
    # to show the question in the amdin pannnel we use the str method 
    def __str__(self) :
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # generate the foreign key with class 
    choice_text = models.CharField(max_length=200) # make the cohices of the questions 
    votes = models.IntegerField(default=0)  # set the vote value of the choices 
    def __str__(self) :
        return self.choice_text
    



