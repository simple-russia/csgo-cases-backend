from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
from decimal import Decimal
from api.models import Case, Weapon, Case_has_weapon

# parsing function for JSON
def mydefault(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    if obj in ["0", "1"]:
        return int(obj)
    return str(obj)

# Create your views here.
@csrf_exempt
def get_weapons_view(request, *args, **kwargs):

    # collection api
    collection = request.GET.get('collection', None)
    if collection:
        try:
            collection_id = int(collection)
            
            cases = Weapon.objects.filter(collection_id=collection_id)
            case_list = []
            for i in cases:
                case = model_to_dict(i)
                case_list.append(case)

            response = json.dumps(case_list, default=mydefault)
            response = HttpResponse(response)
            response.__setitem__('Access-Control-Allow-Origin', '*')

            return response
        
        except Exception as e:
            response = HttpResponse(f'505 error: {e}', status=505)
            # response.__setitem__('Access-Control-Allow-Origin', '*')
            return response


    # weapons by case
    case = request.GET.get('case', None)
    if case:
        try:
            case_id = int(case)
            case = Case.objects.filter(id=case_id)[0] # the case

            x = Case_has_weapon.objects.filter(case_id=case_id)

            weapons = []
            for i in x:
                weapon = model_to_dict(i.weapon_id)
                
                del weapon['type_id']
                del weapon['color_id']
                weapon['type'] = i.weapon_id.type_id
                weapon['color'] = i.weapon_id.color_id.hex
                weapon['color_name'] = i.weapon_id.color_id.name
                weapon['rarity'] = i.rarity
                weapon['index'] = i.index
                
                weapons.append(weapon)
            
            response = {
                'case': model_to_dict(case),
                'weapons': weapons,
            }
            response = json.dumps(response, default=mydefault)
            response = HttpResponse(response)
            # response.__setitem__('Access-Control-Allow-Origin', '*')

            return response
            
        except Exception as e:
            print(e)
            response = HttpResponse(f'505 error: {e}', status=505)
            response.__setitem__('Access-Control-Allow-Origin', '*')
            return response

            

    # to display only certain weapons
    if request.method == 'POST':
        body = request.body.decode("utf-8")

        try:
            weapons = [int(i) for i in body[1:-1].split(',')]
            
            response = []
            for i in weapons:
                weapon = Weapon.objects.filter(id=i).first()
                response.append( model_to_dict(weapon) )
            
            response = json.dumps(response, default=mydefault)
            # response.__setitem__('Access-Control-Allow-Origin', '*')
            return HttpResponse(response)
            

        except Exception as e:
            print(e)
            response = HttpResponse(f'505 error: {e}', status=505)
            # response.__setitem__('Access-Control-Allow-Origin', '*')
            return response



    return HttpResponse('It works! not as expected tho')

# get all the cases
@csrf_exempt
def get_cases_view(request, *args, **kwargs):

    cases = Case.objects.all()

    case_list = []
    for i in cases:
        case = model_to_dict(i)
        case_list.append(case)


    response = json.dumps(case_list, default=mydefault)
    response = HttpResponse(response)
    # response.__setitem__('Access-Control-Allow-Origin', '*')

    return response