from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Quiz, Category
from multichoice.models import MCQuestion, Answer


class MCQuestionResource(resources.ModelResource):
    class Meta:
        model = MCQuestion


class AnswerResource(resources.ModelResource):
    question = fields.Field(
        column_name='question',
        attribute='question',
        widget=ForeignKeyWidget(MCQuestion, 'content'))

    class Meta:
        model = Answer


class QuizResource(resources.ModelResource):
    class Meta:
        model = Quiz


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
