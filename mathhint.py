import pandas as pd

def count_hot_days(csv_path):
    # CSV 파일 읽기
    df = pd.read_csv(csv_path)

    # 날짜 열을 datetime 형식으로 변환
    df['date'] = pd.to_datetime(df['date'])

    # 년도 열 추가
    df['year'] = df['date'].dt.year

    # 30도 이상인 날 필터링
    hot_days = df[df['temperature'] >= 30]

    # 각 년도별로 30도 이상인 날짜 수 세기
    hot_days_count = hot_days.groupby('year').size()

    return hot_days_count

def main(csv_path):
    hot_days_count = count_hot_days(csv_path)
    print("년도별 30도 이상인 날짜 수:")
    print(hot_days_count)

if __name__ == "__main__":
    # 예시 CSV 파일 경로
    csv_path = 'daily.temp.csv'
    main(csv_path)
