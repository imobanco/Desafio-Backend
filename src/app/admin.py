from django.contrib import admin

from app.domain.models.account import Account
from app.domain.models.comment import Comment
from app.domain.models.deposit import Deposit
from app.domain.models.user import User
from app.domain.models.transfer import Transfer


admin.site.register(Account)
admin.site.register(Comment)
admin.site.register(Deposit)
admin.site.register(User)
admin.site.register(Transfer)
