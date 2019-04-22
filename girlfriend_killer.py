import pyautogui
import time
import random
import pyperclip
girl_names = ["가이", "나린", "다슬", "라나", "늘봄", "드리", "루리", "민예", "규하", "초이", "태희", "민아", "민정", "혜교", "나영"]
wait_for_input_duration: int = 3
loop_for: int = 50
annoy_interval: float = 0.5
chat_room_position: pyautogui.Point = None
send_button_position: pyautogui.Point = None


def position_chat_room():
    global chat_room_position
    chat_room_position = pyautogui.position()


def position_send_button():
    global send_button_position
    send_button_position = pyautogui.position()


def get_annoying_message():
    global girl_names
    name = random.choice(girl_names)
    front_variants = ["하...", "흑 ㅠㅠ", "어떻게 말을 해야될지 모르겠네.."]
    front_form = random.choice(front_variants)

    tail_variants = ["잘지내? 보고 싶어 ㅠㅠ", "한번만더 기회를 줘"]
    tail_form = random.choice(tail_variants)
    return front_form + name + "야.. " + tail_form


def wait_for_input(input_name: str):
    print("Please position your pointer on : " + input_name + " ...")
    time.sleep(wait_for_input_duration)

def cp_paste_msg(msg):
    pyperclip.copy(msg)
    # if windows system ctrl, if mac os, cmd
    pyautogui.hotkey("command", "v")

def send_annoying_message_once():
    # locate chat room
    pyautogui.click(chat_room_position.x, chat_room_position.y)
    time.sleep(0.1)
    # enters message
    msg = get_annoying_message()
    cp_paste_msg(msg)

    time.sleep(0.1)

    # locate send message
    pyautogui.click(send_button_position.x, send_button_position.y)
    time.sleep(0.1)


def main():
    wait_for_input("채팅룸에 마우스")
    position_chat_room()
    wait_for_input("보내기 버튼에 마우스")
    position_send_button()

    for x in range(loop_for):
        send_annoying_message_once()


def test():
    msg = get_annoying_message()
    print(msg)


if __name__ == "__main__":
    main()
