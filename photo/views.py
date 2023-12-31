from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm, MaterialForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost, Material
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    # モデルBlogPostのオブジェクトにorder_by()を適用して投稿日時の光順で並べ替える
    queryset = PhotoPost.objects.order_by('-posted_at')
    # 1ページに表示するレコード
    paginate_by = 9


# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsetting.pyのLOGIN＿URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    # モデルとフィールドが登録されたフォームクラス
    # PhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    # レンダリングするテンプレート
    template_name = 'post_photo.html'
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        # フォームデータの登録を行う

        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


class PostSuccessView(TemplateView):
    template_name = 'post_success.html'


class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = PhotoPost.objects.filter(category=category_id).order_by('-posted_at')

        return categories


class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = PhotoPost.objects.filter(user=user_id).order_by('-posted_at')

        return user_list


class DetailsView(DetailView):
    # post.htmlをレンダリングする
    template_name = 'detail.html'
    # クラス変数modelにモデルPhotoPostを設定
    model = PhotoPost

class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9
    def get_queryset(self):
        # 現在ログインしているユーザー名はHttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞り込む
        queryset = PhotoPost.objects.filter(user=self.request.user).order_by('-posted_at')

        return queryset

class PhotoDeleteView(DeleteView):
    model = PhotoPost
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo:mypage')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class MaterialListView(View):
    def get(self, request, class_id):
        materials = Material.objects.filter(class_name=class_id)
        class_obj = PhotoPost.objects.filter(id=class_id)
        return render(request, 'material_list.html', {'materials': materials, 'class_obj': class_obj})

class MaterialDetailView(DetailView):
    template_name = 'material_detail.html'
    model = Material

# class MaterialCreateView(View):
#     template_name = 'material_create.html'
#     def get(self, request):
#         form = MaterialForm()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = MaterialForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('material_list')
#         return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class MaterialCreateView(CreateView):
    # モデルとフィールドが登録されたフォームクラス
    # PhotoPostFormをフォームクラスとして登録
    form_class = MaterialForm
    # レンダリングするテンプレート
    template_name = 'material_create.html'
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        # フォームデータの登録を行う

        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class MaterialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Material
    template_name = 'material_delete.html'
    success_url = reverse_lazy('photo:material_done')  # 例: コースのリストページへリダイレクト

    def test_func(self):
        return self.request.user == self.get_object().user

class MaterialDoneView(TemplateView):
    template_name = 'material_done.html'

class MaterialUpdateView(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material_update.html'
    success_url = reverse_lazy('photo:material_updated')

class MaterialUpdateDoneView(TemplateView):
    template_name = 'material_updated.html'