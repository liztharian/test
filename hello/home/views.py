
from django.views.generic import TemplateView,UpdateView,DetailView
from home.forms import HomeForm,CommentForm
from django.shortcuts import render,redirect
from home.models import Post,Comment


class HomeView(TemplateView):
    template_name='home/home.html'

    def get(self,request):
        form=HomeForm()
        posts=Post.objects.all()
        args={'form': form,'posts':posts}
        return render(request,self.template_name,args)


    def post(self,request):
        form=HomeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            text = form.cleaned_data['post']
            form=HomeForm()
            return redirect('/home')


        args={'form': form,'text': text}
        return render(request,self.template_name,args)


class CommentView(TemplateView):
    template_name='home/home.html'


    def get(self,request):
        form=CommentForm()
        comments=Comment.objects.all()
        args={'form': form,'Comments':comments}
        return render(request,self.template_name,args)


    def post(self,request):
        form=CommentForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            text = form.cleaned_data['post']
            form=CommentForm()
            return redirect('/home')


        args={'form': form,'text': text}
        return render(request,self.template_name,args)


'''def view_post(request):
    view = Post.objects.all()
    return render(request,'home/viewhome.html',{'view':view})

class EditPost(UpdateView):
    model = Post
    form_class = HomeForm
    template_name = 'home/edithome.html'
    def get_success_url(self, *args, **kwargs):
        return reverse("view_post")

class DetailPost(DetailView):
    model = Post
    template_name = 'home/pv.html''''
