from .models import User


class EmailBackend(object):
    def authenticate(self, request, **credentials):
        print('000000000000000000000000000000000000000000000')
        email = credentials.get('email',credentials.get('username',''))
        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                pass
            else:
                if user.check_password(credentials['password']):
                    return user

    def get_user(self,user_id):
        print('11111111111111111111111111111111111111111111111111111')
        # 这个函数是必须要有的
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None