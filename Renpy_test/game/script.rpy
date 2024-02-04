# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# 캐릭터 변수 선언
define ch_jemin = Character("제민", color = "#62de7f")
define ch_blue = Character("파랑", color = "#4b37cc")
define ch_red = Character("노을", color = "#ed0000")

# The game starts here.

# 독백용 
# 노블 = 전체 창에서 나오는 나레이터
# 비주얼 노벨 = 대화창만을 사용하는 나레이터

# 전체 창 나레이터
define narrator = Character(None, kind = nvl)
# 대화창에 나레이터
define ch_narrator = Character(None)

#이미지 
image bg_office = "bg/office.jpg"

# image 얼굴 바꾸기 
image scg_blue idle:
    im.FactorScale("character/blue/blue_idle.png", 1.8)

image scg_blue angry: 
    im.FactorScale("character/blue/blue_angry.png", 1.8)

image scg_blue happy: 
    im.FactorScale("character/blue/blue_happy.png", 1.8)

image scg_blue sad: 
    im.FactorScale("character/blue/blue_sad.png", 1.8)

image scg_red idle:
    im.FactorScale("character/red/red_idle.png", 1.8)

image scg_red angry:
    im.FactorScale("character/red/red_angry.png", 1.8)

image scg_red happy:
    im.FactorScale("character/red/red_happy.png", 1.8)

image scg_red sad:
    im.FactorScale("character/red/red_sad.png", 1.8)


image bg_classStart = "bg/office_meeting.jpg"



# label 밑에 하나로 침


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_office

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # 이름이 없는 나레이션은 전체 나레이션(창 나레이션)

    "제민이는 공부에 흥미가 없다."
    "그래서 숙제를 안한다."
    "이 게임은 제민이가 숙제를 베끼느냐 못 베끼느냐에 따라 엔딩 분기가 나뉩니다."

    # 나레이션 지우기용
    nvl clear

    "제민이는 학원 친구들과 학원에서 만났다."
    "첫번째 친구 파랑이는 말이 많고"
    "두번째 친구 노을이는 무뚝뚝하다."

    ch_jemin "왔냐"

    show scg_blue idle at left with dissolve

    ch_blue "안녕!"

    show scg_blue happy at left with dissolve

    show scg_red idle at right with dissolve

    ch_red "안녕~"

    show scg_red happy at right with dissolve

    ch_jemin "나 오늘 학원숙제 안했는데 숙제 보여줄 사람"

    ch_blue "오늘도 양심 없는 하루를 보내고 있구나"

    ch_red "..."


    # 엔딩 분기용
    $get_book = 0
    #$my_name = "제민"
    #$is_girl = True 
    $bad_friend =  False


    #선택지
    menu:
        "파랑이 숙제를 뺏는다":
            ch_jemin "파랑아 숙제 내놔라"
            ch_blue "누가 준다고 했냐?"
            menu:
                "강제로 뺏는다":
                    ch_blue "양아치냐?"
                    ch_narrator "숙제를 얻었다"
                    show scg_blue angry at left with dissolve
                    $bad_friend = True
                    $get_book = get_book + 1
                "뺏지 않는다":
                    ch_jemin "의리 없는 자식"
                    $get_book = get_book - 1

        "노을이 숙제를 뺏는다":
            ch_jemin "노을아 숙제 땡큐"
            show scg_red sad at right with dissolve
            ch_red "빨리 베끼고 내놔"
            ch_narrator "숙제를 얻었다"
            $get_book = get_book + 1

        "안 뺏는다":
            ch_jemin "의리 없는 자식들"
            $get_book = get_book - 1
    

    # 위 선택지가 끝나면 여기로 옴
    ch_jemin "아, 학원 때려치고 싶다. 숙제도 맨날 안하는데"
    "파랑, 노을" "말 만 하지 말고 좀 때려쳐봐라"

    ch_red "나 먼저 간다."

    hide scg_red with dissolve

    ch_narrator "노을이가 갔다."

    ch_blue "나도 간다."

    hide scg_blue with dissolve

    ch_narrator "파랑이도 갔다."

    ch_narrator "이제 곧 수업이 시작한다."


    #label을 부르는 2가지문 (call, jump)
    # call good_ending 을 할 경우 회귀문임 -> label의 return을 만나면 다시 call 문으로 돌아옴 (loop 문을 썼을 때 좋음)


    # 엔딩 분기용 조건
    # > < >= <= == != and or
    if (get_book > 0 and bad_friend == True):
        # jump하면 함수로 이동함 
        jump hidden_ending
    elif (get_book > 0): 
        jump good_ending
    else:
        jump normal_ending
    
    return

    # This ends the game.

    label good_ending:
        scene bg_classStart with dissolve
        ch_narrator "숙제를 베껴서 선생님께 혼나지 않았다."
        return
    # 메인메뉴로 돌아감

    label normal_ending:
        scene bg_classStart with dissolve
        ch_narrator "숙제를 하지 않아 선생님께 혼났다."
        return

    label hidden_ending:
        scene bg_classStart with dissolve
        ch_narrator "파랑이의 숙제를 베껴서 선생님께 혼나지는 않았지만, 파랑이에게 장문의 사과 문자를 보내야 했다. 다음 부터는 친구를 겁박하지 말자!"
        return   


