# Задание
Необходимо реализовать класс, представляющий собой ROS-ноду. Логика поведения ноды следующая:
* предполагается, что нода будет использоваться в совокупности с нодами turtlesim_node и turtle_teleop_key из пакета turtlesim
* разрабатываемая нода должна создавать второй движущийся объект в окне turtlesim_node. При этом стартовая черепашка будет управляться с клавиатуры, а вторая - нет
* необходимо реализовать возможность движения второй черепашки за первой. Для этого необходимо считывать координаты обеих черепашек через топики /<имя черепашки>/Pose, вычислять трансформацию между позициями и посылать команды в топик /<имя черепашки2>/cmd_vel
* необходимо обернуть разрабатываемую ноду в один класс, чтобы избежать глобальных переменных
* необходимо разработать launchfile, запускающий все требуемые ноды, а также установить в нём в качестве входного параметра скорость черепашки-преследователя.

# Окружение
OS Ubuntu 20.04, ROS Noetic

# Как запускать
В корневой папке проекта последовательно нужно ввести 3 команды:
* `catkin_make`
* `source devel/setup.bash`
* `roslaunch turtles_runner my_launch.launch`

На экране запустится окно с двумя черепашками.

# Управление
Окно консоли, с которой запускается roslaunch, должно быть в активном фокусе. Далее тыкаем стрелочки на клавиатуре для управления первой черепашкой. Движение стандартное для пакета `turtle_teleop_key`.

# Дополнительно
Для **смены скорости второй черепашки**, которая следует за первой, нужно создать отдельное окно консоли и ввести следующую команду:
`rosparam set /turtles_runner/speed *числовое_значение_скорости*`

Исходники для выполнения задания расположены в созданном пакете **turtles_runner** в папке **src**.
