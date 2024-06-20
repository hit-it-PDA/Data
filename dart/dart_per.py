# import requests

# # API 요청을 위한 기본 정보 설정
# crtfc_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # 발급받은 인증키
# corp_code = "00159023"  # 공시대상회사의 고유번호
# bsns_year = "2023"  # 사업연도
# reprt_code = "11014"  # 보고서 코드 (3분기보고서)
# idx_cl_code = "M210000"  # 지표분류코드 (수익성지표)

# # API 요청 URL 구성
# url = f"https://opendart.fss.or.kr/api/fnlttCmpnyIndx.json?crtfc_key={crtfc_key}&corp_code={corp_code}&bsns_year={bsns_year}&reprt_code={reprt_code}&idx_cl_code={idx_cl_code}"

# # API 요청 보내기
# response = requests.get(url)

# # 응답을 JSON 형식으로 파싱
# data = response.json()

# # 응답 상태 확인 및 데이터 출력
# if data["status"] == "000":
#     print("정상 응답")
#     for item in data["list"]:
#         print(f"보고서 코드: {item['reprt_code']}")
#         print(f"사업 연도: {item['bsns_year']}")
#         print(f"고유번호: {item['corp_code']}")
#         print(f"종목코드: {item['stock_code']}")
#         print(f"지표분류코드: {item['idx_cl_code']}")
#         print(f"지표분류명: {item['idx_cl_nm']}")
#         print(f"지표코드: {item['idx_code']}")
#         print(f"지표명: {item['idx_nm']}")
#         if 'idx_val' in item:
#             print(f"지표값: {item['idx_val']}")
#         print("-" * 40)
# else:
#     print(f"에러 발생: {data['message']}")

# 참조 - API
# https://blog.naver.com/eastfever5/222278729061