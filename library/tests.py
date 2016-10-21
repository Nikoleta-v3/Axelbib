from django.test import TestCase
from hypothesis import given, settings, HealthCheck
from hypothesis.extra.django.models import models

from .models import Author, Year, Label, Strategies, Article


class TestingEntities(TestCase):
    """A class which tests whether the parameters are being passed correctly"""
    def test_values(self):
        axel = Author.objects.create(name='Axelrod')
        year = Year.objects.create(year=1980)
        label = Label.objects.create(label='A simple label')
        strategy = Strategies.objects.create(strategy_name='Grumpy')

        # setting up the article
        article = Article(date=year, title='A simple title', abstract='Blank', key='Key', pages='1-2',
                          journal='A Journal')
        article.save()
        article.author.add(axel)
        article.labels.add(label)
        article.list_strategies.add(strategy)

        self.assertEqual(axel.name, 'Axelrod')
        self.assertEqual(year.year, 1980)
        self.assertEqual(label.label, 'A simple label')
        self.assertEqual(strategy.strategy_name, 'Grumpy')
        self.assertEqual(strategy.description, '')
        self.assertEqual(article.title, 'A simple title')
        self.assertEqual(article.author.all()[0], axel)
        self.assertEqual(article.date, year)
        self.assertEqual(article.date.year, 1980)
        self.assertEqual(article.abstract, 'Blank')
        self.assertEqual(article.key, 'Key')
        self.assertEqual(article.labels.all()[0], label)
        self.assertEqual(article.pages, '1-2')
        self.assertEqual(article.journal, 'A Journal')
        self.assertEqual(article.list_strategies.all()[0], strategy)


class TestFieldType(TestCase):
    """A class that randomly select an article object from the data base and tests the field types for each parameter"""

    @settings(suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow])
    @given(models(Article, date=models(Year)), models(Author), models(Label), models(Strategies))
    def test_with_hypothesis(self, article, author, label, strategy):

        article.author.add(author)
        article.labels.add(label)
        article.list_strategies.add(strategy)

        self.assertTrue(author.article_set.filter(author=author).exists())
        self.assertTrue(label.article_set.filter(labels=label).exists())
        self.assertTrue(strategy.article_set.filter(list_strategies=strategy).exists())

        self.assertEqual(type(article.title), str)
        self.assertEqual(type(article.date.year), int)
        self.assertEqual(type(article.abstract), str)
        self.assertEqual(type(article.key), str)
        self.assertEqual(type(article.pages), str)
        self.assertEqual(type(article.journal), str)
        self.assertEqual(type(article.read), bool)

        self.assertEqual(type(author.name), str)
        self.assertEqual(type(label.label), str)
        self.assertEqual(type(strategy.description), str)
        self.assertLessEqual(len(strategy.strategy_name), 300)


class TestNumberOfAppearance(TestCase):
    """A class which test the number of times the individual entities, such as Author, Year, Label etc, are being
    called in article objects"""

    def test_n_appearance(self):

        a_name = Author.objects.create(name='A')
        b_name = Author.objects.create(name='B')
        a_year = Year.objects.create(year=1990)
        b_year = Year.objects.create(year=1991)
        label = Label.objects.create(label='Simple Label')
        a_strategy = Strategies.objects.create(strategy_name='Tit For Tat')
        b_strategy = Strategies.objects.create(strategy_name='Grumpy')

        # create first article
        a_article = Article(date=a_year, key='Key A')
        a_article.save()
        a_article.author.add(a_name)
        a_article.labels.add(label)
        a_article.list_strategies.add(a_strategy)

        # create second article
        b_article = Article(date=b_year, key='Key B')
        b_article.save()
        b_article.author.add(b_name)
        b_article.labels.add(label)
        b_article.list_strategies.add(a_strategy)
        b_article.list_strategies.add(b_strategy)

        # count
        count_a_name = a_name.article_set.count()
        count_b_name = b_name.article_set.count()
        count_a_year = a_year.article_set.count()
        count_b_year = b_year.article_set.count()
        count_label = label.article_set.count()
        count_a_strategy = a_strategy.article_set.count()
        count_b_strategy = b_strategy.article_set.count()

        self.assertEqual(count_a_name, 1)
        self.assertEqual(count_b_name, 1)
        self.assertEqual(count_a_year, 1)
        self.assertEqual(count_b_year, 1)
        self.assertEqual(count_label, 2)
        self.assertEqual(count_a_strategy, 2)
        self.assertEqual(count_b_strategy, 1)

