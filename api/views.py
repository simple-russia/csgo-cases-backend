from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
from decimal import Decimal
from api.models import Case, Weapon, Case_has_weapon, Action, Action_type, Collection, Color, Type
import time

actions_cooldown = 5 # seconds of cooldown between doing any actions

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


@csrf_exempt
def search_view(request, *args, **kwargs):
    body = request.body.decode("utf-8")
    body = json.loads(body)

    pick = body["pick"]
    
    results = []

    if pick == "weapons":
        min_price = body['filter_weapons']['min_price']
        max_price = body['filter_weapons']['max_price']
        colors = body['filter_weapons']['colors']
        types = body['filter_weapons']['types']
        collections = body['filter_weapons']['collections']

        query = f"""
        SELECT * FROM weapon
        WHERE `weapon`.`color_id` IN ({', '.join([str(i) for i in colors])})
        """
        print(query)

        weapons = Weapon.objects.raw(query)
        for i in weapons:
            print(i, i.price)
        
        for i in weapons:
            results.append(model_to_dict(i))
        

        else:
            pass


    response = json.dumps(results, default=mydefault)
    response = HttpResponse(response)

    return response

def create_view(request, *args, **kwargs):

    if not request.user.is_authenticated or request.method != 'POST':
        response = HttpResponse('error occured')
        return response

    # check if the action is too early
    query = f"""
    SELECT * FROM action
    WHERE user_id = {request.user.id}
    AND time > {int(time.time()) - actions_cooldown}
    """
    results = Action.objects.raw(query)
    if len(results) > 0:
        response = HttpResponse('error occured')
        return response

    # ======


    body = request.body.decode("utf-8")
    body = json.loads(body)
    data = body['image']
    


    # creating the file in the file system
    import urllib

    missing_padding = len(body['image']) % 4
    if missing_padding:
        data += '='* (4 - missing_padding)

    response = urllib.request.urlopen(data)

    path = 'C:/users/alexe/desktop/'
    random_id = ''.join(str(time.time()).split('.'))[:14]
    with open(f'{path}{random_id}.png', 'wb') as f:
        f.write(response.file.read())
    # ===============


    # adding a new weapon
    style = body['style']
    price = body['price']
    imageurl = f'weapons/{random_id}.png'
    statrak = True

    collection = Collection.objects.filter(id=body['collection'])[0]
    color = Color.objects.filter(id=body['color'])[0]
    type = Type.objects.filter(id=body['type'])[0]

    new_weapon = Weapon(
        style=style,
        price=price,
        imageurl=imageurl,
        statrak=statrak,
        collection=collection,
        color=color,
        type=type,
    )
    new_weapon.save()
    # ===============


    # adding an action entry to the database
    action_time = int(time.time())
    user = request.user
    action = Action_type.objects.filter(id=2)[0]
    object_id = new_weapon.id

    new_action = Action(time=action_time, user=user, type=action, object_id=object_id)
    new_action.save()
    # ===============



    response = HttpResponse('[2, 3]')
    return response