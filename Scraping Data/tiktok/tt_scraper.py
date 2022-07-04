from TikTokApi import TikTokApi

api = TikTokApi(custom_verify_fp="verify_4f1234903b363062aff069c332688892")
x = []
for videos in api.search.users_alternate('holywings'):
    print(videos)