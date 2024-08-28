from django.shortcuts import render, redirect, get_object_or_404
from crime.models import Region, Place, TimeRange, Post
from crime.forms import PostForm
from django.db.models import Sum
import json
import csv


def region(request):
    CSV_PATH = 'static/region.csv'
    with open(CSV_PATH, newline='', encoding='euc-kr') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            Region.objects.create(
                year=row['year'],
                region=row['region'],
                category=row['category'],
                cnt=row['cnt'],
            )
    return

def seoul(request, year, category_name):
    total_sum = Region.objects.aggregate(total=Sum('cnt'))['total'] or 0
    
    # 각 카테고리의 cnt 값들의 합
    categories = ['살인', '강간·강제추행', '강도', '절도', '폭력']
    category_sums = {}
    for category in categories:
        category_sums[category] = Region.objects.filter(category=category).aggregate(total=Sum('cnt'))['total'] or 0

    # 각 카테고리 비율 계산
    category_rates = {category: (category_sums[category] / total_sum if total_sum > 0 else 0) for category in categories}

    
    label_list = []
    data_list = []
    for seoul in Region.objects.filter(year=year, category=category_name):
        label_list.append(seoul.region)
        data_list.append(seoul.cnt)

    context = {
        "label_list": label_list,
        "data_list": data_list,
        "category_rates": json.dumps(category_rates),  # 카테고리 비율을 JSON 형식으로 변환
    }
    
    return render(request, "seoul.html", context)

def place(request, year, category_name):
    total_sum = Place.objects.aggregate(total=Sum('cnt'))['total'] or 0
    
    # 각 카테고리의 cnt 값들의 합
    categories = ['살인', '강간·강제추행', '강도', '절도', '폭력']
    category_sums = {}
    for category in categories:
        category_sums[category] = Place.objects.filter(category=category).aggregate(total=Sum('cnt'))['total'] or 0

    # 각 카테고리 비율 계산
    category_rates = {category: (category_sums[category] / total_sum if total_sum > 0 else 0) for category in categories}

    
    label_list = []
    data_list = []
    for place in Place.objects.filter(year=year, category=category_name):
        label_list.append(place.place)
        data_list.append(place.cnt)

    context = {
        "label_list": label_list,
        "data_list": data_list,
        "category_rates": json.dumps(category_rates),  # 카테고리 비율을 JSON 형식으로 변환
    }
    
    return render(request, "place.html", context)

def time(request, category_name):
    total_sum = TimeRange.objects.aggregate(total=Sum('cnt'))['total'] or 0
    
    # 각 카테고리의 cnt 값들의 합
    categories = ['살인', '강간·강제추행', '강도', '절도', '폭력']
    category_sums = {}
    for category in categories:
        category_sums[category] = TimeRange.objects.filter(category=category).aggregate(total=Sum('cnt'))['total'] or 0

    # 각 카테고리 비율 계산
    category_rates = {category: (category_sums[category] / total_sum if total_sum > 0 else 0) for category in categories}

    
    label_list = []
    data_list = []
    for times in TimeRange.objects.filter(category=category_name):
        label_list.append(times.timerange)
        data_list.append(times.cnt)

    context = {
        "label_list": label_list,
        "data_list": data_list,
        "category_rates": json.dumps(category_rates),  # 카테고리 비율을 JSON 형식으로 변환
    }
    
    return render(request, "time.html", context)

def landing(request): # ~:8000/landing/ 접속 
    # list = Post.objects.all()
    return render(request, "landing.html")  

#  서울시 구별 게시판 조회
def gu_post(request): # 8000/gu_post/ 접속 
    posts= Post.objects.all().order_by('-id')
    return render(request, "gu_post.html",{"posts":posts})

# 게시글 작성 페이지 
def post_add(request): # 8000/post_add/ 접속 
    # post_add = 모델.odbjects.all() 
    if request.method == "POST": 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

        url = "/crime/gu_post/" 
        return redirect(url)
    
    else:
        form = PostForm()

    form = PostForm()
    context = {"form": form}
    
    return render(request, "post_add.html", context)


def post_edit(request, pk): # 게시글 수정 
    post = Post.objects.get(pk=pk)
    if request.method == "POST": # 양식에 맞게 잘 작성됐다면 
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid(): # 게시글 저장 
            post = form.save(commit=False)
            post.user = request.user
            post.save() 
            url = f"/crime/post_detail/"
            return redirect(url) # 저장 후 그 상세 페이지로, 해당 게시글의 상세페이지로 가는건???? 
    else: 
        form = PostForm(instance=post)
        context = {"form": form}
    return render(request, "post_edit.html", context) # 폼에 맞게 작성된게 아니라면 수정 페이지로 리다이렉트
    
def post_detail(request):
    # post = Post.objects.get(pk=pk)
    # comment_form = CommentForm()
    # context = {"post" : post, 
    #            "comment_form": comment_form}
    return render(request, "post_detail.html")


def post_delete(request, pk): # 삭제누르면 삭제되고 구별 게시판으로 리다이렉트
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("gu_post")
