iМакрокоманды

Цель: Научиться обрабатывать ситуации с точки зрения SOLID, когда требуется уточнить существующее поведение без модификации существующего кода.

Предположим, что у нас уже написаны команды MoveCommand и RotateCommand. 
Теперь возникло новое требование: пользователи в игре могут устанавливать правило - во время движение расходуется топливо, двигаться можно только при наличии топлива.

Реализовать новую возможность можно введя две новые команды: 
1. CheckFuelCommand - проверяет, что топлива достаточно, если нет, то выбрасывает исключение CommandException.
2. BurnFuelCommand - уменьшает количество топлива на скорость расхода топлива.

После этого мы можем три команды выстроить в цепочку - CheckFuelCommand->MoveCommand->BurnFuelCommand

Чтобы это было прозрачно для пользователя реализуем Макрокоманду - специальную разновидность команды, которая в конструкторе принимает массив команда, а методе execute их все последовательно выполняет.
При повороте движущегося объекта меняется вектор мгновенной скорости. Напишите команду, которая модифицирует вектор мгновенной скорости, в случае поворота.
Постройте цепочку команд для поворота.
1. Реализовать класс CheckFuelCommand и тесты к нему.
2. Реализовать класс BurnFuelCommand и тесты к нему.
3. Реализовать простейшую макрокоманду и тесты к ней. Здесь простейшая - это значит, что при выбросе исключения вся последовательность команд приостанавливает свое выполнение,  
   а макрокоманда выбрасывает CommandException.
4. Реализовать команду движения по прямой с расходом топлива, используя команды с предыдущих шагов.
5. Реализовать команду для модификации вектора мгновенной скорости при повороте. Необходимо учесть, что не каждый разворачивающийся объект движется.
6. Реализовать команду поворота, которая еще и меняет вектор мгновенной скорости, если есть.

Критерии оценки:
1. Домашнее задание сдано - 2 балла.
2. Реализована команда CheckFuelCommand - 1балл
3. Написаны тесты к CheckFuelCommand - 1 балл
4. Реализована команда BurnFuelCommand - 1балл
5. Написаны тесты к BurnFuelCommand - 1 балл
6. Реализована команда MacroCommand - 1балл
7. Написаны тесты к MacroCommand - 1 балл
8. Реализована команда движения по прямой с расходом топлива и тесты к ней - 1 балл 
9. Реализована команда ChangeVelocityCommand - 1балл
10. Написаны тесты к ChangeVelocityCommand - 1 балл
11. Реализована команда поворота, которая еще и меняет вектор мгновенной скорости - 1балл
Итого: 12 баллов
Задание принято, если набрано не менее 8 баллов.

Рекомендуем сдать до: 10.10.2021