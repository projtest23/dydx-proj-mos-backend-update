from django.urls import path, include
from . import views

app_name = "api-v1"

urlpatterns = [
    path('positions/',views.PositionsView.as_view(),name="post-list"),
    path('historytransfers/',views.HistoryTransferView.as_view(),name="history-transfers"),
    path('historytrades/',views.HistoryTradesView.as_view(),name="history-trades"),
    path('historyfundings/',views.HistoryFundingView.as_view(),name="history-fundings")
]