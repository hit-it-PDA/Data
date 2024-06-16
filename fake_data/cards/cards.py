import pandas as pd
import random
import datetime

# 카드사 정보 및 카드 번호 앞자리 설정
card_companies = {
    'KB국민카드': '381',
    '신한카드': '366',
    '하나카드': '044',
    '롯데카드': '368',
    'BC카드': '361'
}

# 카드 이름 및 종류 설정
card_names = {
    'KB국민카드': {
        '신용카드': '삼성페이 KB국민카드',
        '체크카드': '카카오페이 KB국민 체크카드'
    },
    '신한카드': {
        '신용카드': '신한카드 Point Plan',
        '체크카드': '신한카드 Pick E 체크 캐릭터형(루피)'
    },
    '하나카드': {
        '신용카드': '하나 CLUB H 아메리칸 익스프레스 리저브 카드',
        '체크카드': 'Young Hana+ 체크카드'
    },
    '롯데카드': {
        '신용카드': '롯데마트&MAXX 카드',
        '체크카드': '롯데포인트 플러스 체크카드'
    },
    'BC카드': {
        '신용카드': '[BC바로] GOAT BC바로카드',
        '체크카드': '[BC바로] 밥바라밥 페이북머니 체크카드'
    }
}

# 날짜 범위 설정
start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2024, 6, 12)

# 랜덤 날짜 생성 함수
def random_date(start, end):
    return start + datetime.timedelta(days=random.randint(0, (end - start).days))

# 은행 계좌 엑셀 파일 읽기
bank_accounts_df = pd.read_excel('../bank_accounts/db/bank_accounts.xlsx')

# 입출금 계좌를 가진 유저 필터링
filtered_users = bank_accounts_df[bank_accounts_df['account_type'] == '입출금'].drop_duplicates(subset=['user_id'])

# 데이터 생성
data = []
user_card_set = {}

for _, row in filtered_users.iterrows():
    user_id = row['user_id']
    account_no = row['account_no']
    
    num_cards = random.randint(0, 5)  # 유저가 가질 카드 개수를 0에서 5개 사이로 랜덤 설정
    user_card_set[user_id] = set()
    
    for _ in range(num_cards):
        company_name = random.choice(list(card_companies.keys()))
        card_type = random.choice(list(card_names[company_name].keys()))
        
        while (company_name, card_type) in user_card_set[user_id]:
            company_name = random.choice(list(card_companies.keys()))
            card_type = random.choice(list(card_names[company_name].keys()))
        
        card_no = card_companies[company_name] + ''.join([str(random.randint(0, 9)) for _ in range(13)])
        card_name = card_names[company_name][card_type]
        created_at = random_date(start_date, end_date)
        expired_at = created_at + datetime.timedelta(days=5*365)
        
        user_card_set[user_id].add((company_name, card_type))
        
        data.append([
            card_no, company_name, card_name, card_type, created_at, expired_at, user_id, account_no
        ])

# 데이터프레임 생성
df = pd.DataFrame(data, columns=[
    'card_no', 'company_name', 'card_name', 'card_type', 'created_at', 'expired_at', 'user_id', 'account_no'
])

# 엑셀 파일로 저장
df.to_excel('./db/cards.xlsx', index=False)
# 데이터프레임을 CSV로 저장
df.to_csv("./db/cards.csv", index=False)

print("엑셀, csv 파일이 생성되었습니다.")
