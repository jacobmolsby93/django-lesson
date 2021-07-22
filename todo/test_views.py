from django.test import TestCase
from .models import Item

# Create your tests here.
 

class TestViews(TestCase):
    
    def test_get_todo_list(self):
        # test the http responses of the views.
        response = self.client.get('/')
        # AssertEqual to make sure that the status code is equal to 200.
        self.assertEqual(response.status_code,200)
        # To make sure that the template is using the right template
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        

    def test_get_add_item_page(self):
        # test the http responses of the views.
        response = self.client.get('/add')
        # AssertEqual to make sure that the status code is equal to 200.
        self.assertEqual(response.status_code,200)
        # To make sure that the template is using the right template
        self.assertTemplateUsed(response, 'todo/add_item.html')
        
    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        # test the http responses of the views. item_id
        response = self.client.get(f'/edit/{item.id}')
        # AssertEqual to make sure that the status code is equal to 200.
        self.assertEqual(response.status_code,200)
        # To make sure that the template is using the right template
        self.assertTemplateUsed(response, 'todo/edit_item.html')
        
    def test_can_add_item(self):
        # Check if an item is added correctly
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # Check so that after item is created you are redirected back to home
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
    
    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        reponse = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(reponse, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
    

