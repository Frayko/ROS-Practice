# Как запускать
В корневой папке проекта последовательно нужно ввести 3 команды:
* `catkin_make`
* `source devel/setup.bash`
* `roslaunch turtles_runner my_launch.launch`

На экране запустится окно с двумя черепашками.

# Управление
Окно консоли, с которой запускается roslaunch, должно быть в активном фокусе. Далее тыкаем стрелочки на клавиатуре для управления первой черепашкой. Движение стандартное для для пакета `turtle_teleop_key`.

# Дополнительно
Для **смены скорости второй черепашки**, которая следует за первой, нужно создать отдельное окно консоли и ввести следующую команду:

`rosparam set /turtles_runner/speed *числовое_значение_скорости*`