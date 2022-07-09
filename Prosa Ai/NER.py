import requests
import pandas as pd
data = pd.read_excel('holywings.xlsx')
datas = data['berita'].to_string()
input_sentence = "indoseia makan jakarta anies baswedan membuntuh"
headers = {'x-api-key': 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ik5XSTBNemRsTXprdE5tSmtNaTAwTTJZMkxXSTNaamN0T1dVMU5URmxObVF4Wm1KaSIsInR5cCI6IkpXVCJ9.eyJhcHBsaWNhdGlvbl9pZCI6NzAzNjEsImxpY2Vuc2Vfa2V5IjoiMjRmMzExYmItNDhhMy00Y2E5LTlkYjUtZjYyZjI1YzMwYjlkIiwidW5pcXVlX2tleSI6IjFiMjk5Y2FmLTk4MTYtNDI2Yy1hNTg5LWEyYjM0NGZiZmJhOCIsInByb2R1Y3RfaWQiOjExLCJhdWQiOiJhcGktc2VydmljZSIsInN1YiI6Ijk3ZDljMjg3LWU5YzEtNGE4Yi1hZDMyLTI1ZjgwMzhjZDhlYSIsImV4cCI6MTY4ODQ2MTM5MSwiaXNzIjoiY29uc29sZSIsImlhdCI6MTY1NjkyNTM5MX0.RugtQ5z5KwBKG2AtTVOwsvlcnQ7PVNNVekLAVQm1_sGWDCVIFDqn_xeLQthQCCQIYgNxkuAbmbdUOky16PvvTT4YTDy1dOZCXWTR79BjdAwa6-v-Z0nzLJEVjYmU-Pldz1LTqgij2ba2kHd741hPuW5zUiSK7vS8_-TlJut5GPRagHJEtI5LuqQ_gqvQqQpXv5AtEn0byAgcWYnC1gcE_baRzZbor2NAL-H4LFaQi8X8522TRZCxoInOe6QLkuPVkyCy4SgabQjZ2UriuGipsAPVddxBhWqNCQKOUGPUeStiBxyxypiXaFu2ks2IYL5_hL7F-7a9zJ8lN0fg-4Y-Rw',
           'Content-Type': 'application/json'}
body = {'text': input_sentence}
r_pos = requests.post('https://api.prosa.ai/v2/text/ner', headers = headers, json = body)
print(datas)
print(r_pos.content)