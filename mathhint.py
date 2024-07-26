def calculate_grade(percentage):
    # 퍼센트에 따른 등급 계산
    if percentage <= 4:
        return 1
    elif percentage <= 11:
        return 2
    elif percentage <= 23:
        return 3
    elif percentage <= 40:
        return 4
    elif percentage <= 60:
        return 5
    elif percentage <= 77:
        return 6
    elif percentage <= 89:
        return 7
    elif percentage <= 96:
        return 8
    else:
        return 9

def main():
    try:
        percentage = float(input("퍼센트를 입력하세요 (0에서 100 사이): "))
        if percentage < 0 or percentage > 100:
            print("올바른 퍼센트를 입력하세요. (0에서 100 사이)")
        else:
            grade = calculate_grade(percentage)
            print(f"퍼센트 {percentage}%는 내신 {grade}등급입니다.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")

if __name__ == "__main__":
    main()
