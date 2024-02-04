# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# 캐릭터 변수 선언
define ch_player = Character("나", color = "#62de7f")
define ch_sr1 = Character("타부서 직원1", color = "#4b37cc")
define ch_sr2 = Character("타부서 직원2", color = "#ed0000")
define ch_sr3 = Character("연관부서 직원3", color = "#4b37cc")
define ch_hr1 = Character("HR 부장1", color = "#ed0000")
define ch_cto1 = Character("이사1", color = "#ed0000")
define ch_ceo1 = Character("대표1", color = "#ed0000")
define ch_family1 = Character("나의 가족1", color = "#ed0000")

# The game starts here.


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


image bg_meeting = "bg/office_meeting.jpg"


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_office

    
    "나는 퇴사를 고민 중이다."
    "퇴사를 할 수 있을까?"

    $ player_name = renpy.input("당신의 이름은 무엇인가요?")

    $ player_name = player_name.strip()
    # The .strip() instruction removes any extra spaces the player 
    # may have typed by accident.
    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name="제민"


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # %(player_name)s s를 꼭 써야함
    ch_player "요새 퇴사를 진지하게 고민하고 있어"

    ch_sr1 "저도 고민중이에요. 회사에서 월급도 세 번 밀렸는데, 답이 없잖아요"
    ch_sr1 "저는 진짜 %(player_name)s 이 회사 퇴사하시면 저도 같이 퇴사할꺼에요"

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
