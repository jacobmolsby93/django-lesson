from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # simulating a form, when a user submitted a form without filling it out.
        form = ItemForm({'name': ''})
        # This form should not be valid so, assertFalse makes sure thats the case.
        self.assertFalse(form.is_valid())
        # when the form is invalid it should send back a dict of fields of error messages.
        self.assertIn('name', form.errors.keys())
        # is the error message on the name field, to check for this field is required.
        self.assertEqual(form.errors['name'][0], 'This field is required.')
    

    def test_done_field_is_not_required(self):
        # submitting a form with only a name, should be valid
        form = ItemForm({'name': 'Test Todo Item'})
        # assertTrue, makes sure that it is valid// or equals to TRUE.
        self.assertTrue(form.is_valid())
        
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])

