import pkg_resources

import pydirectinput as direct
import pyautogui as auto
from python_imagesearch.imagesearch import imagesearch as search
from python_imagesearch.imagesearch import multimagesearch as msearch
from python_imagesearch.imagesearch import multimagesearchcoord as msearchcoord
from python_imagesearch.imagesearch import imagesearcharea as searcharea
from python_imagesearch.imagesearch import multimagesearcharea as msearcharea
import random
import time
from printy import printy
from printy import inputy
from dataclasses import dataclass


auto.FAILSAFE = False

global t1
t1 = 0.1
global t2
t2 = 0.2
global prec
prec = 0.8

# Start utility methods
def onscreen(path, precision=prec):
    return search(path, precision)[0] != -1


def onscreenarea(path, x1, y1, x2, y2, precision=prec):
    return searcharea(path, x1, y1, x2, y2, precision)[0] != -1


def click_key(key):
    auto.keyDown(key)
    time.sleep(random.uniform(t1, t2))
    auto.keyUp(key)


def click_left():
    auto.mouseDown(duration=random.uniform(t1, t2))
    time.sleep(random.uniform(t1, t2))
    auto.mouseUp(duration=random.uniform(t1, t2))


def click_right():
    auto.mouseDown(button="right", duration=random.uniform(t1, t2))
    time.sleep(random.uniform(t1, t2))
    auto.mouseUp(button="right", duration=random.uniform(t1, t2))


def click_to(path, button="left"):
    if onscreen(path):
        auto.moveTo(search(path), duration=random.uniform(t1, t2))
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
        auto.moveTo(888, 376, duration=random.uniform(t1, t2))
        click_right()
        time.sleep(random.uniform(t1, t2))
    main()


def bench_full(data):
    return


def bench_manager(data, champ):
    return


def buy(data):
    for i in data.shop:
        count = 0
        while count < 5 and onscreenarea(i, data.shop_area[0], data.shop_area[1], data.shop_area[2], data.shop_area[3]):
            count += 1
            if searcharea("./captures/empty_bench_8.png", data.scan_bench_pos[8][0], data.scan_bench_pos[8][1], data.scan_bench_pos[8][2], data.scan_bench_pos[8][3], prec)[0] == -1:
                bench_full(data)
            pos = searcharea(i, data.shop_area[0], data.shop_area[1], data.shop_area[2], data.shop_area[3], prec)
            auto.moveTo(pos[0] + data.shop_area[0], pos[1] + data.shop_area[1], duration=random.uniform(t1, t2))
            click_left()
            bench_manager(data, i)
    auto.moveTo(data.loot_pos[0], duration=random.uniform(t1, t2))


def scan_bench(data, bench):
    capt = ["./captures/empty_bench_0.png", "./captures/empty_bench_1.png", "./captures/empty_bench_2.png", "./captures/empty_bench_3.png", "./captures/empty_bench_4.png", "./captures/empty_bench_5.png", "./captures/empty_bench_6.png", "./captures/empty_bench_7.png", "./captures/empty_bench_8.png"]
    for i in range(0, len(bench)):
        if searcharea(capt[i], data.scan_bench_pos[i][0], data.scan_bench_pos[i][1], data.scan_bench_pos[i][2], data.scan_bench_pos[i][3], prec)[0] == -1:
            bench[i] = "xyz"


def sell_loot(data):
    new_bench = ["", "", "", "", "", "", "", "", ""]
    scan_bench(data, new_bench)
    for i in range(0, len(data.bench)):
        if data.bench[i] != new_bench[i]:
            sell(data.bench_pos[i], data)
            data.bench_champ[i] = ""


def search_loot(data):
    for i in data.loot_pos:
        auto.moveTo(i, duration=random.uniform(t1, t2))
        click_right()
        time.sleep(1)
    
def sell(pos, data):
    auto.moveTo(pos, duration=random.uniform(t1, t2))
    direct.press("e")
    # auto.moveTo(pos, duration=random.uniform(t1, t2))
    # auto.mouseDown(duration=random.uniform(t1, t2))
    # auto.moveTo(data.shop_pos[2], duration=random.uniform(t1, t2))
    # auto.mouseUp(duration=random.uniform(t1, t2))

def refresh(data):
    auto.moveTo(data.refresh_pos[0], data.refresh_pos[1], duration=random.uniform(t1, t2))
    click_left()

def buy_xp(data):
    auto.moveTo(data.buy_xp_pos[0], data.buy_xp_pos[1], duration=random.uniform(t1, t2))
    click_left()


def spiral(data, pos, step, nb_loop):
    negx = -1
    negy = 1
    stepx = 0
    stepy = 0
    t = 0
    for i in range(0, nb_loop * 4 + 1):
        if i % 2 == 1:
            negx *= -1
        if i % 2 == 0:
            negy *= -1
            t += 0.002
        if i % 4 == 1:
            stepx += 1
        if i % 4 == 0:
            stepy += 1
        auto.moveTo(pos[0] + negx * step * stepx, pos[1] + negy * step * stepy, duration=random.uniform(t1/5, t2/5))
        click_right()
        time.sleep(t)
    auto.moveTo(data.loot_pos[0], duration=random.uniform(t1, t2))
    click_right()


def read_item(data):
    for i in range(0, len(data.item_bench)):
        data.item_bench[i] = ""
    for i in range(0, len(data.item_bench)):
        auto.moveTo(data.item_pos[i], duration=random.uniform(t1, t2))
        data.item_bench[i] = msearcharea(data.item, data.item_bench_area[0], data.item_bench_area[1], data.item_bench_area[2], data.item_bench_area[3], precision=prec)


def put_item(data):
    for i in range(0, 5):
        if "./captures/rod.png" in data.item_bench and "./captures/chain.png" in data.item_bench:
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/rod.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/rod.png")] = ""
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/chain.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/chain.png")] = ""
            data.item_champ.append("locket")
        if not "qss" in data.item_champ and "./captures/glove.png" in data.item_bench and "./captures/negatron.png" in data.item_bench:
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/glove.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/glove.png")] = ""
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/negatron.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/negatron.png")] = ""
            data.item_champ.append("qss")
        if "./captures/belt.png" in data.item_bench and "./captures/sword.png" in data.item_bench:
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/belt.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/belt.png")] = ""
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/sword.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/sword.png")] = ""
            data.item_champ.append("zeke")
        if data.item_bench.count("./captures/sword.png") >= 2:
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/sword.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/sword.png")] = ""
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/sword.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/sword.png")] = ""
            data.item_champ.append("db")
        if ("qss" in data.item_champ or data.item_bench.count("./captures/glove.png") >= 2) and "./captures/bow.png" in data.item_bench:
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/glove.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/glove.png")] = ""
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/bow.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_champ.append("lw")
            data.item_bench[data.item_bench.index("./captures/bow.png")] = ""
        if ("qss" in data.item_champ or data.item_bench.count("./captures/glove.png") >= 2) and "./captures/tear.png" in data.item_bench:
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/glove.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/glove.png")] = ""
            auto.moveTo(data.item_pos[data.item_bench.index("./captures/tear.png")], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
            data.item_bench[data.item_bench.index("./captures/tear.png")] = ""
            data.item_champ.append("hoj")


def main():
    @dataclass
    class Data:
        shop:               list
        lantern_pos:        tuple
        buy_xp_pos:         tuple
        refresh_pos:        tuple
        interest_pos:       list
        bench_pos:          list
        scan_bench_pos:     list
        shop_pos:           list
        board_pos:          list
        item_pos:           list
        item_bench:         list
        slot_champ_item:    list
        item:               list
        loot_pos:           list
        loot:               list
        item_champ:         list
        shop_area:          list
        item_bench_area:    list
        board_champ:        list
        bench_champ:        list

    count = 0
    item_bench = ["", "", "", "", "", "", "", "", "", ""]
    item_bench_area = [231, 422, 1034, 1055]
    item_champ = []
    slot_champ_item = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    item = ["./captures/dice.png", "./captures/fon.png", "./captures/spatula.png", "./captures/magnet.png", "./captures/belt.png", "./captures/bow.png", "./captures/chain.png", "./captures/glove.png", "./captures/neeko.png", "./captures/negatron.png", "./captures/rod.png", "./captures/sword.png", "./captures/tear.png", "./captures/reforge.png"]
    shop = ["./captures/tristana_shop.png", "./captures/nidalee_shop.png", "./captures/diana_shop.png", "./captures/teemo_shop.png", "./captures/sivir_shop.png", "./captures/kindred_shop.png", "./captures/yuumi_shop.png", "./captures/shen_shop.png"]
    loot = ["./captures/blue_orb.png", "./captures/gold_orb.png", "./captures/white_orb.png"]
    lantern_pos = (943, 252)
    buy_xp_pos = (378, 959)
    refresh_pos = (383, 1040)
    item_pos = [(289, 754), (334, 722), (305, 689), (349, 663), (330, 634), (339, 596), (380, 629), (395, 592), (440, 631), (407, 664)]
    interest_pos = [[371, 509, 447, 579], [386, 445, 460, 515], [400, 381, 478, 458], [418, 326, 486, 396], [433, 273, 503, 336]]
    bench_pos = [(407, 761), (531, 763), (649, 763), (769, 766), (885, 763), (1005, 760), (1124, 766), (1243, 765), (1364, 768)]
    bench_champ = ["", "", "", "", "", "", "", "", ""]
    scan_bench_pos = [[370, 721, 478, 851], [479, 729, 598, 837], [592, 729, 719, 837], [716, 735, 841, 837], [828, 737, 961, 838], [947, 735, 1080, 840], [1062, 736, 1198, 837], [1177, 735, 1320, 837], [1294, 733, 1440, 842]]
    shop_pos = [(575, 980), (780, 980), (985, 980), (1180, 980), (1380, 980)]
    shop_area = [454, 887, 1547, 1075]
    loot_pos = [(580 - 120, 670), (1280 + 120, 590), (610 - 120, 510), (1280 + 120, 440), (549 - 120, 383), (1304 + 120, 299), (574 - 120, 248), (1243 + 120, 194)]
    board_pos = [[(568, 655), (698, 653), (829, 653), (956, 651), (1090, 654), (1219, 652), (1348, 656)], [(519, 572), (647, 572), (772, 570), (908, 566), (1021, 573), (1145, 572), (1268, 574)], [(598, 499), (713, 496), (837, 496), (957, 487), (1078, 491), (1198, 490), (1319, 489)], [(549, 420), (667, 426), (784, 423), (902, 421), (1015, 421), (1132, 423), (1249, 420)]]
    board_champ = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
    data = Data(shop, lantern_pos, buy_xp_pos, refresh_pos, interest_pos, bench_pos, scan_bench_pos, shop_pos, board_pos, item_pos, item_bench, slot_champ_item, item, loot_pos, loot, item_champ, shop_area, item_bench_area, board_champ, bench_champ)
    while not onscreen("./captures/2-4.png"):
        anyloot = msearchcoord(data.loot, precision=prec)
        if anyloot[0] != -1:
            auto.moveTo(anyloot, duration=random.uniform(t1, t2))
            click_right()
            time.sleep(2)
            spiral(data, anyloot, 40, 2)
            sell_loot(data)
            continue
        if count == 0 and onscreen("./captures/1-3.png"):
            count = 1
            auto.moveTo(data.shop_pos[0], duration=random.uniform(t1, t2))
            click_left()
            data.bench_champ[0] = "xyz"
            auto.moveTo(data.shop_pos[1], duration=random.uniform(t1, t2))
            click_left()
            auto.moveTo(data.bench_pos[1], duration=random.uniform(t1, t2))
            auto.mouseDown(duration=random.uniform(t1, t2))
            auto.moveTo(data.board_pos[1][3], duration=random.uniform(t1, t2))
            auto.mouseUp(duration=random.uniform(t1, t2))
        if count == 1 and onscreen("./captures/2-1.png"):
            count = 3
            sell(data.board_pos[0][3], data)
            sell(data.board_pos[1][3], data)
            sell(data.board_pos[2][3], data)
            data.bench_champ[0] = ""
            read_item(data)
            print(data.item_bench)
        buy(data)
        time.sleep(1)
        if count == 3 and onscreen("./captures/2-2.png"):
            count = 4
            put_item(data)
        if count == 4 and onscreen("./captures/2-3.png"):
            count = 5
            buy(data)
    while onscreen("./captures/2-4.png"):
        auto.moveTo(928, 396, duration=random.uniform(t1, t2))
        click_right()
        time.sleep(random.uniform(t1, t2))
    while not onscreen("./captures/2-7.png"):
        if count == 5:
            count = 6
            time.sleep(1)
            sell_loot(data)
            auto.moveTo(data.lantern_pos, duration=random.uniform(t1, t2))
            click_right()
            time.sleep(2)
            spiral(data, data.lantern_pos, 40, 2)
        buy(data)
        time.sleep(1)
    while not onscreen("./captures/3-4.png"):
        buy(data)
        time.sleep(1)
        while not onscreen("./captures/3-2.png"):
            direct.press("d")
            buy(data)
        if count == 6:
            count = 7
            search_loot(data)
            sell_loot(data)
            read_item(data)
        if count == 7 and onscreen("./captures/3-3.png"):
            count = 8
            put_item(data)
    exit("Success")

# End main process


# Start auth + main script
# while (1):
#     time.sleep(5)
#     auto.alert(auto.position())
start()
auto.alert("Press OK when you're in a TFT lobby!\n")
print("Bot started, queuing up!")
queue()

# End auth + main script
#video graphics quality medium
#full screen on my laptop