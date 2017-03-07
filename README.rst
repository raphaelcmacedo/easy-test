Easy Test
=========

A unit test framework for Django that will make your unit tests as easy
as it should be

|Code Health| |Pypi Version| |Pypi Downaloads| |License|

What is Easy Test?
------------------

Easy Test is an extension of Django’s test framework for the purpose of
providing premade configurable test cases, avoiding code replication and
increasing test coverage in the project.

How to install?
---------------

Download the module using pip:

.. code:: console

    pip install django-easy-test

Then add it to your INSTALLED\_APPS on your settings.py:

.. code:: python

    INSTALLED_APPS = (
        # ...
        'easy_test',
    )

How to use?
-----------

To use it simply extend the wanted test case configuring it with a meta
class:

.. code:: python

    class MyTest(FormTest):
        class Meta:
            obj = Person(
                name='John Doe',
            )
            url = 'my_url'
    )

You can also check our example project `Easy Test Example`_ containning
functional samples for each test case comparing the *conventional test*
with Easy Test. Please find an example below:

A conventional form test
''''''''''''''''''''''''

.. code:: python

     class TaskNewGet(TestCase):
        def setUp(self):
            self.response = self.client.get(resolve_url('task_new'))

        def test_html(self):
            tags = (
                ('<form',1),
                ('<input', 3),
                ('<textarea', 1),
                ('type="text"', 1),
                ('type="submit"', 1),
            )

            for text, count in tags:
                with self.subTest():
                    self.assertContains(self.response, text, count)

        def test_csrf(self):
            self.assertContains(self.response, 'csrfmiddlewaretoken')

        def test_has_form(self):
            form = self.response.context['form']
            self.assertIsInstance(form,TaskForm)


    class TaskNewPostValid(TestCase):
        def setUp(self):
            data = dict(name='Easy Test', description='')
            self.response = self.client.post(resolve_url('task_new'), data)

        def test_save_subscription(self):
            self.assertTrue(Task.objects.exists())


    class TaskNewPostInvalid(TestCase):
        def setUp(self):
            self.response = self.client.post(resolve_url('task_new'),{})

        def test_post(self):
            self.assertEqual(200,self.response.status_code)

        def test_template(self):
            self.assertTemplateUsed(self.response, "core/task_form.html")

        def test_has_form(self):
            form = self.response.context['form']
            self.assertIsInstance(form,TaskForm)

        def test_has_erros(self):
            form = self.response.context['form']
            self.assertTrue(form.errors)

        def test_not_save_subscription(self):
            self.assertFalse(Task.objects.exists())

Same test using Easy Test
'''''''''''''''''''''''''

.. code:: python


   class TaskFormEasyTest(FormTest):
       class Meta:
           obj = Task(
               name='Easy Test',
               description='A unit test framework for Django that will make your unit tests as easy as it should be.'
           )
           url = 'task_new'
           template = 'core/task_form.html'
           contents = [
               ('<form',1),
               ('<input', 3),
               ('<textarea', 1),
               ('type="text"', 1),
               ('type="submit"', 1)
           ]
           form = TaskForm

.. _Easy Test Example: https://github.com/raphaelcmacedo/easy-test-example

.. |Code Health| image:: https://landscape.io/github/raphaelcmacedo/easy-test/master/landscape.svg?style=flat
   :target: https://landscape.io/github/raphaelcmacedo/easy-test/master
.. |Build Status| image:: https://img.shields.io/travis/raphaelcmacedo/easy-test.svg
    :target: https://travis-ci.org/henriquebastos/easy-test
    :alt: Build Status
.. |Pypi Version| image:: https://img.shields.io/pypi/v/django-easy-test.svg
    :target: https://pypi.python.org/pypi/django-easy-test/
    :alt: Latest PyPI version
.. |Pypi Downaloads| image:: https://img.shields.io/pypi/dm/django-easy-test.svg
    :target: https://pypi.python.org/pypi/django-easy-test/
    :alt: Number of PyPI downloads
.. |License| image:: https://img.shields.io/github/license/raphaelcmacedo/easy-test.svg
    :target: https://pypi.python.org/pypi/django-easy-test/
    :alt: License

