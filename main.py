from game import Tank, Move, Rotate, CheckFuel, BurnFuel, \
                 BurnFuelMove, MovableAdapter, RotatableAdapter, CheckFuelAdapter, BurnFuelAdapter


if __name__ == '__main__':
    T1 = Tank()
    while True:
        print(f'Текущая позиция {T1.get_property("position")}\nБашня смотрит под углом {T1.get_property("direction")}')
        print()

        cmd_name = input('Ведите для движения move\n'
                         'для поворота rotate\n'
                         'для выхода q\n')
        if cmd_name == 'q':
            break
        if cmd_name == 'move':
            T1.velocity = [int(i) for i in input('Через запятую введите введите вектор скорости\n').split(',')]
            cm_l = [CheckFuel(CheckFuelAdapter(T1)), Move(MovableAdapter(T1)), BurnFuel(BurnFuelAdapter(T1))]
            BurnFuelMove(cm_l).execute()
            
        if cmd_name == 'rotate':
            T1.angle_velocity = int(input('Введите угол поворота\n'))
            Rotate(RotatableAdapter(T1)).execute()
            
