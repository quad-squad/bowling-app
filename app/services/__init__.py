def calculate_score_frame(pins):
    pins = pins.split(" ")
    frame = ""
    def new_frame():
        nonlocal frame
        nonlocal turn
        nonlocal num_pins_open
        frame = ""
        turn = -1
        num_pins_open = 10
    new_frame()
    frames = []
    for knock_out in pins:
        turn += 1
        num_pins_open -= int(knock_out)
        if  int(knock_out)==0 or turn==0:
            if turn == 1:
                frame += "-"
                frames.append(frame)
                new_frame()
            else:
                frame+=knock_out
        if turn==0 and num_pins_open==0:
            frames.append("X")
            new_frame()
        if turn==1 and num_pins_open==0:
            frame=frame[0] +  "/"
            frames.append(frame)
            new_frame()
        if turn==1 and num_pins_open!=0:
            frame+=knock_out
            frames.append(frame)
            new_frame()
    frames.append(frame)
    bonus = ''.join(frames[9:])
    del frames[9:]
    frames.append(bonus)

    return (' '.join(frames))

