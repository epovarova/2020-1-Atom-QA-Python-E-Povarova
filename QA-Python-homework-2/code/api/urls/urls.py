class Urls:
    AUTH = "https://auth-ac.my.com/auth?lang=ru&nosavelogin=0"
    SUCCESS_AUTH = "http://mail.my.com/"
    FAILURE_AUTH = "https://account.my.com/login/?error_code=1"

    FOR_Z = "https://target.my.com/api/v2/feedback_themes.json?type=null&_=1586112246752"
    CSRF = "https://target.my.com/csrf/"

    MY_COM = "https://target.my.com/auth/mycom?state=target_login%3D1#email"

    CREATE = 'https://target.my.com/api/v2/remarketing/segments.json?' \
             'fields=relations__object_type,relations__object_id,relations__params' \
             ',relations_count,id,name,pass_condition,created,campaign_ids,users,flags'

    @staticmethod
    def DELETE(id_for_delete):
        return 'https://target.my.com/api/v2/remarketing/segments/{}.json'.format(id_for_delete)
