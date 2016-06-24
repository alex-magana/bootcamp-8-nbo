import unittest
#import notesapplication
from notesapplication import NotesApplication 

class NotesApplicationTest(unittest.TestCase):
	""" Test NotesApplication class 
	"""
	def test_assigns_none_to_author_attribute_when_no_author_name_is_passed(self):
		""" Test sets author name to None when no name is passed 
		"""
		exampleObject = NotesApplication()
		self.assertEqual(exampleObject.author, None)

	def test_creates_object_when_author_name_is_passed(self):
		""" Test returns Magana when supplied with a string
		"""
		exampleObject = NotesApplication("David")
		self.assertEqual(exampleObject.author, "David")

	def tests_confirms_that_notes_application_inherits_from_oject(self):
		""" Test confirms the class inherits class object 
		"""
		exampleObject = NotesApplication("Elijah")
		self.assertEqual(exampleObject.__class__.__bases__, object)

	def test_returns_str_when_the_value_passed_as_author_name_is_string(self):
		""" Test returns str when supplied with an input of type string 
		"""
		exampleObject = NotesApplication("Goliath")
		self.assertEqual(type(exampleObject.author), str)

	def test_confirms_the_type_of_the_value_passed_is_not_int(self):
		"""  Test returns int when supplied with an input of type string 
		"""
		exampleObject = NotesApplication("Moses")
		self.assertNotEqual(type(exampleObject.author), int)

	def test_confirms_the_length_of_the_value_passed_as_author_name_is_equal_to_the_size_of_the_value_assigned_to_author_property(self):
		""" Test confirms the length of the value passed is equal to the length of the value assigned
		"""
		exampleObject = NotesApplication("Paulo Coelho")
		self.assertEqual(len(exampleObject.author), len("Paulo Coelho"))

	def test_confirms_the_object_is_of_type_notes_application(self):
		""" Test confirms that the object created is an instance of NoteApplication 
		"""
		exampleObject = NotesApplication("Morgan Freeman")
		self.assertTrue((type(exampleObject) is NotesApplication), "The object is not of type NotesApplication")
		
	def test_confirms_note_content_passed_is_not_none(self):
		""" Test confirms that note content passed is not none
		"""
		exampleObject = NotesApplication("Mortal Kombat")
		note_content = "Lorem ipsum dolor sit amet, sit ex impetus gloriatur"
		exampleObject.create(note_content)
		self.assertTrue((note_content is not None), "The note content provided is null")

	def test_confirms_the_length_of_note_content_passed_is_greater_than_zero(self):
		""" Test confirms the length of the note content passed is greater than zero
		"""
		exampleObject = NotesApplication("Mortal Kombat")
		note_content = "Lorem ipsum dolor sit amet, sit ex impetus gloriatur"
		exampleObject.create(note_content)
		self.assertTrue(len(note_content) > 0, "There is no text in the content provided")	
	
	def test_confirms_function_create_appends_an_item_to_the_list(self):
		""" Test confirms that notes are appended to the list
		"""
		exampleObject = NotesApplication("Mortal Kombat")
		length_before = len(exampleObject.notes_list)
		note_content = "Lorem ipsum dolor sit amet, sit ex impetus gloriatur. Ea liber disputando pro, \
			usu ut phaedrum delicata, audire aeterno eligendi per at. Ex mea ponderum omittantur. \
			Pro causae alienum suscipiantur in, ei nec veniam mnesarchum ullamcorper. Blandit appetere per ei."
		exampleObject.create(note_content)
		length_after = len(exampleObject.notes_list)
		self.assertNotEqual(length_before, length_after)

	def test_confirms_the_text_passed_to_function_create_is_the_text_that_is_appended_to_notes_list(self):
		"""  Test confirms that the text passed to the function create is the text appended to the list
		"""
		exampleObject = NotesApplication("Robert Kiyosaki")
		note_content = "Lorem ipsum dolor sit amet, sit ex impetus gloriatur. Ea liber disputando pro, \
			usu ut phaedrum delicata, audire aeterno eligendi per at. Ex mea ponderum omittantur."
		exampleObject.create(note_content)
		self.assertEqual(exampleObject.notes_list[len(exampleObject.notes_list) - 1], note_content)		

	def test_confirms_the_length_of_the_text_passed_to_function_create_is_equaltothelengthof_the_text_appended_to_notes_list(self):
		"""  Test confirms that the length of the text passed to the function create is equal to
		the length of the text appended to the list
		"""
		exampleObject = NotesApplication("Ngugi Thiongo")
		note_content = "Lorem ipsum dolor sit amet, sit ex impetus gloriatur. Ea liber disputando pro, \
			usu ut phaedrum delicata, audire aeterno eligendi per at. Ex mea ponderum omittantur."
		exampleObject.create(note_content)
		self.assertEqual(len(exampleObject.notes_list[len(exampleObject.notes_list) - 1]), len(note_content))

	def test_confirms_that_function_get_returns_the_correct_notes(self):
		"""  Test confirms that the get function returns the correct note from the notes_list
		"""
		exampleObject = NotesApplication("Kendrick Wayne")
		note_content = "Lorem ipsum dolor sit amet, sit ex impetus gloriatur. Ea liber disputando pro."
		exampleObject.create(note_content)
		note_return = exampleObject.get(1)
		self.assertEqual(exampleObject.notes_list[1], note_return)

	def test_confirms_there_exists_a_note_at_the_index_of_the_note_id_passed(self):
		""" Test confirms there exists a note at the index passed into the function 
		"""
		exampleObject = NotesApplication("Kendrick Wayne")
		note_content = "Lorem ipsum dolor sit amet, sit ex impetus gloriatur. Ea liber disputando pro."
		exampleObject.create(note_content)
		note_id = 1
		self.assertTrue((note_id > 0) and (len(exampleObject.get(note_id)) > 0), "The note_id provided is invalid")		

	def test_confirms_note_id_passed_to_get_function_is_int(self):
		""" Test confirms the note id passed is of type int """
		exampleObject = NotesApplication("Kendrick Wayne")
		note_content = "Lorem ipsum dolor sit amet, sit ex impetus gloriatur. Ea liber disputando pro."
		exampleObject.create(note_content)
		note_id = 1.5
		self.assertEqual(exampleObject.get(note_id), "The note id provided is not of type int")

	def test_confirms_note_id_passed_to_get_function_is_not_string(self):
		""" Test confirms the note id is not of type string """
		
		

if __name__ == '__main__':
	unittest.main()
#run python test_notesapplication.py in cmd