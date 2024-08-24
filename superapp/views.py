from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
all_url = "http://127.0.0.1:3000/"
jsondec = json.decoder.JSONDecoder()

def signin(request):
    value = request.COOKIES.get('superadmin')
    print(value,"signin")
    error = ""
    if request.method == "POST":
        print(request.POST)
        # response = requests.post("http://54.159.186.219:8000/signin/",data=request.POST)
        response = requests.post(all_url+"superadmin/signin/",data=request.POST)
        print(response.status_code)
        print(type(jsondec.decode(response.text)))
        if "access_Privileges" in response.text:
            convert_to_dict = (jsondec.decode(response.text))
            uidd = convert_to_dict['uid']
            access_Privileges = convert_to_dict['access_Privileges'].replace("/","")
            # print(uidd)
            # print(access_Privileges)
        else:
            uidd = (response.text)
        if response.status_code == 200:

        # if get["otp"] == data['user_otp']:
            response = redirect(f"/Dashboard_profile_finder/{uidd}")
            response.set_cookie("superadmin",uidd)
            return response
            # return redirect(f"/Dashboard_profile_finder/{uidd}")
        else:
            error = "YOUR EMAILID OR PASSWORD IS INCORRECT"
        
    context = {'error':error}

    return render(request,"index.html",context)

def logout(request):
    print("logout")
    value = request.COOKIES.get('superadmin')
    response = redirect("/signin")
    # response = HttpResponse("cookies cleared")
    response.delete_cookie("signin",value)
    return response

def dashboard_profile_finder(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    print(mydata)
    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()


    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'profile_finder1':profile_finder[::-1],
        'hiring_manager':hiring_manager,
        'profile_manager':profile_manager,
        'sales_manager':sales_manager,
        'private_investigator':private_investigator,
        'ad_provider':ad_provider,
        'ad_distributor':ad_distributor,
        'access':access,



    }
    return render(request,"dashboard_profilefinder.html",context)

def dashboard_hiring_manager(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()


    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'hiring_manager':hiring_manager,
        'hiring_manager1':hiring_manager[::-1],
        'profile_manager':profile_manager,
        'sales_manager':sales_manager,
        'private_investigator':private_investigator,
        'ad_provider':ad_provider,
        'ad_distributor':ad_distributor,
        'access':access,



    }

    return render(request,"dashboard_hiring_manager.html",context)

def dashboard_regional_manager(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()


    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'hiring_manager':hiring_manager,
        'profile_manager':profile_manager,
        'sales_manager':sales_manager,
        'private_investigator':private_investigator,
        'ad_provider':ad_provider,
        'ad_distributor':ad_distributor,
        'access':access,



    }
    return render(request,"dashboard_regional_manager.html",context)

def dashboard_ad_provider(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()


    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'hiring_manager':hiring_manager,
        'profile_manager':profile_manager,
        'sales_manager':sales_manager,
        'private_investigator':private_investigator,
        'ad_provider':ad_provider,
        'ad_provider1':ad_provider[::-1],
        'ad_distributor':ad_distributor,
        'access':access,



    }
    return render(request,"dashboard_ad_provider.html",context)

def dashboard_ad_distributor(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()


    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'hiring_manager':hiring_manager,
        'profile_manager':profile_manager,
        'sales_manager':sales_manager,
        'private_investigator':private_investigator,
        'ad_provider':ad_provider,
        'ad_distributor':ad_distributor,
        'ad_distributor1':ad_distributor[::-1],
        'access':access,




    }
    return render(request,"dashboard_ad_distributor.html",context)

def dashboard_profile_manager(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()


    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'hiring_manager':hiring_manager,
        'profile_manager':profile_manager,
        'profile_manager1':profile_manager[::-1],
        'sales_manager':sales_manager,
        'private_investigator':private_investigator,
        'ad_provider':ad_provider,
        'ad_distributor':ad_distributor,
        'access':access,



    }
    return render(request,"dashboard_profile_manager.html",context)

def dashboard_sales_person(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()


    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'hiring_manager':hiring_manager,
        'profile_manager':profile_manager,
        'sales_manager':sales_manager,
        'sales_manager1':sales_manager[::-1],
        'private_investigator':private_investigator,
        'ad_provider':ad_provider,
        'ad_distributor':ad_distributor,
        'access':access,



    }
    return render(request,"dashboard_sales_person.html",context)

def dashboard_private_investigator(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()


    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'hiring_manager':hiring_manager,
        'profile_manager':profile_manager,
        'sales_manager':sales_manager,
        'private_investigator':private_investigator,
         'private_investigator1':private_investigator[::-1],
        'ad_provider':ad_provider,
        'ad_distributor':ad_distributor,
        'access':access,



    }
    return render(request,"dashboard_private_investigator.html",context)

def dashboard_affiliate_marketing(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    #profile_finder
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    #hiring_manager
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    #profile_manager
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    #sales_manager
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    #private_investigator
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    #ad_provider
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    #ad_distributor
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()
    #aff_marketing
    aff_marketing = requests.get("http://127.0.0.1:3000/all_aff_data").json()



    print(mydata)
    print(request.get_full_path())
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'hiring_manager':hiring_manager,
        'profile_manager':profile_manager,
        'sales_manager':sales_manager,
        'private_investigator':private_investigator,
        'ad_provider':ad_provider,
        'ad_distributor':ad_distributor,
        'aff_marketing1':aff_marketing[::-1],
        'access':access,



    }
    return render(request,"dashboard_affiliate_marketing.html",context)

def revenue(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'access':access,
    }
    return render(request,"revenue.html",context)

def expense(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'access':access,
    }
    return render(request,"expense.html",context)


def public_user(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    profile_finder = requests.get(f"http://127.0.0.1:3000/alluserdata/").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_finder':profile_finder,
        'access':access,
    }
    if request.method == "POST":
        if 'uid' in request.POST:
            print(request.POST)
            global uid
            uid = request.POST['uid']
            return redirect(f"/view_details/{id}")
        elif 'delete' in request.POST:
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/public_user_delete/{id}",data = request.POST)
            print(response.status_code)
            return redirect(f"/public_user/{id}")
    return render(request,"public_user.html",context)

def view_details(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    public_user(request,id)
    print(uid) 
    specific_data = requests.get(f"http://127.0.0.1:3000/alldata/{uid}").json()
    my = requests.get(f"http://127.0.0.1:3000/alldata/{uid}").json()
    #sibling details
    sibling_name_value=[]
    sibling_relation_value=[]
    sibling_occupation_value=[]
    sibling_name = my['sibling_name'][1:-1].split(", ")
    sibling_relation = my['sibling_relation'][1:-1].split(", ")
    sibling_occupation = my['sibling_occupation'][1:-1].split(", ")
    for sibling_name_x in sibling_name:
        sibling_name_value.append(sibling_name_x[1:-1])
    for sibling_relation_x in sibling_relation:
        sibling_relation_value.append(sibling_relation_x[1:-1])
    for sibling_occupation_x in sibling_occupation:
        sibling_occupation_value.append(sibling_occupation_x[1:-1])
    sibling={}
    sib = [sibling]
    for i, sibling_name_data in enumerate(sibling_name_value):
            sibling[f'sibling_name_{i}'] = sibling_name_data
    for i, sibling_relation_data in enumerate(sibling_relation_value):
            sibling[f'sibling_relation_{i}'] = sibling_relation_data
    for i, sibling_occupation_data in enumerate(sibling_occupation_value):
            sibling[f'sibling_occupation_{i}'] = sibling_occupation_data
    

    #education
    education_school_value=[]
    education_year_value=[]
    education_course_value=[]
    education_school = my['education_school'][1:-1].split(", ")
    education_year = my['education_year'][1:-1].split(", ")
    education_course = my['education_course'][1:-1].split(", ")
    for education_school_x in education_school:
        education_school_value.append(education_school_x[1:-1])
    for education_year_x in education_year:
        education_year_value.append(education_year_x[1:-1])
    for education_course_x in education_course:
        education_course_value.append(education_course_x[1:-1])
    education={}
    edu = [education]
    for i, education_school_data in enumerate(education_school_value):
            education[f'education_school_{i}'] = education_school_data
    for i, education_year_data in enumerate(education_year_value):
            education[f'education_year_{i}'] = education_year_data
    for i, education_course_data in enumerate(education_course_value):
            education[f'education_course_{i}'] = education_course_data
    
    # print(edu)

     #working experience
    company_name_value=[]
    position_value=[]
    salary_range_value=[]
    profession_value = []
    company_name = my['company_name'][1:-1].split(", ")
    position = my['position'][1:-1].split(", ")
    salary_range = my['salary_range'][1:-1].split(", ")
    profession = my['profession'][1:-1].split(", ")
    for company_name_x in company_name:
        company_name_value.append(company_name_x[1:-1])
    for position_x in position:
        position_value.append(position_x[1:-1])
    for salary_range_x in salary_range:
        salary_range_value.append(salary_range_x[1:-1])
    for profession_x in profession:
        profession_value.append(profession_x[1:-1])
    working={}
    wor = [working]
    for i, company_name_data in enumerate(company_name_value):
            working[f'company_name_{i}'] = company_name_data
    for i, position_data in enumerate(position_value):
            working[f'position_{i}'] = position_data
    for i, salary_range_data in enumerate(salary_range_value):
            working[f'salary_range_{i}'] = salary_range_data
    for i, profession_data in enumerate(profession_value):
            working[f'profession_{i}'] = profession_data
    # print(wor)

   #intrest
    
    
    your_intrest_value=[]
    your_intrest = my['your_intrest'][1:-1].split(", ")
    for i, your_intrest_data in enumerate(your_intrest):
            your_intrest_value.append({'intrest':your_intrest_data[1:-1]})
 
    inte=your_intrest_value
    # print(your_intrest_value)

    yourinterest = my['your_intrest']
    x = yourinterest.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthyourinterest = x.split(",")
    # print(lengthyourinterest)

    interestlist = ["Music","Travel","Gaming","Reading","Photograph","Writing","Sports","Artist",
                    "Singing","Custom","Dancer","Speaking"]

    #non intrest
    
    
    non_intrest_value=[]
    non_intrest = my['non_intrest'][1:-1].split(", ")
    for i, non_intrest_data in enumerate(non_intrest):
            non_intrest_value.append({'non_intrest':non_intrest_data[1:-1]})
 
    non_inte=non_intrest_value
    # print(non_inte)

    yournoninterest = my['non_intrest']
    non = yournoninterest.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthyournoninterest = non.split(",")

    #complexion
    complexion = my['complexion']
    com = complexion.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthcomplexion= com.split(",")
    # print(lengthcomplexion)

    complexionlist = ["Dark","Medium","ModerateFaIr","FaIr","VeryFair"]

    #food taste
    food_taste = my['food_taste']
    ft = food_taste.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthfood_taste= ft.split(",")
    # print(lengthfood_taste)

    food_tastelist = ["Sweezt","Bitter","UmamI","Salt","Sour","Spicy"]

    #gallery

    gall = my['gallery']
    ga = gall.replace("[", "").replace("]","").replace("'","").replace(" ","")
    lengthgallery= ga.split(",")

    
    context={
        'key':mydata,
        'current_path':request.get_full_path(),
        'specific_data':specific_data,
        'sibling':sib,
      'education':edu,
      'working':wor,
      'intrest':inte,
      'interestlist':interestlist,
      'lengthyourinterest':lengthyourinterest,
      'non_intrest':non_inte,
      'lengthyournoninterest':lengthyournoninterest,
      'complexionlist':complexionlist,
      'lengthcomplexion':lengthcomplexion,
      'lengthfood_taste':lengthfood_taste,
      'food_tastelist':food_tastelist,
        'lengthgallery':lengthgallery,
        'access':access,
        # 'access_Privileges':access_Privileges,
    }
    if request.method == "POST":
        print(request.POST)
        print("yes")
        response = requests.post(f"http://127.0.0.1:3000/status/{id}",data = request.POST)
        print(response)
        return redirect(f"profile_manager/profile_finders/{id}")
    
    else:
         pass
    return render(request,"adminview_details.html",context)

def hiring_manager(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']
    hiring_manager = requests.get("http://127.0.0.1:3000/all_hm_data/").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'hiring_manager':hiring_manager,
        'access':access,
    }
    if request.method == "POST":
        if 'uid' in request.POST:
            # print(request.POST)
            # global uid
            # uid = request.POST['uid']
            # return redirect(f"/view_details/{id}")
            pass
        elif 'delete' in request.POST:
            # print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/hirirng_user_delete/{id}",data = request.POST)
            print(response.status_code)
            return redirect(f"/hiring_manager/{id}")
        else:
            print(request.POST)
            response = requests.post("http://127.0.0.1:3000/superadmin/super_admin_hm_signup",data=request.POST)
            print(response.status_code)
            # print(response.text)
            return redirect(f"/hiring_manager/{id}")
    return render(request,"hiring_manager.html",context)

def hm_edit_acc(request,id,uid):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    try:
        hiring_my_data = requests.get(f"http://127.0.0.1:3000/hm_my_data/{uid}").json()[0]
            #for education 
        education  = jsondec.decode(hiring_my_data['level_education'])
        study = jsondec.decode(hiring_my_data['field_study'])
        school_colege = jsondec.decode(hiring_my_data['school_colege'])
        completed_year = jsondec.decode(hiring_my_data['completed_year'])
        study_location = jsondec.decode(hiring_my_data['study_location'])
        try:
            degree_cer = jsondec.decode(hiring_my_data['degree_cer'])
        except:
            pass
        educations = []
        for x in range(1,len(education)+1):
            new = {}
            try:
                new['level_education'] = education[x-1]
            except:
                pass
            try:
                new['field_study'] = study[x-1]
            except:
                pass
            try:
                new['school_colege'] = school_colege[x-1]
            except:
                pass
            try:
                new['completed_year'] = completed_year[x-1]
            except:
                pass
            try:
                new['study_location'] = study_location[x-1]
            except:
                pass
            try:
                new['degree_cer'] = degree_cer[x-1]
            except:
                pass
            educations.append(new)
        print(educations)
        skills = jsondec.decode(hiring_my_data['skills'])
        #for work 
        try:
            work_job_title  = jsondec.decode(hiring_my_data['work_job_title'])
        except:
            pass
        try:
            work_company_name = jsondec.decode(hiring_my_data['work_company_name'])
        except:
            pass
        try:
            work_start_date = jsondec.decode(hiring_my_data['work_start_date'])
        except:
            pass
        try:
            starting_salary = jsondec.decode(hiring_my_data['starting_salary'])
        except:
            pass
        try:
            work_end_date = jsondec.decode(hiring_my_data['work_end_date'])
        except:
            pass
        try:
            final_salary = jsondec.decode(hiring_my_data['final_salary'])
        except:
            pass
        try:
            reason_leaving = jsondec.decode(hiring_my_data['reason_leaving'])
        except:
            pass
        try:
            work_review_y = jsondec.decode(hiring_my_data['work_review_y'])
        except:
            pass
        try:
            expr_certi = jsondec.decode(hiring_my_data['expr_certi'])
        except:
            pass
        working_details = []
        if hiring_my_data['work_job_title'] != "empty":
            for x in range(1,len(work_job_title)+1):
                new = {}
                try:
                    new['work_job_title'] = work_job_title[x-1]
                except:
                    pass
                try:
                    new['work_company_name'] = work_company_name[x-1]
                except:
                    pass
                try:
                    new['work_start_date'] = work_start_date[x-1]
                except:
                    pass
                try:
                    new['starting_salary'] = starting_salary[x-1]
                except:
                    pass
                try:
                    new['work_end_date'] = work_end_date[x-1]
                except:
                    pass
                try:
                    new['final_salary'] = final_salary[x-1]
                except:
                    pass
                try:
                    new['reason_leaving'] = reason_leaving[x-1]
                except:
                    pass
                try:
                    new['work_review_y'] = work_review_y[x-1]
                except:
                    pass
                try:
                    new['expr_certi'] = expr_certi[x-1]
                except:
                    pass
                working_details.append(new)

        neww=[]
        response = requests.get('https://api.first.org/data/v1/countries').json()
        all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        states = json.dumps(all["data"])
        al = (all["data"])
        for x in al:
            name = (x.get("name"))
            neww.append(name)
        countryname = json.dumps(neww)
    
        context={
            'key1':mydata,
               'key':hiring_my_data,
            'current_path':request.get_full_path(),
            'response': response, 
            'region': response,'all':al,
            'country': countryname,'states': states,
            'access':access,
            'hiring_my_data':hiring_my_data,
            'education':education,
            'study':study,
            'response': response,
            'region': response,
            'all':al,
            'country': countryname,'states': states,
            'a':educations,
            'skills':skills,
            'working_details':working_details,
        }
        if request.method == "POST":
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/hiring_upload_account/{uid}",data=request.POST,files = request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                return redirect(f"/hiring_manager/{id}")
        return render(request,"adminhm_edit_acc.html",context)
    except:
        context={
           'key':mydata,
           'current_path':request.get_full_path(),
       }
        return render(request,"adminhm_edit_acc.html",context)


def admin_profile_manager(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']  
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'profile_manager':profile_manager,
        'access':access,
    }
    if request.method == "POST":
        if 'uid' in request.POST:
            # print(request.POST)
            # global uid
            # uid = request.POST['uid']
            # return redirect(f"/view_details/{id}")
            pass
        elif 'delete' in request.POST:
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/profile_user_delete/{id}",data = request.POST)
            print(response.status_code)
            return redirect(f"/profile_manager/{id}")
    return render(request,"profile_manager.html",context)

def pm_edit_acc(request,id,uid):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        try:
            mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
            access=""
        except:
            mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
            access=mydata['access_privilage']   
        profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
        pm_data = requests.get(f"http://127.0.0.1:3000/pm_myid/{uid}").json()[0] 
   
        education  = jsondec.decode(pm_data['level_education'])
    
        study = jsondec.decode(pm_data['field_study']) 
        #country api 
        neww=[]
        response = requests.get('https://api.first.org/data/v1/countries').json()
        all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        states = json.dumps(all["data"])
        al = (all["data"])
        for x in al:
            name = (x.get("name"))
            neww.append(name)
            countryname = json.dumps(neww)
            countryname = json.dumps(neww)
    
        context = {'response': response, 'region': response,'all':al,
                    'country': countryname,'states': states,'key1':mydata,
                    'current_path':request.get_full_path(),'access':access,
                    'pm_data':pm_data,
                    'education':education,
                    'study':study,}
        
        if request.method=="POST":
            print(request.POST)
            # response = requests.post(f"http://127.0.0.1:3000/pm_edit_account/{uid}",   data = request.POST,files=request.FILES)
            response = requests.post(f"http://127.0.0.1:3000/profile_manager_upload_account/{request.POST['uid']}",data=request.POST,files = request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                return redirect(f"/profile_manager/{id}")
        return render(request,"pm_edit_acc.html",context)
    except:
        return render(request,"pm_edit_acc.html",context)


def sales_person(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    sales_manager = requests.get("http://127.0.0.1:3000/all_sm_data/").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'sales_manager':sales_manager,
        'access':access,
    }
    if request.method == "POST":
        if 'uid' in request.POST:
            # print(request.POST)
            # global uid
            # uid = request.POST['uid']
            # return redirect(f"/view_details/{id}")
            pass
        elif 'delete' in request.POST:
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/sales_user_delete/{id}",data = request.POST)
            print(response.status_code)
            return redirect(f"/sales_person/{id}")
    return render(request,"sales_person.html",context)

def sm_edit_profile(request,id,uid):
        value = request.COOKIES.get('superadmin')
        if value != None:
            print(value)
            # return redirect("/Dashboard_profile_finder/{value}")
        else:
            return redirect("/superadmin")
        try:
            # sm_mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{uid}").json()[0] 
            # print(sm_mydata)
            try:
                mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
                access=""
            except:
                mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
                access=mydata['access_privilage']
            profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
            sales_my_data = requests.get(f"http://127.0.0.1:3000/sm_my_data/{uid}").json()[0]  
            education  = jsondec.decode(sales_my_data['level_education'])
            study = jsondec.decode(sales_my_data['field_study']) 
            neww=[]
            response = requests.get('https://api.first.org/data/v1/countries').json()
            all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
            # statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
            states = json.dumps(all["data"])
            al = (all["data"])
            for x in al:
                name = (x.get("name"))
                neww.append(name)
            countryname = json.dumps(neww)
        
            context = {"key1":mydata,'sales_my_data':sales_my_data,
         'education':education,
        'study':study,
                    'current_path':request.get_full_path(),'response': response, 'region': response,'all':al,
                        'country': countryname,'states': states,
                        'current_path':request.get_full_path(),'access':access,}
            
            if request.method=="POST":
                print(request.POST)
                response = requests.post(f"http://127.0.0.1:3000/sales_upload_account/{uid}", data = request.POST,files=request.FILES)
                print(response)
                print(response.status_code)
                print(response.text)
                if response.status_code == 200:
                    return redirect(f"/sales_person/{id}")
            return render(request,"adminsm_editprofile.html",context)
        
            
        except:
            return render(request,"adminsm_editprofile.html")

def affiliate_marketing(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    sales_manager = requests.get("http://127.0.0.1:3000/all_aff_data").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'sales_manager':sales_manager,
        'access':access,
    }
    if request.method == "POST":
        if 'uid' in request.POST:
            # print(request.POST)
            # global uid
            # uid = request.POST['uid']
            # return redirect(f"/view_details/{id}")
            pass
        elif 'delete' in request.POST:
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/sales_user_delete/{id}",data = request.POST)
            print(response.status_code)
            return redirect(f"/sales_person/{id}")
    return render(request,"affiliate_marketing.html",context)

def am_editaccount(request,id,uid):
        value = request.COOKIES.get('superadmin')
        if value != None:
            print(value)
            # return redirect("/Dashboard_profile_finder/{value}")
        else:
            return redirect("/superadmin")
        try:
            # sm_mydata = requests.get(f"http://127.0.0.1:3000/sm_my_data/{uid}").json()[0] 
            # print(sm_mydata)
            try:
                mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
                access=""
            except:
                mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
                access=mydata['access_privilage']
            af_my_data = requests.get(f"http://127.0.0.1:3000/af_my_data/{uid}").json()[0]  
            education  = jsondec.decode(af_my_data['level_education'])
            study = jsondec.decode(af_my_data['field_study']) 
            neww=[]
            response = requests.get('https://api.first.org/data/v1/countries').json()
            all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
            # statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
            states = json.dumps(all["data"])
            al = (all["data"])
            for x in al:
                name = (x.get("name"))
                neww.append(name)
            countryname = json.dumps(neww)
        
            context = {"key":mydata,'sales_my_data':af_my_data,'education':education,'study':study,
                    'current_path':request.get_full_path(),'response': response, 'region': response,'all':al,
                        'country': countryname,'states': states,
                        'current_path':request.get_full_path(),'access':access,}
            
            if request.method=="POST":
                print(request.POST)
                response = requests.post(f"http://127.0.0.1:3000/affiliate_upload_account/{request.POST['uid']}", data = request.POST,files=request.FILES)
                print(response)
                print(response.status_code)
                print(response.text)
                if response.status_code == 200:
                    return redirect(f"/affiliate_marketing/{id}")
            return render(request,"am_editaccount.html",context)
        
            
        except:
            return render(request,"am_editaccount.html")
        
def private_investigator(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    private_investigator = requests.get("http://127.0.0.1:3000/all_private_investigator_data").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
                'private_investigator':private_investigator,
                'access':access,

    }
    if request.method == "POST":
        if 'uid' in request.POST:
            # print(request.POST)
            # global uid
            # uid = request.POST['uid']
            # return redirect(f"/view_details/{id}")
            pass
        elif 'delete' in request.POST:
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/pi_user_delete/{id}",data = request.POST)
            print(response.status_code)
            return redirect(f"/private_investigator/{id}")
    return render(request,"private_investigator.html",context)

def pi_edit_profile(request,id,uid):
        value = request.COOKIES.get('superadmin')
        if value != None:
            print(value)
            # return redirect("/Dashboard_profile_finder/{value}")
        else:
            return redirect("/superadmin")
        try:
            mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
            access=""
        except:
            mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
            access=mydata['access_privilage']    
        profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
        pi_my_data = requests.get(f"http://127.0.0.1:3000/pi_my_data/{uid}").json()[0]
        education  = jsondec.decode(pi_my_data['level_education'])
        study = jsondec.decode(pi_my_data['field_study'])   
        # print(my)
        if request.method == "POST":
            print(request.POST)
            print(request.FILES)
            response = requests.post(f"http://127.0.0.1:3000/private_investigator_upload_account/{request.POST['uid']}",data=request.POST,files=request.FILES)
            if response.status_code == 200:
                return redirect(f"/private_investigator/{id}")
        context={
            # 'key':my,
                 'pi_my_data':pi_my_data,
                'education':education,
                'study':study,
                 'key1':mydata,
                 'current_path':request.get_full_path(),
                 'access':access,
                 }
        return render(request,"pi_edit_profile.html",context)


def pi_settings(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']  
    pi_data = requests.get(f"http://127.0.0.1:3000/superadmin/pi_settings/1").json() 
    print(pi_data) 
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'pi_data':pi_data,
        'access':access,
    }
    if request.method == "POST":
        print(request.POST)
        response = requests.post(f"http://127.0.0.1:3000/superadmin/pi_settings/{id}",data = request.POST)
        print(response.status_code)
        print(response.text)
        if response.status_code == 200:
            return redirect(f"/pi_settings/{id}")

    return render(request,"pi_settings.html",context)

def performance_settings(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    pi_performance_calc = requests.get(f"http://127.0.0.1:3000/superadmin/pi_performance_calculations/1").json() 
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'pi_performance_calc':pi_performance_calc,
        'access':access,
    }
    if request.method == "POST":
        print(request.POST)
        response = requests.post(f"http://127.0.0.1:3000/superadmin/pi_performance_calculations/{id}",data = request.POST)
        print(response.status_code)
        print(response.text)
        if response.status_code == 200:
            return redirect(f"/performance_settings/{id}")
    return render(request,"performance_settings.html",context)


def ad_provider(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage'] 
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    ad_provider = requests.get("http://127.0.0.1:3000/all_ad_pro_data/").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'ad_provider':ad_provider,
        'access':access,
    }
    if request.method == "POST":
        if 'uid' in request.POST:
            # print(request.POST)
            # global uid
            # uid = request.POST['uid']
            # return redirect(f"/view_details/{id}")
            pass
        elif 'delete' in request.POST:
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/adpro_user_delete/{id}",data = request.POST)
            print(response.status_code)
            return redirect(f"/ad_provider/{id}")
    return render(request,"ad_provider.html",context)

def ad_pro_edit_account(request,id,uid):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        try:
            mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
            access=""
        except:
            mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
            access=mydata['access_privilage']    
        profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
        ad_pro_my_data = requests.get(f"http://127.0.0.1:3000/ad_pro_my_data/{uid}").json()[0] 
        education  = jsondec.decode(ad_pro_my_data['level_education'])
        study = jsondec.decode(ad_pro_my_data['field_study'])  
        
        neww=[]
        response = requests.get('https://api.first.org/data/v1/countries').json()
        
        all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        # statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        states = json.dumps(all["data"])
        al = (all["data"])
        for x in al:
           name = (x.get("name"))
           neww.append(name)
        countryname = json.dumps(neww)
    
        context = {'education':education,
        'study':study,
        'ad_pro_my_data':ad_pro_my_data,
                   'key1':mydata,'current_path':request.get_full_path(),
                   'response': response, 'region': response,'all':al,
                    'country': countryname,'states': states,
                    'current_path':request.get_full_path(),'access':access,}
        
        if request.method == "POST":
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/ad_provider_upload_account/{request.POST['uid']}", data = request.POST,files=request.FILES)
            print(response)
            # print(response.status_code)
            # print(response.text)
            if response.status_code == 200:
                return redirect(f"/ad_provider/{id}")
    
        return render(request,"adminad_pro_editAccount.html",context)
    except:
        return render(request,"adminad_pro_editAccount.html")


def ad_distributor(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    profile_manager =  requests.get("http://127.0.0.1:3000/all_pm_data/").json()
    ad_distributor = requests.get("http://127.0.0.1:3000/all_ad_dis_data/").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'ad_distributor':ad_distributor,
        'access':access,
    }
    if request.method == "POST":
        if 'uid' in request.POST:
            # print(request.POST)
            # global uid
            # uid = request.POST['uid']
            # return redirect(f"/view_details/{id}")
            pass
        elif 'delete' in request.POST:
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/addis_user_delete/{id}",data = request.POST)
            print(response.status_code)
            return redirect(f"/ad_distributor/{id}")
    return render(request,"ad_distributor.html",context)

def ad_dis_edit_account(request,id,uid):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        try:
            mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
            access=""
        except:
            mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
            access=mydata['access_privilage']    
        ad_pro_my_data = requests.get(f"http://127.0.0.1:3000/ad_dis_my_data/{uid}").json()[0]  
        education  = jsondec.decode(ad_pro_my_data['level_education'])
        study = jsondec.decode(ad_pro_my_data['field_study'])   
        
        neww=[]
        response = requests.get('https://api.first.org/data/v1/countries').json()
        
        all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        # statess = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
        states = json.dumps(all["data"])
        al = (all["data"])
        for x in al:
           name = (x.get("name"))
           neww.append(name)
        countryname = json.dumps(neww)
    
        context = {'ad_pro_my_data':ad_pro_my_data,
        'education':education,
        'study':study,'key1':mydata,'current_path':request.get_full_path(),
                   'response': response, 'region': response,'all':al,
                    'country': countryname,'states': states,
                    'current_path':request.get_full_path(),'access':access,}
        
        if request.method == "POST":
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/ad_distributor_upload_account/{request.POST['uid']}", data = request.POST,files=request.FILES)
            print(response)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                return redirect(f"/ad_distributor/{id}")
    
        return render(request,"adminad_dis_editAccount.html",context)
    except:
        return render(request,"adminad_dis_editAccount.html")


def emra_coin(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    all_emra_coin = requests.get(f"http://127.0.0.1:3000/superadmin/emra_coin/{id}").json()
    if request.method == "POST":
        print(request.POST)
        if "delete" in request.POST:
            response = requests.post(f"http://127.0.0.1:3000/superadmin/emra_coin/{request.POST['delete']}",data=request.POST)
            print(response.status_code)
        elif "edit" in request.POST:
            response = requests.post(f"http://127.0.0.1:3000/superadmin/emra_coin/{request.POST['edit']}",data=request.POST)
            print(response.status_code)

        else:
            response = requests.post(f"http://127.0.0.1:3000/superadmin/emra_coin/{id}",data=request.POST)
            print(response.status_code)
            # superadmin/emra_coin/<id>
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_emra_coin':all_emra_coin,
        'access':access,
    }
    return render(request,"emra_coin.html",context)

def commision_cal(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']    
    commision_Data = requests.get(f"http://127.0.0.1:3000/superadmin/commision/{id}").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'commision_Data':commision_Data,
        'access':access,
    }
    if request.method == "POST":
        response = requests.post(f"http://127.0.0.1:3000/superadmin/commision/{id}",data=request.POST)
        print(response.status_code)
        print(response.text)
    return render(request,"commision_cal.html",context)

def Add_Commision_1(request,id,uid):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    print(uid)
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']    
    if uid > "0":
        edit_commision = requests.get(f"http://127.0.0.1:3000/superadmin/single_commisionn/{uid}").json()
    else:
        edit_commision = ""
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'edit_commision':edit_commision,
        'access':access,
    }
    if request.method == "POST":
        if "add" in request.POST:
            print("Add")
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/commision/{id}",data=request.POST)
            print(response.status_code)
            print(response.text)
        else:
            print("edit")
            print(request.POST)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/commision/{uid}",data=request.POST)
            print(response.status_code)
            print(response.text)
        return redirect(f"/commision_calculator/{id}")
    return render(request,"Add_Commision_1.html",context)

def complaint_list(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']  
    try:  
        all_complaint = requests.get(f"http://127.0.0.1:3000/superadmin/all_complaint_list/{id}").json()['data']
    except:
        all_complaint=""
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_complaint':all_complaint,
        'access':access,
    }
    return render(request,"complaint_list.html",context)

def dropdown_values(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']  
    # all drop downs
    country_dropdown = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/country").json()
    # country_dropdown = ""
    country_alter=[]
    for x in country_dropdown:
        dic = {}
        x['citiess'] = jsondec.decode(x['cities'])
        country_alter.append(x)
        print(type(jsondec.decode(x['cities'])))
    currency_dropdown = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/currency").json()
    # physical_status_dropdown =""
    # cast = ""
    # type_of_relationship = ""
    # education = ""
    # job_position = ""
    # salary_range = ""
    # intrest = ""
    # no_intrest = ""
    # complexion = ""
    # food_taste = ""
    # organs = ""
    # familystatus = ""
    marital_status_dropdown = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/marital_status").json()
    physical_status_dropdown = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/physical_status").json()
    cast = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/cast").json()
    type_of_relationship = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/type_of_relationship").json()
    education = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/education").json()
    job_position = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/job_position").json()
    salary_range = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/salary_range").json()
    intrest = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/intrest").json()
    no_intrest = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/no_intrest").json()
    complexion = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/complexion").json()
    food_taste = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/food_taste").json()
    organs = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/organs").json()
    familystatus = requests.get("http://127.0.0.1:3000/superadmin/dropdownn/familystatus").json()


    # end drop downs
    neww=[]
    response = requests.get('https://api.first.org/data/v1/countries').json()
    all = requests.get('https://countriesnow.space/api/v0.1/countries/states').json()
    states = json.dumps(all["data"])
    al = (all["data"])
    for x in al:
        name = (x.get("name"))
        neww.append(name)
    countryname = json.dumps(neww)

    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'access':access,
        'response': response, 'region': response,'all':al,
                    'country': countryname,'states': states,
                    'country_dropdown':country_alter,
                    'currency_dropdown':currency_dropdown,
                    'marital_status_dropdown':marital_status_dropdown,
                    'physical_status_dropdown':physical_status_dropdown,
                    'cast':cast,
                    'type_of_relationship':type_of_relationship,
                    'education':education,
                    'job_position':job_position,
                    'salary_range':salary_range,
                    'intrest':intrest,
                    'no_intrest':no_intrest,
                    'complexion':complexion,
                    'food_taste':food_taste,
                    'organs':organs,
                    'familystatus':familystatus,
                    'trigger':""
                    
                    
    }
    if request.method == "POST":
        print(request.POST)
        if "city" in request.POST:
            data={
                'country':request.POST['country'],
                'cities':json.dumps(request.POST.getlist('city')),
                'currency' :"None",
                'values':"None", 
                'category' :'country'
            }
        elif "currency" in request.POST:
            data={
                'country':request.POST['country'],
                'cities':"None",
                'currency' :request.POST['currency'],
                'values':"None", 
                'category' :'currency'
            }
        elif "marital_status" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['marital_status'], 
                'category' :'marital_status'
            }
        elif "physical_status" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['physical_status'], 
                'category' :'physical_status'
            }
        elif "cast" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['cast'], 
                'category' :'cast'
            }
        elif "type_of_relationship" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['type_of_relationship'], 
                'category' :'type_of_relationship'
            }
        elif "education" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['education'], 
                'category' :'education'
            }
        elif "job_position" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['job_position'], 
                'category' :'job_position'
            }
        elif "salary_range" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['salary_range'], 
                'category' :'salary_range'
            }
        elif "intrest" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['intrest'], 
                'category' :'intrest'
            }
        elif "no_intrest" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['no_intrest'], 
                'category' :'no_intrest'
            }
        elif "complexion" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['complexion'], 
                'category' :'complexion'
            }
        elif "food_taste" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['food_taste'], 
                'category' :'food_taste'
            }
        elif "organs" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['organs'], 
                'category' :'organs'
            }
        elif "familystatus" in request.POST:
            data={
                'country':"None",
                'cities':"None",
                'currency' :"None",
                'values':request.POST['familystatus'], 
                'category' :'familystatus'
            }
        elif 'delete' in request.POST:
            data = request.POST
        elif 'edit' in request.POST:
            data = request.POST
        elif 'edit_cities' in request.POST:
            data = request.POST
        elif 'delete_cities' in request.POST:
            data = request.POST
        elif "currency_country" in request.POST:
            data = request.POST
        
           
        response = requests.post(f"http://127.0.0.1:3000/superadmin/dropdownn/{id}",data=data)
        print(response.status_code)
        if response.status_code == 200:
            return redirect(f"/dropdown_values/{id}")
    return render(request,"dropdown_values.html",context)

def third_party_users(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    error = ""
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']    
    all_third_party_user = requests.get(f"http://127.0.0.1:3000/superadmin/third_party_userrr/{id}").json()
    
    if request.method == "POST":
        print(request.POST)
        response = requests.post(f"http://127.0.0.1:3000/superadmin/third_party_userrr/{id}",data=request.POST)
        print(response.status_code)
        print(response.text)
        if response.status_code == "200":
            return redirect(f"/third_party_users/{id}")
        
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_third_party_user':all_third_party_user,
        'error':error,
        'access':access,
    }
    return render(request,"third_party_users.html",context)

def third_party_user_Add(request,id,uid):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    error = ""
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']    
    if uid != "0":
        single_third_party_user = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{uid}").json()
        print(single_third_party_user)
    else:
        single_third_party_user = ""
    
    if request.method == "POST":
        if "add" in request.POST:
            print(request.POST)
            data={}
            for x in request.POST.keys():
                data[x] = request.POST[x]
            data.pop("access_privilage")
            data["access_privilage"] = request.POST.getlist('access_privilage')
            print(data)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/third_party_userrr/{id}",data=data)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                    return redirect(f"/third_party_users/{id}")
            else:
                error = "!--User already Exixts--!"
        else:
            print("edit")
            print(request.POST)
            uid = request.POST['edit']
            data={}
            for x in request.POST.keys():
                data[x] = request.POST[x]
            data.pop("access_privilage")
            data["access_privilage"] = request.POST.getlist('access_privilage')
            print(data)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/third_party_userrr/{uid}",data=data)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                return redirect(f"/third_party_users/{id}")
                
        
    context = { 
        'key':mydata,
        'current_path':request.get_full_path(),
        'single_third_party_user':single_third_party_user,
        'error':error,
        'access':access,
        }
    return render(request,"third_party_user_Add.html",context)

def subscription(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']    
    all_subscription = requests.get(f"http://127.0.0.1:3000/superadmin/subscription/{id}").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_subscription':all_subscription,
        'access':access,
    }
    if request.method == "POST":
        print(request.POST)
        if 'delete' in request.POST:
            response = requests.post(f"http://127.0.0.1:3000/superadmin/subscription/{request.POST['delete']}",data=request.POST)
            print(response.status_code)
            print(response.text)
            return redirect(f"/subscription/{id}")

    return render(request,"subscriptions.html",context)

def subscriptionadd(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'access':access,
    }
    if request.method == "POST":
        print(request.POST)
        if 'delete' in request.POST:
            response = requests.post(f"http://127.0.0.1:3000/superadmin/subscription/{request.POST['delete']}",data=request.POST)
            print(response.status_code)
            print(response.text)
            return redirect(f"/subscription/{id}")

        else:
            response = requests.post(f"http://127.0.0.1:3000/superadmin/subscription/{id}",data=request.POST)
            print(response.status_code)
            print(response.text)
            return redirect(f"/subscription/{id}")
    return render(request,"subscriptionadd.html",context)

def subscriptionedit(request,id,sid):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']   
    single_subscriptionN = requests.get(f"http://127.0.0.1:3000/superadmin/single_subscriptionN/{id}/{sid}").json()
    
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'single_subscriptionN':single_subscriptionN,
        'access':access,
    }
    if request.method == "POST":
        print(request.POST)
        response = requests.post(f"http://127.0.0.1:3000/superadmin/single_subscriptionN/{id}/{sid}",data=request.POST)
        print(response.status_code)
        # print(response.text)
        return redirect(f"/subscription/{id}")

    return render(request,"subedit.html",context)



def External_expense(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']  
    all_external_expenses = requests.get(f"http://127.0.0.1:3000/superadmin/external_expenses_add/{id}").json()
    if request.method == "POST":
        print(request.POST)
        if "delete" in request.POST:
            response = requests.post(f"http://127.0.0.1:3000/superadmin/external_expenses_add/{request.POST['delete']}",data=request.POST)
            print(response.status_code)
            if response.status_code == 200:
                return redirect(f"/External_expense/{id}")
        elif "edit" in request.POST:
            response = requests.post(f"http://127.0.0.1:3000/superadmin/external_expenses_add/{request.POST['edit']}",data=request.POST,files = request.FILES)
            print(response.status_code)
            if response.status_code == 200:
                return redirect(f"/External_expense/{id}")
        else:
            print(request.FILES)
            response = requests.post(f"http://127.0.0.1:3000/superadmin/external_expenses_add/{id}",data=request.POST,files=request.FILES)
            print(response.status_code)
            if response.status_code == 200:
                return redirect(f"/External_expense/{id}")

    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'all_external_expenses':all_external_expenses,
        'access':access,
    }
    return render(request,"External_expense.html",context)

def insentives_settings(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage']    
    incentive_data = requests.get(f"http://127.0.0.1:3000/superadmin/incentive_settings/1").json()
    if request.method == "POST":
        print(request.POST)
        response = requests.post(f"http://127.0.0.1:3000/superadmin/incentive_settings/{id}",data = request.POST)
        print(response.status_code)
        print(response.text)
        if response.status_code == 200:
            return redirect(f"/insentives_settings/{id}")
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'incentive_data':incentive_data,
        'access':access,
        
    }
    return render(request,"insentives_settings.html",context)

def matching_list(request,id):
    value = request.COOKIES.get('superadmin')
    if value != None:
        print(value)
        # return redirect("/Dashboard_profile_finder/{value}")
    else:
        return redirect("/superadmin")
    try:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/my_data/{id}").json()[0]
        access=""
    except:
        mydata = requests.get(f"http://127.0.0.1:3000/superadmin/single_third_party_userrr/{id}").json()
        access=mydata['access_privilage'] 
    all_data = requests.get("http://127.0.0.1:3000/superadmin/dummy_matching_list").json()
    context = {
        'key':mydata,
        'current_path':request.get_full_path(),
        'access':access,
        'all_data':all_data,
        
    } 
    if request.method == "POST":
        print(request.POST)
        if "delete" in request.POST:
            response = requests.post("http://127.0.0.1:3000/superadmin/dummy_matching_list",data = request.POST)
            print(response.status_code)
        else:
            print(request.FILES)
            response = requests.post("http://127.0.0.1:3000/superadmin/dummy_matching_list",data = request.POST,files = request.FILES)
            print(response.status_code)
        return redirect(f"/dummy_matching_list/{mydata['id']}")
    return render(request,"dummy_matching_list.html",context)



