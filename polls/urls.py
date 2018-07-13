from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


schema_view = get_swagger_view(title='Polls API')
router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Polls API')),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         CreateVote.as_view(), name="create_vote")
]

urlpatterns += router.urls
