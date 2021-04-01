import pkg_resources

import pyautogui as auto
from python_imagesearch.imagesearch import imagesearch as search
from python_imagesearch.imagesearch import imagesearcharea as searcharea
import random
import time
from printy import printy
from printy import inputy


auto.FAILSAFE = False


# Start utility methods
def onscreen(path, precision=0.8):
    return search(path, precision)[0] != -1


def search_to(path):
    pos = search(path)
    if onscreen(path):
        auto.moveTo(pos, duration=random.uniform(0.1, 0.2))
        return pos


def click_key(key):
    auto.keyDown(key)
    time.sleep(random.uniform(0.1, 0.2))
    auto.keyUp(key)


def click_left():
    auto.mouseDown(duration=random.uniform(0.1, 0.2))
    time.sleep(random.uniform(0.1, 0.2))
    auto.mouseUp(duration=random.uniform(0.1, 0.2))


def click_right():
    auto.mouseDown(button="right", duration=random.uniform(0.1, 0.2))
    time.sleep(random.uniform(0.1, 0.2))
    auto.mouseUp(button="right", duration=random.uniform(0.1, 0.2))


def click_to(path, button="left"):
    if onscreen(path):
        auto.moveTo(search(path), duration=random.uniform(0.1, 0.2))
        if button == "left":
            click_left()
        elif button == "right":
            click_right()
# End utility methods


# Start main process
def queue():
    click_to("./captures/find match ready.png")
    while not onscreen("./captures/accept.png"):
        time.sleep(1)
    click_to("./captures/accept.png")
    print("Loading!")
    loading()


def loading():
    while not onscreen("./captures/1-1.png"):
        time.sleep(random.uniform(0.5, 1.5))

    print("Match starting!")
    start()


def start():
    while onscreen("./captures/1-1.png"):
        auto.moveTo(888, 376, duration=random.uniform(0.1, 0.2))
        click_right()
        time.sleep(random.uniform(0.1, 0.2))
    main()


def buy(shop, scan_bench_pos, board_pos):
    for i in shop:
        while onscreen(i):
            if searcharea("./captures/empty_bench.png", scan_bench_pos[8][0], scan_bench_pos[8][1], scan_bench_pos[8][2], scan_bench_pos[8][3], 0.8) != -1:
                auto.moveTo(board_pos[8][0], duration=random.uniform(0.1, 0.2))
                click_key("e")
            click_to(i)


def scan_bench(bench, scan_bench_pos):
    for i in bench:
        if searcharea("./captures/empty_bench.png", scan_bench_pos[i][0], scan_bench_pos[i][1], scan_bench_pos[i][2], scan_bench_pos[i][3], 0.8)[0] == -1:
            bench[i] = 1


def sell_loot(bench, bench_pos, scan_bench_pos):
    new_bench = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    scan_bench(new_bench, scan_bench_pos)
    for i in range(0, bench.len()):
        if bench[i] != new_bench[i]:
            auto.moveTo(bench_pos[i], duration=random.uniform(0.1, 0.2))
            click_key("e")


def search_loot(loot):
    for i in loot:
        while onscreen(i):
            click_to(i, "right")



def main():
    count = 1
    bench = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    shop = ["./captures/tristana_shop.png", "./captures/nidalee_shop.png", "./captures/diana_shop.png", "./captures/teemo_shop.png", "./captures/sivir_shop.png", "./captures/yuumi_shop.png"]
    loot = ["./captures/blue_orb.png", "./captures/gold_orb.png", "./captures/white_orb.png", "./captures/coin.png"]
    interest_pos = [[371, 509, 447, 579], [386, 445, 460, 515], [400, 381, 478, 458], [418, 326, 486, 396], [433, 273, 503, 336]]
    bench_pos = [(450, 777), (570, 777), (690, 777) , (810, 777), (930, 777), (1050, 777), (1170, 777), (1290, 777), (1410, 777)]
    scan_bench_pos = [[370, 721, 478, 851], [479, 729, 598, 837], [592, 729, 719, 837], [716, 735, 841, 837], [828, 737, 961, 838], [947, 735, 1080, 840], [1062, 736, 1198, 837], [1177, 735, 1320, 837], [1294, 733, 1440, 842]]
    shop_pos = [(575, 980), (780, 980), (985, 980), (1180, 980), (1380, 980)]
    board_pos = [[(560, 440), (680, 440), (800, 440), (920, 440), (1040, 440), (1160, 440), (1280, 440)], [(610, 510), (730, 510), (850, 510), (970, 510), (1090, 510), (1210, 510), (1330, 510)], [(540, 590), (660, 590), (780, 590), (910, 590), (1040, 590), (1160, 590), (1280, 590)], [(580, 670), (710, 670), (840, 670), (970, 670), (1100, 670), (1230, 670), (1360, 670)]]
    while not onscreen("./captures/carou.png"):
        if searcharea("./captures/empty_bench.png", scan_bench_pos[0][0], scan_bench_pos[0][1], scan_bench_pos[0][2], scan_bench_pos[0][3], 0.8)[0] != -1 and (onscreen("./captures/1-2.png") or onscreen("./captures/1-3.png")):
            auto.moveTo(shop_pos[0], duration=random.uniform(0.1, 0.2))
            click_left()
        if count and onscreen("./captures/2-1.png"):
            count = 0
            auto.moveTo(board_pos[3][0], duration=random.uniform(0.1, 0.2))
            click_key("e")
            auto.moveTo(board_pos[3][1], duration=random.uniform(0.1, 0.2))
            click_key("e")
            auto.moveTo(board_pos[3][2], duration=random.uniform(0.1, 0.2))
            click_key("e")
            scan_bench(bench, scan_bench_pos)
            search_loot(loot)
            sell_loot(bench, bench_pos, scan_bench_pos)
        buy(shop, scan_bench_pos, board_pos)
        time.sleep(1)
    while onscreen("./captures/carou.png"):
        auto.moveTo(928, 396, duration=random.uniform(0.1, 0.2))
        click_right()
        time.sleep(random.uniform(0.1, 0.2))
    while not onscreen("./captures/golems.png"):
        buy(shop, scan_bench_pos, board_pos)
        time.sleep(1)
    while not onscreen("./captures/carou.png"):
        buy(shop, scan_bench_pos, board_pos)
        while not onscreen("./captures/3-2.png") and searcharea("./captures/orb_interest.png", interest_pos[0][0], interest_pos[0][1], interest_pos[0][2], interest_pos[0][3], 0.8)[0] != -1:
            click_key("d")
            buy(shop, scan_bench_pos, board_pos)
        exit("Success")


def surrender():
    time.sleep(15)

    time.sleep(1)

    while onscreen("./captures/missions ok.png"):
        click_to("./captures/missions ok.png")
        time.sleep(2)
    while onscreen("./captures/skip waiting for stats.png"):
        click_to("./captures/skip waiting for stats.png")
    time.sleep(5)
    while onscreen("./captures/play again.png"):
        click_to("./captures/play again.png")

    time.sleep(10)
    print("Queuing up again!")
    queue()
# End main process


# Start auth + main script
while (1):
    time.sleep(3)
    auto.alert(auto.position())
auto.alert("Press OK when you're in a TFT lobby!\n")
print("Bot started, queuing up!")
queue()

# End auth + main script
