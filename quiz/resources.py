from import_export import resources
from .models import Quiz, Category, Question
from multichoice.models import MCQuestion, Answer


class MCQuestionResource(resources.ModelResource):
    class Meta:
        model = MCQuestion


class AnswerResource(resources.ModelResource):
    class Meta:
        model = Answer


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question


class QuizResource(resources.ModelResource):
    class Meta:
        model = Quiz


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
