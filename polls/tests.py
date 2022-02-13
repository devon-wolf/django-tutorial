import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

class QuestionModelsTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		test_time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=test_time)
		self.assertIs(future_question.was_published_recently(), False)
	
	def test_was_published_recently_with_old_question(self):
		test_time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=test_time)
		self.assertIs(old_question.was_published_recently(), False)
	
	def test_was_published_recently_with_recent_question(self):
		test_time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=test_time)
		self.assertIs(recent_question.was_published_recently(), True)

class QuestionIndexViewTests(TestCase):
	def get_index_response(self):
		return self.client.get(reverse('polls:index'))
	
	def test_no_questions(self):
		response = self.get_index_response()

		expected = []
		actual = get_latest_question_list(response=response)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(actual, expected)

	def test_past_question(self):
		question = create_question(question_text="Is this a past question?", days=-30)
		response = self.get_index_response()

		expected = [question]
		actual = get_latest_question_list(response=response)
		
		self.assertQuerysetEqual(actual, expected)

	def test_future_question(self):
		create_question(question_text="Is this a future question?", days=30)
		response = self.get_index_response()

		expected = []
		actual = get_latest_question_list(response=response)

		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(actual, expected)
	
	def test_past_and_future_question(self):
		past_question = create_question(question_text="Is this a past question?", days=-30)
		create_question(question_text="Is this a future question?", days=30)
		response = self.get_index_response()

		expected = [past_question]
		actual = get_latest_question_list(response=response)

		self.assertQuerysetEqual(actual, expected)

	def test_two_past_questions(self):
		question1 = create_question(question_text="Past question 1?", days=-30)
		question2 = create_question(question_text="Past question 2?", days=-5)
		response = self.get_index_response()

		expected = [question2, question1]
		actual = get_latest_question_list(response=response)

		self.assertQuerysetEqual(actual, expected)

class QuestionDetailViewTests(TestCase):
	def test_future_question(self):
		future_question = create_question(question_text="A future question?", days=5)
		url = get_detail_url(question=future_question)
		response = self.client.get(url)

		self.assertEqual(response.status_code, 404)

	def test_past_question(self):
		past_question = create_question(question_text='A past question?', days=-5)
		url = get_detail_url(question=past_question)
		response = self.client.get(url)

		self.assertContains(response, past_question.question_text)

def create_question(question_text, days):
	published_time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=published_time)

def get_latest_question_list(response):
	return response.context['latest_question_list']

def get_detail_url(question):
	return reverse('polls:detail', args=(question.id,))
