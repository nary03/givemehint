import pandas as pd

def find_recipes_by_ingredient(csv_path, ingredient_name):
    # CSV 파일 읽기
    df = pd.read_csv(csv_path)

    # 입력한 재료가 포함된 레시피 필터링
    filtered_recipes = df[df['ingredients'].apply(lambda x: ingredient_name in x.split(','))]

    # 레시피 목록 추출
    recipes = filtered_recipes['recipe'].tolist()

    return recipes

def main():
    csv_path = 'recipes.csv'
    ingredient_name = input("재료 이름을 입력하세요: ")
    recipes = find_recipes_by_ingredient(csv_path, ingredient_name)

    if len(recipes) > 0:
        print(f"'{ingredient_name}' 재료로 만들 수 있는 레시피 목록:")
        for recipe in recipes:
            print(recipe)
    else:
        print(f"'{ingredient_name}' 재료로 만들 수 있는 레시피를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
