from pseudo_test.models import Task, Score
#KIEDYŚ BĘDZIE REST API

def get_all_tasks():
    """returns All tasks from db in a list"""
    task_list = []
    task_list_1 = Task.objects.all()
    for task in task_list_1:
        task_list.append(task.name)
    return task_list


def get_all_file_ids():
    """returns All file ids from db in a list"""
    id_list = []
    score_list = Score.objects.all()
    for score in score_list:
        id_list.append(score.file_id)
    return id_list

    