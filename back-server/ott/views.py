from django.shortcuts import render
# import json
# from rest_framework import serializers
# from .models import Netflix

# Create your views here.
# def netflix(request):
#     file_path = '@ott\\fixtures\\dummy.json'
    
#     with open(file_path, 'rt', encoding='utf-8') as file:
#         data = json.load(file)
#         for item in data:
#             # 필요한 데이터 추출
#             full_path = item.get('full_path')
#             full_paths = item.get('full_paths')
#             jw_entity_id = item.get('jw_entity_id')
#             object_type = item.get('object_type')
#             poster = item.get('poster')
#             poster_blur_hash = item.get('poster_blur_hash')
#             scoring = item.get('scoring')
#             title = item.get('title')
#             tmdb_id = None
#             for score in scoring:
#                 if score.get('provider_type') == 'tmdb:id':
#                     tmdb_id = score.get('value')
#                     break
#             print(title)
#             # Netflix 객체 생성 및 저장
#             netflix = Netflix(
#                 full_path=full_path,
#                 full_paths=full_paths,
#                 jw_entity_id=jw_entity_id,
#                 object_type=object_type,
#                 poster=poster,
#                 poster_blur_hash=poster_blur_hash,
#                 scoring=scoring,
#                 title=title,
#                 tmdb_id=tmdb_id
#             )
#             netflix.save()

#     return render(request, 'netflix.html')

