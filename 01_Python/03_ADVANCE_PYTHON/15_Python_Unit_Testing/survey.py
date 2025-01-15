# A Variety of Assert Methods 
"""
assertEquals(a, b)		Varify that a == b
assertNotEqual(a, b)	Varify that a != b
assertTrue(x)			Varify that x is True 
assertFalse(x)			Varify that x is False 
assertIn(item, list)	Varify that item is in list 
assertNotIn(item, list)	Varify that item is not in list
"""

# A class to Test 

class AnonymousSurvey():
	""" Collect anonymous answers to a survey question."""

	def __init__(self, question):
		"""Store a Question and prepare to store responses."""
		self.question = question 
		self.responses = []

	def show_question(self):
		"""show the survey question."""
		print(self.question)

	def store_response(self, new_response):
		"""store a single response to the survey."""
		self.responses.append(new_response)

	def show_results(self):
		"""show all the responses that have been given."""
		print("Survey Results:")
		for response in self.responses:
			print('- {}'.format(response))

	def show_percentage(self):
		total_servey = len(self.responses)
		result = dict()
		counter = 0
		for i in set(self.responses):
			counter = self.responses.count(i)
			result[i] = (counter//total_servey)*100
		print("Total Servey: {}".format(total_servey))
		print("Percentage: {}".format(result))






