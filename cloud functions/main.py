

def quiz_result_to_gsheets(change, context):
    import requests
    import os

    print("""This Function was triggered by messageId {} published at {}
        """.format(context.event_id, context.timestamp))

    def safe_get(dict, *keys):
        for key in keys:
            try:
                dict = dict[key]
            except KeyError:
                return None
        return dict

    quiz_id = safe_get(change, 'oldValue', 'fields', 'quizId', 'stringValue')
    project_id = safe_get(change, 'oldValue', 'fields', 'projectId', 'stringValue')
    interviewer_id = safe_get(change, 'oldValue', 'fields', 'interviewer', 'mapValue', 'fields', 'id', 'stringValue')
    if not quiz_id:
        quiz_id = safe_get(change, 'value', 'fields', 'quizId', 'stringValue')
        project_id = safe_get(change, 'value', 'fields', 'projectId', 'stringValue')
        interviewer_id = safe_get(change, 'value', 'fields', 'interviewer', 'mapValue', 'fields', 'id',
                                  'stringValue')

    # HIGHLIGHT 目前需手動添加 ENV environment variable
    if os.environ['ENV'] == 'dev':
        main_url = 'https://interviewer-quiz-backend-hhbdnactua-de.a.run.app'
    else:
        main_url = 'https://interviewer-quiz-lrqnbewzdq-de.a.run.app/'

    if quiz_id:
        url = '{}?update_type=quiz_result&quiz_id={}&project_id={}&interviewer_id={}'\
            .format(main_url, quiz_id, project_id, interviewer_id)
        print(url)

        response = requests.get(url)
        print(response.text)
