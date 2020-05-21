
#추가, print('\n'*55)가능.옵션-컨피겨-제너럴-오토스퀴즈의 숫자 조절. 60이면 60이상 반복될 때 아이콘 하나로 표시됨.
#추가, 처음 보여주는 카드를 3번째, 혹은 2번째에 출력되게 할 수 있다. 남은 3장의 카드를 슬라이싱하면 가능?!
#추가, 예외입력처리, 하트9 처럼 쉼표 안적는 등의 경우, 한글,숫자,특수문자 등
#추가, 예외입력처리, 하트9 처럼 쉼표 안적는 등의 경우

#마술사와 조수
'''
마술 내용:
트럼프 카드 52장 중에서 5장을 뽑습니다.
그 중에서 4장을 보여주면
나머지 1장을 마술사가 알아맞춥니다.
'''

def input_5_cards(num2, cards):
    i=1
    while i < 6:
        a,b=input('%d번째 카드의 무늬와 숫자를 입력해주세요. : ' %i).split(',')        
        if b.isalpha():
            b=num2.index(b.lower())
            b+=1 
        b=int(b)
        a=a.lower()
        cards.append([a,b])
        i+=1
    return cards

def choice_sec_card(cards5): #무늬가 같은 두 카드를 비밀카드, 처음 보여줄 카드로 정한다. 즉, 처음 보여주는 카드의 무늬가 비밀카드의 무늬이다.

    overlap_shape=[]
    for a in cards5:
        i=0
        count=0
        while i < 5:
            if a[0] == cards5[i][0]: count+=1 #카드 자신의 무늬가 5장 안에 또 있는지 판단한다. 있을 때마다 카운트 1씩 올라간다.
            i+=1
        if count == 2: #카운트2:자신의 무늬를 발견할 때 +1, 다른 카드에서 같은 무늬를 발견하면 +1해서 총 카운트 2
            overlap_shape.append(a)

    sec_card=[]
    first_card=[]
    overlap_shape.sort() #정렬된 1번째, 2번째 원소는 반드시 서로 똑같은 무늬의 서로 다른 두 수.(여기서 앞 문자만 정렬되고 뒤의 숫자는 정렬되지 않았다고 가정하고 코딩한다.)
    x=overlap_shape[0][1] #무늬가 같은 첫번째 카드의 숫자
    y=overlap_shape[1][1] #무늬가 같은 두번째 카드의 숫자
    z=overlap_shape[0][0] #두 카드의 무늬
    if abs(x-y) <=6: #두 수의 차의 절대값이 6이하이면(참고로 두 숫자가 같을 수는 없다. 트럼프 카드에서 같은 무늬의 숫자는 1부터 13까지 하나씩만 있다.)
        if x > y: #두 수 중에서 큰 수를 비밀카드로 한다.
            sec_card=[z,x]
            first_card=[z,y]
            k=x-y
        else:
            sec_card=[z,y]
            first_card=[z,x]
            k=y-x
    else: #두 수의 차의 절대값이 7이상이면
        if x > y: #두 수 중에서 작은 수를 비밀카드로 한다.
            sec_card=[z,y]
            first_card=[z,x]
            k=(13-x)+y #보수(10과 1 사이의 거리는 9이지만, 13까지의 숫자로 보면 4이다.즉, ... 10,11,12,13,1,2 ... 순서이다.)
        else:
            sec_card=[z,x]
            first_card=[z,y]
            k=x+(13-y)

    print('비밀카드는',sec_card,'입니다.')
    print('처음 보여줄 카드는',first_card,'입니다.')
    print('비밀카드와 처음카드의 거리는',k,'입니다.')
    cards5.remove(sec_card)
    cards5.remove(first_card)
    print('그 다음 보여줄 세 장의 카드는',cards5,'입니다.')
    
    return sec_card, first_card, cards5, k

def sort_3_cards(num,shape,cards3,k,k_lists):
    x=0
    sort_cards3=[]
    for a in num: #무늬 행
        for b in shape: #숫자 열
            if [b,a] in cards3:
                x+=1
                sort_cards3.append([b,a,x])
            if x == 3: break
    print(sort_cards3)                

    sort_cards3_0=[]
    k_list=k_lists[k-1]
    print(k_list)
    for a in k_list:
        sort_cards3_0.append(sort_cards3[a-1])        
    print(sort_cards3_0)
    return sort_cards3_0

def print_show_4_cards(first_card,cards):
    print('비밀카드를 제외한 남은 네 장의 카드를 말씀드리겠습니다.')
    print(first_card)
    for i in cards:
        print(i)
    print('당신이 본 카드가 위의 4장이 맞는지 확인해주세요.')
    print('맞다면 마술사에게 이 카드를 보여주세요.')


#main
k_lists=[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] #컴퓨터와 나만 아는 암호코드이다. 두번째부터 출력되는 카드의 숫자 순서가 10, 5, 7 이면 크기대로 3,1,2이고 이것은 이 리스트의 5번째 원소이다. 
num=(1,2,3,4,5,6,7,8,9,10,11,12,13) #카드의 숫자는 1부터 13까지이다.
num2=('a',2,3,4,5,6,7,8,9,10,'j','q','k')
shape=('d','s','c','h') #중복된 숫자의 카드는 '다이아, 스페이드, 크리스탈, 하트' 순서의 무늬로 그 크기를 판단한다.

#1)5장의 카드를 입력받습니다.(입력받은 5장의 카드를 리스트 안의 리스트로 저장합니다.)
print('순서에 관계없이 5장의 카드를 차례로 입력해주세요.')
print('카드의 무늬, 쉼표, 숫자 또는 문자를 입력해주세요.')
print('ex1) h,6 (->하트 6) \nex2) d,a (->다이아 A)')

cards=[]
cards5=input_5_cards(num2,cards)

#1.5)컴퓨터가 비밀카드 한 장과 보여줄 카드 네 장을 선택합니다.

sec_card, first_card, cards3, k = choice_sec_card(cards5)

#1.8)컴퓨터가 관객과 마술사에게 4장의 카드를 보여줍니다. 카드를 정렬해서 보여줍니다.

sort_cards3 = sort_3_cards(num,shape,cards3,k,k_lists)

#2)이 중에서 4장의 카드를 관객에게 보여줍니다.

print_show_4_cards(first_card, sort_cards3)

#4)마술사가 남은 카드 한 장을 알아맞춥니다.
