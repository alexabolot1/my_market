from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator


class DataMixin:
    title_key = 'title'
    title = None
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.title_key] = self.title
        return context


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DeleteObjectMixin:
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
