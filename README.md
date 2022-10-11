# 페어 프로그래밍

## 프로젝트 소개

- 🗓

  프로젝트 기간

  - 2022.10.07

- 💻

  사용 기술

  - Python, Django, HTML, CSS, Bootstrap5

- ⭐

  나의 역할

  - 디자인을 제외한 모두.

## 목적

페어 프로그래밍을 통해 영화 리뷰 커뮤니티 서비스를 개발

- **ModelForm**을 활용한 CRUD 구현
- **Staticfiles** 활용

# 문제 해결

## 문제 상황

짧은 시간에 진도를 나가다 보니 팀원분들이 아직 ModelForm을 사용해 본 것이 없었습니다. 

## 해결

저는 팀원들과 이야기를 해 보고 제가 알려드리면서 하자고 진행을 하였습니다. 

다행히 이전 진도까지는 두분 다 따라온 상태였습니다. 

ModelForm을 사용하는 상황이 new를 만들때랑 update를 사용하는 상황이었는데요.

처음 new를 만들때는 쌤의 github에 들어가서 보는 방식으로 문제를 해결했는데. 제대로 이해할거면 else: 아래 부분부터 설명을 해 줘야 했는데. 자연스럽게 제일 위에 if문 부터 설명을 하게 되어서 이해를 못했을거 같았습니다. 

그래서 두번째 update를 만들때 순서에 맞게 보여주면서 알려줘야 겠다고 생각을 했습니다. 

1. 우선 update를 render하는 것을 보여주었습니다. 
   ```python
   review_form = ReviewForm()
   context = {
       "review_form": review_form,
   }
   return render(request,'reviews/update.html',context)
   ```

   이 부분은 이전과 비슷해서 힘들지 않게 이해 했던 걸로 보였습니다. 

2. 그 다음 update.html에 가서 만들었는데. 사실 이 부분은 modelForm쓰기 전에 비해서 특정 명령어를 추가만 하면 끝나는 과정이었습니다. 이 부분은 이해하라고 하면 오히려 혼란을 줄 거 같았고 그래서 이 부분은 그냥 복사 붙여 넣기 하면 끝이라고 설명을 했습니다. 

   ```html
   {% extends 'base.html' %}
   {% block content %}
     {% load django_bootstrap5 %}
     {% bootstrap_css %}
     {% bootstrap_javascript %}
     <form action="" method="post">
       {% csrf_token %}
       {% bootstrap_form review_form %}
       {% bootstrap_button button_type="submit" content="OK" button_class="btn-primary col-3"%}
       {% bootstrap_button button_type="reset" content="Cancel" button_class="btn-primary col-3"%}
     </form>
   {% endblock %}
   ```

3. 이제 저 update.html의 form에서 POST로 이 함수로 데이터를 불러오는데. 이때 이걸 처리해 주어야 한다. 

   ```python
   def update(request,pk):
       review = Review.objects.get(pk=pk)
       if request.method == "POST":
           review_form = ReviewForm(request.POST)
           if review_form.is_valid():
               review_form.save()
               return redirect("review:index")
       else:
           review_form = ReviewForm()
       context = {
           "review_form": review_form,
       }
       return render(request,'reviews/update.html',context)
   ```

   이제서야 if와 else를 넣어서 설명해 주었습니다. 

4. 마지막으로 이 상태로 구현되걸 보여 주고, `instance=review` 가 빠져서 내용이 안채워져 있다 이것만 채우면 됩니다. 하고 끝냈습니다. 

   다행히 두분 다 감을 좀 잡으신거 같았습니다. 

   

   

   

   

   

   
