from TikTokApi import TikTokApi
verifyFp = "verify_l56tsajf_PQbOUBbe_ecKx_47ST_8yq4_W0wyv5tVksFK"
api = TikTokApi(custom_verify_fp=verifyFp)
userdata = api.user(username='eliaveve_').info()
print(userdata)