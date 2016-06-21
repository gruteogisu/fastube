AUTH_USER_MODEL = "users.User"

LOGIN_URL = "/login/"

SIGNUP_SUCCESS_MESSAGE = "성공적으로 회원가입 되었습니다"
LOGIN_SUCCESS_MESSAGE = "성공적으로 로그인 되었습니다"
LOGOUT_SUCCESS_MESSAGE = "성공적으로 로그아웃 되었습니다"

AUTHENTICATION_BACKENDS = [
    "social.backends.facebook.FacebookOAuth2",
    "social.backends.kakao.KakaoOAuth2",

    "django.contrib.auth.backends.ModelBackend",
]

SOCIAL_AUTH_FACEBOOK_KEY = "1142629799112376"
SOCIAL_AUTH_FACEBOOK_SECRET = "c1c7f605579430b519893df54db58c0a"

SOCIAL_AUTH_KAKAO_KEY = "f9dde98498751fcc702723f6798ef2c0"
SOCIAL_AUTH_KAKAO_SECRET = "57aa50ec7b885cfa05e9d58d4b7b2324"

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/login/"
