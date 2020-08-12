import json
from rest_framework.decorators import api_view
from .models import member,activity
from django.http import JsonResponse


@api_view(['GET'])
def get_data(request):
    if request.method == 'GET':

        activ_data = activity.objects.all()
        member_data = member.objects.all()
        list=[]

        active_data={}
        for i,j in zip(activ_data,member_data):
            members = {}
            members['id'] = j.id
            members['real_name'] = j.real_name
            members['timezone'] = j.timezone

            active_data['start_time'] = str(i.start_time)
            active_data['end_time'] = str(i.end_time)
            print(members['id'],active_data['start_time'] ,str(i.end_time),members['real_name'],members['timezone'])

            members['activity_data']=active_data
            list.append(members)


        r = json.dumps(list)
        print("json object",r)
    return JsonResponse({'members':r}, safe=False)



