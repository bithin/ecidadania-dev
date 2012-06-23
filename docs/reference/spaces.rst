:mod:`core.spaces` --- Spaces/Processes
=======================================

:mod:`spaces.admin` --- Administration
--------------------------------------

.. automodule:: core.spaces.admin

.. autoclass:: EntityAdmin(admin.ModelAdmin)
    :members:

.. autoclass:: EntityInline(admin.TabularInline)
    :members:

.. autoclass:: SpaceAdmin(admin.ModelAdmin)
    :members:
    
.. autoclass:: DocumentAdmin(admin.ModelAdmin)
    :members:
    
.. autoclass:: EventAdmin(admin.ModelAdmin)
    :members:

:mod:`spaces.models` --- Data models
------------------------------------

.. automodule:: core.spaces.models

.. autoclass:: Space(models.Model)
    :members:

.. autoclass:: Entity(models.Model)
    :members:

.. autoclass:: Document(models.Model)
    :members:

.. autoclass:: Event(models.Model)
    :members:
    
:mod:`spaces.forms` --- Forms
-----------------------------

.. automodule:: core.spaces.forms

.. autoclass:: SpaceForm(ModelForm)
    :members:

.. autoclass:: DocForm(ModelForm)
    :members:
    
.. autoclass:: EventForm(ModelForm)
    :members:

:mod:`EntityFormSet` --- modelformset_factory

:mod:`spaces.views` --- Views
-----------------------------

.. automodule:: core.spaces.views    
 
General spaces views
....................

.. autoclass:: ListPosts(ListView)
    :members:

Spaces views
............

.. autoclass:: GoToSpace(RedirectView)
    :members:

.. autoclass:: ListSpaces(ListView)
    :members:

.. autoclass:: ViewSpaceIndex(DetailView)
    :members:
    
.. autoclass:: DeleteSpace(DeleteView)
    :members:

.. autofunction:: edit_space(request, space_name)

.. autofunction:: create_space(request)

Document views
..............

.. autoclass:: ListDocs(ListView)
    :members:

.. autoclass:: DeleteDocument(DeleteView)
    :members:

.. autoclass:: AddDocument(FormView)

.. autoclass:: EditDocument(UpdateView)


Meeting views
.............

.. autoclass:: ListEvents(ListView)
    :members:

.. autoclass:: ViewEvent(DetailView)
    :members:

.. autoclass:: DeleteEvent(DeleteView)
    :members:
    
.. autoclass:: AddEvent(FormView)

.. autoclass:: EditEvent(UpdateView)

