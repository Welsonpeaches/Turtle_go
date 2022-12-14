import turtle as tt


turn = 0
BOARD_X = 0
BOARD_Y = 0
STEP = 30


tt.speed(0)
tt.tracer(False)
tt.bgcolor('orange')
tt.pensize(1.5)

tt.hideturtle()



# 保存落子位置
turns = []






def draw_board(x, y, step):
    tt.speed(0)
    tt.tracer(False)
    tt.bgcolor('orange')
    tt.pensize(1.5)
    tt.hideturtle()



    
    # 计算左上角坐标
    
    start_x = x - 9 * step
    start_y = y + 9 * step

    
    # 画 19 条横线
    for i in range(19):
            tt.up()
            tt.goto(start_x, start_y - i * step)
            tt.down()
            tt.goto(start_x + step * 18, start_y -  i * step)

    

    

    # 画 19 条横线
    for i in range(19):
            tt.up()
            tt.goto(start_x + i * step, start_y)
            tt.down()
            tt.goto(start_x + i * step, start_y + -step * 18)

    #点星位
    #第一行
    tt.up()
    
    tt.goto(start_x + step * 15, start_y - step * 15)
    tt.dot(step * 10 / 30, 'black')

    
    tt.up()
    tt.goto(x, y)
    tt.dot(step * 10 / 30, 'black')
   
    
    for i in [3, 9, 15]:
        for j in [3, 9, 15]:
            tt.goto(start_x + step * j, start_y - step * i)
            tt.dot(step * 0.3, 'black')

def translate(x, y):
    return round(x / STEP) * STEP, round(y / STEP) * STEP


def translate_go(x, y):
    bx = x - (BOARD_X - 9 * STEP)
    lx = round(bx / STEP)

    by = y - (BOARD_Y + 9 * STEP)
    ly = round(by / -STEP)
    return lx, ly
def turns_to_str(ls):
    turns_str = ""
    for pos in ls:
        s = str(pos[0]) + ',' + str(pos[1]) + '\n'
        turns_str += s

    return turns_str




def save_turns():
    #print("保存文件")
    f = open("S3542647B.fufu", "w", encoding='utf8')
    
    f.write(turns_to_str(turns))
    f.close()

def save_str_to_turns(str_turns):
    lines = str_turns.split("\n")
    turns.clear()
    for line in lines:
        if line:
            pos_list = line.split(",")
            pos =(int(pos_list[0]),int(pos_list[1]))
            turns.append(pos)

    print(turns)


def draw_turns(turn_list):
    pass










def read_turns():
    #print("读取文件")
    file_name = 'S3542647B.fufu'
    f = open(file_name, "r", encoding="utf8")
    str_turns = f.read()
    f.close()


    save_str_to_turns(str_turns)
    draw_turns(turns)

def drop(x, y):
    # 如果棋子落在棋盘外面，那么就什么都不干，直接返回
    # 超出左边 或者 超出右边 或者 超出上边 或者 超出下边
    # 左边
    board_left = BOARD_X - 9 * STEP
    # 右边
    board_right = BOARD_X + 9 * STEP
    # 上边
    board_up = BOARD_Y + 9 * STEP
    # 下边
    board_down = BOARD_Y - 9 * STEP

    
    if x < board_left or x > board_right or \
       y > board_up or y < board_down:     
        return





    
    global turn

    bx, by = translate(x , y)
    tt.goto(bx, by)
    if turn == 0 and x < 270 and x> -270 and y < 270 and y > -270:
            tt.dot(30, 'black')
            turn += 1
        
    elif turn == 1 and x < 270 and x> -270 and y < 270 and y > -270:
            tt.dot(30, 'white')
            turn -= 1
    
    # 保存位置到列表(内存)中
    turns.append(translate_go(x, y))


def show_title():
    tt.up()
    tt.goto(0, 270)
    tt.write("Welcome to Turtle Go", align="center" ,font=('微软雅黑'))
    tt.goto(150, 270)
    tt.write("Ver0.0.2 made by Welsonpeaches@github.com", align="left", font=("微软雅黑",10))





    tt.goto(0,-300)
    tt.write('Press "S" to save the game, "R" to load the archive and "F" to restart the game', align="center",
             font=('宋体',10))   

def reset_board():
    tt.clear()
    show_title()
    draw_board(BOARD_X, BOARD_Y ,STEP)
    #清除数据
    turns.clear()

    



if __name__ == '__main__':
    draw_board(BOARD_X, BOARD_Y ,STEP)
    show_title()

    screen = tt.getscreen()

    
    screen.onclick(drop)


    screen.onkeypress(save_turns,"s")
    screen.onkeypress(read_turns,"r")
    screen.onkeypress(reset_board,"f")
    screen.listen()
    tt.mainloop()

