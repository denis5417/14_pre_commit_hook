# Решатель квадратных уравнений

Программа для решения квадратных уравнений c автозапускаемыми тестами

# Тесты

Установите pre commit hook прежде чем комитить:
```!#bash
ln -s ../../pre-commit.sh .git/hooks/pre-commit
```

Примеры работы:

Программа работает корректно:
```!#bash
$ git commit -m "Good commit"
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
[master 2a8a5d9] Good commit
```
Программа работает с ошибками (коммит не происходит): 
```#!bash
$ git commit -m "Bad commit"
.E..
======================================================================
ERROR: test_returns_none_for_complex_solution (__main__.QuadraticEquationTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 22, in test_returns_none_for_complex_solution
    root1, root2 = get_roots(1, 2, 3)
  File "/Users/deniszvagincev/PycharmProjects/devman/14_pre_commit_hook/quadratic_equation.py", line 6, in get_roots
    root1 = (-b - sqrt(discriminant)) / (2 * a)
ValueError: math domain error

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (errors=1)
```

# Описание функций
`get_roots(a, b, c)` – принимает на вход коэффиценты в квадратном уравнение и возвращает:
  * `None, None` – если корней нет
  * `root1, None` – если есть только 1 корень
  * `root1, root2` – если уравнение имеет два корня
  
# Цели проекта

Этот код написан в образовательных целях. Тренировачный курс для веб-девелоперов - [DEVMAN.org](https://devman.org)
